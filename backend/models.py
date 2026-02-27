from database import db

class Auteur(db.Model):
    id_auteur = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))

class Taxonomie(db.Model):
    id_taxonomie = db.Column(db.Integer, primary_key=True)
    ordre = db.Column(db.String(100))
    famille = db.Column(db.String(100))
    genre = db.Column(db.String(100))

class Pays(db.Model):
    id_pays = db.Column(db.Integer, primary_key=True)
    nom_pays = db.Column(db.String(150))
    continent = db.Column(db.String(100))

class Espece(db.Model):
    id_espece = db.Column(db.Integer, primary_key=True)
    nom_scientifique = db.Column(db.String(200))
    description = db.Column(db.Text)
    taille = db.Column(db.Float)
    poids = db.Column(db.Float)
    longevite = db.Column(db.Integer)
    individus = db.Column(db.Integer)

    id_taxonomie = db.Column(db.Integer, db.ForeignKey('taxonomie.id_taxonomie'))
    id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id_auteur'))
    id_pays = db.Column(db.Integer, db.ForeignKey('pays.id_pays'))

    taxonomie = db.relationship("Taxonomie")
    auteur = db.relationship("Auteur")
    pays = db.relationship("Pays")
    images = db.relationship("Image", cascade="all, delete")

class Image(db.Model):
    id_image = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(300))
    id_espece = db.Column(db.Integer, db.ForeignKey('espece.id_espece'))