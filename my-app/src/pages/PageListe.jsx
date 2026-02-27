import { useEffect, useState } from "react";
import { URL_data } from "../config";
import { Link } from "react-router-dom";
import "../App.css";

function PageListe() {
  const [especes, setEspeces] = useState([]);

  useEffect(() => {
    fetch(`${URL_data}/especes`)
      .then(res => res.json())
      .then(data => setEspeces(data))
      .catch(err => console.error("Erreur API :", err));
  }, []);

  return (
    <div className="page">
      <h1>Oiseaux</h1>

      <div className="flex-container">
        {especes.map(e => (
          <div className="card" key={e.id}>
            <img src={e.images[0]} alt={e.nom_scientifique} />
            <h2>{e.nom_scientifique}</h2>
            <p>{e.description}</p>

            {/* Lien vers la page détail */}
            <Link to={`/espece/${e.id}`} className="btn">
              Voir la fiche
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default PageListe;