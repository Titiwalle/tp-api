from flask import Blueprint, jsonify, request
from models import Espece, Taxonomie, Pays, Auteur, Image
from database import db


especes_bp = Blueprint("especes", __name__)

@especes_bp.route("/especes", methods=["GET"])
def get_especes():
    especes = Espece.query.all()

    data = []
    for e in especes:
        data.append({
            "id": e.id_espece,
            "nom_scientifique": e.nom_scientifique,
            "description": e.description,
            "taille": e.taille,
            "poids": e.poids,
            "longevite": e.longevite,
            "individus": e.individus,
            "taxonomie": {
                "ordre": e.taxonomie.ordre,
                "famille": e.taxonomie.famille,
                "genre": e.taxonomie.genre
            },
            "pays": {
                "nom": e.pays.nom_pays,
                "continent": e.pays.continent
            },
            "images": [img.url for img in e.images]
        })

    return jsonify(data)

@especes_bp.route("/especes/<int:id_espece>", methods=["GET"])
def get_espece(id_espece):
    e = Espece.query.get_or_404(id_espece)

    data = {
        "id": e.id_espece,
        "nom_scientifique": e.nom_scientifique,
        "description": e.description,
        "taille": e.taille,
        "poids": e.poids,
        "longevite": e.longevite,
        "individus": e.individus,
        "taxonomie": {
            "ordre": e.taxonomie.ordre,
            "famille": e.taxonomie.famille,
            "genre": e.taxonomie.genre
        },
        "pays": {
            "nom": e.pays.nom_pays,
            "continent": e.pays.continent
        },
        "images": [img.url for img in e.images]
    }

    return jsonify(data)



@especes_bp.route("/especes", methods=["POST"])
def add_espece():
    data = request.json

    # Vérification des champs obligatoires
    required = [
        "nom_scientifique", "description", "taille", "poids", "longevite",
        "individus", "taxonomie", "pays", "auteur"
    ]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Champ manquant : {field}"}), 400

    # --- TAXONOMIE ---
    t = Taxonomie(
        ordre=data["taxonomie"]["ordre"],
        famille=data["taxonomie"]["famille"],
        genre=data["taxonomie"]["genre"]
    )
    db.session.add(t)
    db.session.commit()

    # --- AUTEUR ---
    a = Auteur(
        nom=data["auteur"]["nom"],
        prenom=data["auteur"]["prenom"]
    )
    db.session.add(a)
    db.session.commit()

    # --- PAYS ---
    p = Pays(
        nom_pays=data["pays"]["nom"],
        continent=data["pays"]["continent"]
    )
    db.session.add(p)
    db.session.commit()

    # --- ESPECE ---
    e = Espece(
        nom_scientifique=data["nom_scientifique"],
        description=data["description"],
        taille=data["taille"],
        poids=data["poids"],
        longevite=data["longevite"],
        individus=data["individus"],
        id_taxonomie=t.id_taxonomie,
        id_auteur=a.id_auteur,
        id_pays=p.id_pays
    )
    db.session.add(e)
    db.session.commit()

    # --- IMAGES (optionnel) ---
    if "images" in data:
        for url in data["images"]:
            img = Image(url=url, id_espece=e.id_espece)
            db.session.add(img)
        db.session.commit()

    return jsonify({
        "message": "Espèce ajoutée avec succès",
        "id_espece": e.id_espece
    }), 201


@especes_bp.route("/especes/<int:id_espece>", methods=["DELETE"])
def delete_espece(id_espece):
    espece = Espece.query.get(id_espece)

    if not espece:
        return jsonify({"error": "Espèce introuvable"}), 404

    # Supprimer les images associées
    for img in espece.images:
        db.session.delete(img)

    # Supprimer l'espèce
    db.session.delete(espece)
    db.session.commit()

    return jsonify({"message": f"Espèce {id} supprimée avec succès"}), 200


@especes_bp.route("/especes/<int:id_espece>/images", methods=["POST"])
def add_image(id_espece):
    espece = Espece.query.get(id_espece)
    if not espece:
        return jsonify({"error": "Espèce introuvable"}), 404

    data = request.json
    img = Image(url=data["url"], id_espece=id_espece)
    db.session.add(img)
    db.session.commit()

    return jsonify({"message": "Image ajoutée"}), 201