import { useState } from "react";
import { URL_data } from "../config";


function PageAjoutEspece() {
  const [form, setForm] = useState({
    nom_scientifique: "",
    description: "",
    taille: "",
    poids: "",
    longevite: "",
    individus: "",
    taxonomie: { ordre: "", famille: "", genre: "" },
    pays: { nom: "", continent: "" },
    auteur: { nom: "", prenom: "" },
    images: [""]
  });

  const handleChange = (path, value) => {
    const keys = path.split(".");
    setForm(prev => {
      const updated = { ...prev };
      let obj = updated;

      for (let i = 0; i < keys.length - 1; i++) {
        obj = obj[keys[i]];
      }

      obj[keys[keys.length - 1]] = value;
      return updated;
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      ...form,
      taille: Number(form.taille),
      poids: Number(form.poids),
      longevite: Number(form.longevite),
      individus: Number(form.individus),
      images: form.images.filter(url => url.trim() !== "")
    };

    const res = await fetch((`${URL_data}/especes`), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    console.log(data);
    alert(data.message);
  };

  return (
    <div className="page">
      <h1>Ajouter une espèce</h1>

      <form className="form-ajout" onSubmit={handleSubmit}>

        <h2>Informations générales</h2>
        <input placeholder="Nom scientifique"
               value={form.nom_scientifique}
               onChange={(e) => handleChange("nom_scientifique", e.target.value)} />

        <textarea placeholder="Description"
                  value={form.description}
                  onChange={(e) => handleChange("description", e.target.value)} />

        <input type="number" placeholder="Taille (cm)"
               value={form.taille}
               onChange={(e) => handleChange("taille", e.target.value)} />

        <input type="number" placeholder="Poids (g)"
               value={form.poids}
               onChange={(e) => handleChange("poids", e.target.value)} />

        <input type="number" placeholder="Longévité (années)"
               value={form.longevite}
               onChange={(e) => handleChange("longevite", e.target.value)} />

        <input type="number" placeholder="Individus restants"
               value={form.individus}
               onChange={(e) => handleChange("individus", e.target.value)} />

        <h2>Taxonomie</h2>
        <input placeholder="Ordre"
               value={form.taxonomie.ordre}
               onChange={(e) => handleChange("taxonomie.ordre", e.target.value)} />

        <input placeholder="Famille"
               value={form.taxonomie.famille}
               onChange={(e) => handleChange("taxonomie.famille", e.target.value)} />

        <input placeholder="Genre"
               value={form.taxonomie.genre}
               onChange={(e) => handleChange("taxonomie.genre", e.target.value)} />

        <h2>Pays</h2>
        <input placeholder="Nom du pays"
               value={form.pays.nom}
               onChange={(e) => handleChange("pays.nom", e.target.value)} />

        <input placeholder="Continent"
               value={form.pays.continent}
               onChange={(e) => handleChange("pays.continent", e.target.value)} />

        <h2>Auteur</h2>
        <input placeholder="Nom"
               value={form.auteur.nom}
               onChange={(e) => handleChange("auteur.nom", e.target.value)} />

        <input placeholder="Prénom"
               value={form.auteur.prenom}
               onChange={(e) => handleChange("auteur.prenom", e.target.value)} />

        <h2>Images</h2>
        <input placeholder="URL image"
               value={form.images[0]}
               onChange={(e) => handleChange("images.0", e.target.value)} />

        <button type="submit">Ajouter</button>
      </form>
    </div>
  );
}

export default PageAjoutEspece;