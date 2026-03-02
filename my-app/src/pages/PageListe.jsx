import { useEffect, useState } from "react";
import { URL_data } from "../config";
import "../App.css";

function PageListe() {
  const [especes, setEspeces] = useState([]);
  const [indexes, setIndexes] = useState([]);

  useEffect(() => {
    fetch(`${URL_data}/especes`)
      .then(res => res.json())
      .then(data => {
        setEspeces(data);
        setIndexes(new Array(data.length).fill(0)); 
      })
      .catch(err => console.error("Erreur API :", err));
  }, []);

  // Carrousel automatique
  useEffect(() => {
    if (especes.length === 0) return;

    const interval = setInterval(() => {
      setIndexes(prev =>
        prev.map((i, idx) =>
          especes[idx].images.length > 1
            ? (i + 1) % especes[idx].images.length
            : 0
        )
      );
    }, 2000);

    return () => clearInterval(interval);
  }, [especes]);

  return (
    <div className="page">
      <h1>Oiseaux</h1>

      <div className="flex-container">
        {especes.map((e, idx) => (
          <div className="card" key={e.id}>
            <img
              src={e.images[indexes[idx]]}
              alt={e.nom_scientifique}
            />

            <div className="info">
              <h2>{e.nom_scientifique}</h2>
              <p className="desc">{e.description}</p>

              <div className="details">
                <p><strong>Taille :</strong> {e.taille} cm</p>
                <p><strong>Poids :</strong> {e.poids} g</p>
                <p><strong>Longévité :</strong> {e.longevite} ans</p>
                <p><strong>Population :</strong> {e.individus}</p>

                <p><strong>Taxonomie :</strong> {e.taxonomie.ordre}, {e.taxonomie.famille}, {e.taxonomie.genre}</p>

                <p><strong>Pays :</strong> {e.pays.nom} ({e.pays.continent})</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PageListe;