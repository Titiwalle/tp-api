from app import app
from database import db
from models import Auteur, Taxonomie, Pays, Espece, Image

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- AUTEURS ---
    auteurs = [
        Auteur(nom="Durand", prenom="Alice"),
        Auteur(nom="Martin", prenom="Louis"),
        Auteur(nom="Bernard", prenom="Claire"),
        Auteur(nom="Petit", prenom="Hugo"),
        Auteur(nom="Robert", prenom="Emma"),
    ]
    db.session.add_all(auteurs)
    db.session.commit()

    # --- TAXONOMIES ---
    taxonomies = [
        Taxonomie(ordre="Accipitriformes", famille="Accipitridae", genre="Aquila"),
        Taxonomie(ordre="Passeriformes", famille="Corvidae", genre="Corvus"),
        Taxonomie(ordre="Falconiformes", famille="Falconidae", genre="Falco"),
        Taxonomie(ordre="Passeriformes", famille="Muscicapidae", genre="Erithacus"),
        Taxonomie(ordre="Passeriformes", famille="Paridae", genre="Cyanistes"),
        Taxonomie(ordre="Strigiformes", famille="Strigidae", genre="Bubo"),
        Taxonomie(ordre="Ciconiiformes", famille="Ciconiidae", genre="Ciconia"),
        Taxonomie(ordre="Procellariiformes", famille="Diomedeidae", genre="Diomedea"),
        Taxonomie(ordre="Sphenisciformes", famille="Spheniscidae", genre="Aptenodytes"),
        Taxonomie(ordre="Pelecaniformes", famille="Pelecanidae", genre="Pelecanus"),
        Taxonomie(ordre="Apodiformes", famille="Trochilidae", genre="Archilochus"),
        Taxonomie(ordre="Psittaciformes", famille="Psittacidae", genre="Ara"),
        Taxonomie(ordre="Apterygiformes", famille="Apterygidae", genre="Apteryx"),
        Taxonomie(ordre="Casuariiformes", famille="Casuariidae", genre="Casuarius"),
        Taxonomie(ordre="Phoenicopteriformes", famille="Phoenicopteridae", genre="Phoenicopterus"),
        Taxonomie(ordre="Pelecaniformes", famille="Ardeidae", genre="Egretta"),
        Taxonomie(ordre="Passeriformes", famille="Passeridae", genre="Passer"),
        Taxonomie(ordre="Struthioniformes", famille="Struthionidae", genre="Struthio"),
        Taxonomie(ordre="Strigiformes", famille="Strigidae", genre="Bubo"),
        Taxonomie(ordre="Piciformes", famille="Ramphastidae", genre="Ramphastos"),
    ]
    db.session.add_all(taxonomies)
    db.session.commit()

    # --- PAYS ---
    pays = [
        Pays(nom_pays="France", continent="Europe"),
        Pays(nom_pays="Kenya", continent="Afrique"),
        Pays(nom_pays="Chili", continent="Amérique du Sud"),
        Pays(nom_pays="États-Unis", continent="Amérique du Nord"),
        Pays(nom_pays="Brésil", continent="Amérique du Sud"),
        Pays(nom_pays="Nouvelle-Zélande", continent="Océanie"),
        Pays(nom_pays="Australie", continent="Océanie"),
        Pays(nom_pays="Canada", continent="Amérique du Nord"),
        Pays(nom_pays="Antarctique", continent="Antarctique"),
    ]
    db.session.add_all(pays)
    db.session.commit()

    # --- ESPECES ---
    especes = [
        Espece(nom_scientifique="Aquila chrysaetos", description="Aigle royal", taille=80, poids=4.5, longevite=25, individus=12000, id_taxonomie=1, id_auteur=1, id_pays=1),
        Espece(nom_scientifique="Corvus corax", description="Grand corbeau", taille=65, poids=1.2, longevite=15, individus=500000, id_taxonomie=2, id_auteur=2, id_pays=1),
        Espece(nom_scientifique="Falco peregrinus", description="Faucon pèlerin", taille=40, poids=0.9, longevite=13, individus=140000, id_taxonomie=3, id_auteur=3, id_pays=1),
        Espece(nom_scientifique="Erithacus rubecula", description="Rouge-gorge familier", taille=14, poids=0.02, longevite=5, individus=13000000, id_taxonomie=4, id_auteur=4, id_pays=1),
        Espece(nom_scientifique="Cyanistes caeruleus", description="Mésange bleue", taille=12, poids=0.011, longevite=3, individus=20000000, id_taxonomie=5, id_auteur=5, id_pays=1),
        Espece(nom_scientifique="Bubo bubo", description="Grand-duc d’Europe", taille=70, poids=2.7, longevite=20, individus=20000, id_taxonomie=6, id_auteur=1, id_pays=1),
        Espece(nom_scientifique="Ciconia ciconia", description="Cigogne blanche", taille=100, poids=3.5, longevite=25, individus=230000, id_taxonomie=7, id_auteur=2, id_pays=1),
        Espece(nom_scientifique="Diomedea exulans", description="Albatros hurleur", taille=120, poids=8.5, longevite=50, individus=20000, id_taxonomie=8, id_auteur=3, id_pays=3),
        Espece(nom_scientifique="Aptenodytes forsteri", description="Manchot empereur", taille=115, poids=30, longevite=20, individus=595000, id_taxonomie=9, id_auteur=4, id_pays=9),
        Espece(nom_scientifique="Pelecanus onocrotalus", description="Pélican blanc", taille=160, poids=10, longevite=25, individus=300000, id_taxonomie=10, id_auteur=5, id_pays=2),
        Espece(nom_scientifique="Archilochus colubris", description="Colibri à gorge rubis", taille=9, poids=0.003, longevite=6, individus=7000000, id_taxonomie=11, id_auteur=1, id_pays=4),
        Espece(nom_scientifique="Ara ararauna", description="Ara bleu", taille=85, poids=1.2, longevite=35, individus=100000, id_taxonomie=12, id_auteur=2, id_pays=5),
        Espece(nom_scientifique="Apteryx mantelli", description="Kiwi brun", taille=45, poids=2.8, longevite=20, individus=25000, id_taxonomie=13, id_auteur=3, id_pays=6),
        Espece(nom_scientifique="Casuarius casuarius", description="Casoar à casque", taille=150, poids=45, longevite=40, individus=20000, id_taxonomie=14, id_auteur=4, id_pays=7),
        Espece(nom_scientifique="Phoenicopterus roseus", description="Flamant rose", taille=120, poids=3, longevite=30, individus=680000, id_taxonomie=15, id_auteur=5, id_pays=2),
        Espece(nom_scientifique="Egretta garzetta", description="Aigrette garzette", taille=60, poids=0.4, longevite=10, individus=700000, id_taxonomie=16, id_auteur=1, id_pays=1),
        Espece(nom_scientifique="Passer domesticus", description="Moineau domestique", taille=15, poids=0.03, longevite=4, individus=540000000, id_taxonomie=17, id_auteur=2, id_pays=1),
        Espece(nom_scientifique="Struthio camelus", description="Autruche d’Afrique", taille=210, poids=100, longevite=40, individus=150000, id_taxonomie=18, id_auteur=3, id_pays=2),
        Espece(nom_scientifique="Bubo scandiacus", description="Harfang des neiges", taille=65, poids=2.5, longevite=10, individus=280000, id_taxonomie=19, id_auteur=4, id_pays=8),
        Espece(nom_scientifique="Ramphastos toco", description="Toucan toco", taille=60, poids=0.6, longevite=20, individus=100000, id_taxonomie=20, id_auteur=5, id_pays=5),
    ]
    db.session.add_all(especes)
    db.session.commit()

    # --- IMAGES ---
    images = [
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx_tP2bhOW7kMSo8AXtRWQi_-HOsg6cTShyCdb1AERBVKiMK9L_-RCCo7tlbN6X-oIwpJ6O2JxmX_Kd0664HbvgAFGoyVXR7_RaoMsxA&s=10", id_espece=1),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE62s4V2krbw9Vy3cqFY4Akp8zCZCEaI4MXahTBV-6mNmT3gYQh1w60bVwoh2drhfhUnUHZoXdE4JzO5qst6YMG5iZUeXScnIDy8oRCvV7&s=10", id_espece=2),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgkb84XajzOMB3lCfAXl3T5EuoiU9RUeRP-LxrXgAmLvHaGmbSeML4W7sCllquiBqE8HWxUxUoBFDpa4xaFYLEMyFsdVJSaKMgJ7jKgKiB&s=10", id_espece=3),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfpRBiUZ3oK4YHtBZqELY_fjkHxKFeedV45gn9FqZzhRCox5YcroeVYNQumiX2KPEqdEZkd8zl1n6AFBNUkcJTxPZM3wPOgtRaQnXQfBkj&s=10", id_espece=4),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJeg7_KgjqFDEK6d3pTJSi3FNTiWWbvAOpP0adQB5bDuY8C9YbCB72kCe3j1_PX-4ADYOWzE3_vKrbdLm1KSZXf-qu7degl3iiet7TFoAKwA&s=10", id_espece=5),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJmDM_-XIumqWRx7dqlrPInkd806QhR8S2JYJl2q6V8pnYpwg23ZY6qECfPHkP0LDsrQMuW2ejG2GqYBP2RjSKKwJqGYPK8E56yvbDsyI8OQ&s=10", id_espece=6),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8zcc56IfQFtFM7ZNHsABDmEw6v_Kz0VS6FtP1MfQsHzG28Pr4i4o4ksBNJDhpMOmvVLl5SotfHbxM1Z-kreFYaKEzMKYz1cgR4RaT0z7V&s=10", id_espece=7),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-WcCIA--cGiGNCt_WSM8Ji6BTut1R2X2MsOFyMeIVMkU6IsPzXQVJcolp22HBA1ICKJyQs9S1Fy6-Mk4eWrchr8ZaomnynFFyCPPwkJYXlA&s=10", id_espece=8),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFITgyWlzpBuFRjBGmP965YBfPW33-ex6DE1aF2W_rt0PPrVmgCr7mNjFRNlKW80XFzDdY54cMoGjBmAD5poFUj8_ChjmxkfUwUenD_3-wLQ&s=10", id_espece=9),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh7BLiOy-8KWuxF-X7HM1yorOHzQ3DD4bf60LDMdZFWWDL8OOip_pXfqW8I9aMwGQjJcwia3atS1-cuiLFZtTC2gD3TlpiZZn5NYgsUcSR&s=10", id_espece=10),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC7qCfZxaCrBIr2KBna3MJZM6s1NOen7NoBo7ezn-p63aUUmIR-yYZR5KGvHd_7G7fsh-lhwdCSzIF9_B-p4f8JAvgVVG7IlbNfa3swGwb&s=10", id_espece=11),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTdYdjgESUKbup5Ea8LiizaMhdTicpDEDJgEDYucitgCKycBEhNBEi2UfzzfNfKX40U62i3T3yeMFrxEf1wmoGRfCuKMgiBku8hzorIBuj&s=10", id_espece=12),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3HgR1-raLKKZgvqbOI6BSkp0YZX9bmISYmFsFWOlVHxqQoo8aIbLios-vDtphZ_GAhdyonE6C0_zpeKVqun1jCHslqeBRwN3Pmt9KSNQ9pw&s=10", id_espece=13),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTis4xYA--vHPv8byZKMNE3kwTEC0rNqxGyHZyIrP-4fLaiIPcupzO0T7bIbzHt-Ni4Ijw_Rk4q6B_9je9sh-LUfC9cAAEi7egCwJmXHgX_-g&s=10", id_espece=14),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg_cSerrovb9zcgBWw7YWEI3MnbE0v9_6buXJdDz2zZ8Wr_c--_KY2TUdFGbUAn7Mi-Kj975J7MPwGcha-fT7aBVaBb67CwdP_LB7dDg6v&s=10", id_espece=15),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVQbLkdmOT5RtYf2OafsverXw5aOOvvECPD5pNRjSBWZu_8xI4bKEwNuXKcauhOz9NXqzd2rZmj5zQGuVlmj3lMDXHCOaXMLRVVkdT0eiv2w&s=10", id_espece=16),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW-xgMB5c_TlvujKVfBMAdZIhIAQYAAh-FfXq7Mpka3ZiLr3sarx51x1-0-aCaNUzvJG_CgJeopJB9OTlLsnXxBq02HcycGsOCfAhVlaRHsQ&s=10", id_espece=17),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL2Lv2jjZE38sQWlh567MM1N4Ay510-y8-w51OBSQLXKMcHw_504pB0FMARf_vwqHyZvJ7b2EoPfJhUYvvxgD2IH_d1vIG7i9_bVJrhoXHDw&s=10", id_espece=18),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR24mSSUHtsGQKrht6Gqgc05KX9geuaEPOO8XuivOy2vKjGEcKE49odHjr7-dP7TYR-JzbrTxbF6cGYP2PAUACqF2O7I9sz2MZXL5fMmQLb&s=10", id_espece=19),
        Image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIHH6x2aLjItthmsQNK3Zgxgdzkb8l5yknx4h-D2C1_XVJZHDEvN1eovKBBXY0X5AGG1inVLExKalTrJwuVMk-hwzzPCZOWx8C-AoRcauj&s=10", id_espece=20),
    ]
    db.session.add_all(images)
    db.session.commit()


    print("Données d'oiseaux insérées avec succès !")