import { useEffect, useState } from "react";
import { URL_data } from "../config";

function PageAjoutImage() {
  const [especes, setEspeces] = useState([]);
  const [selectedId, setSelectedId] = useState("");
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${URL_data}/especes`)
      .then(res => res.json())
      .then(data => {
        setEspeces(data);
        console.log("ESPECES :", data);
        setLoading(false);
      });
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!selectedId || !url.trim()) {
      alert("Veuillez sélectionner une espèce et entrer une URL.");
      return;
    }

    const payload = { url };

    const res = await fetch(`${URL_data}/especes/${selectedId}/images`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    alert(data.message || "Image ajoutée !");
    setUrl("");
  };

  return (
    <div className="page">
      <h1>Ajouter une image</h1>

      <form className="form-ajout" onSubmit={handleSubmit}>

        <label>Choisir une espèce :</label>

        {loading ? (
          <p>Chargement des espèces...</p>
        ) : (
          <select
            value={selectedId}
            onChange={(e) => setSelectedId(Number(e.target.value))}
          >
            <option value="">-- Sélectionner --</option>
            {especes.map((e) => (
              <option key={e.id} value={e.id}>
                {e.nom_scientifique}
              </option>
            ))}
          </select>
        )}

        <label>URL de l'image :</label>
        <input
          type="text"
          placeholder="https://..."
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />

        <button type="submit">Ajouter l'image</button>
      </form>
    </div>
  );
}

export default PageAjoutImage;