import { URL_data } from "../config";
import { useEffect, useState } from "react";
import "../App.css";

export default function PageTableau() {
  const [especes, setEspeces] = useState([]);
  const [sortBy, setSortBy] = useState(null);

  useEffect(() => {
    fetch(`${URL_data}/especes`)   // ← correspond à TA route Flask
      .then((res) => res.json())
      .then((data) => setEspeces(data))
      .catch((err) => console.error("Erreur API :", err));
  }, []);

let sortedEspeces = [...especes];

if (sortBy) {
  sortedEspeces.sort((a, b) => {
    let A, B;

    // Champs simples
    if (["taille", "poids", "longevite", "individus"].includes(sortBy)) {
      A = a[sortBy];
      B = b[sortBy];
    }
    // Champs taxonomie
    if (["famille", "genre", "ordre"].includes(sortBy)) {
      A = a.taxonomie[sortBy];
      B = b.taxonomie[sortBy];
    }
    // Tri numérique
    if (typeof A === "number" && typeof B === "number") {
      return B - A; // du plus grand au plus petit
    }
    // Tri texte
    return A.localeCompare(B);
  });
}

  return (
    <div className="page-tableau">
      <h1>Tableau des espèces</h1>

        <div className="select-container">
        <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
          <option value="">Default</option>
          <option value="taille">Taille</option>
          <option value="poids">Poids</option>
          <option value="longevite">Longévité</option>
          <option value="individus">Individus</option>
          <option value="famille">Famille</option>
          <option value="genre">Genre</option>
        </select>
      </div>

      <table className="table-especes">
        <thead>
          <tr>
            <th>Nom scientifique</th>
            <th>Description</th>
            <th>Taille</th>
            <th>Poids</th>
            <th>Longévité</th>
            <th>Individus</th>
            <th>Taxonomie</th>
            <th>Pays</th>
          </tr>
        </thead>

        <tbody>
          {sortedEspeces.map((e) => (
            <tr key={e.id}>
              <td>{e.nom_scientifique}</td>
              <td>{e.description}</td>
              <td>{e.taille} cm</td>
              <td>{e.poids} kg</td>
              <td>{e.longevite} ans</td>
              <td>{e.individus.toLocaleString()}</td>

              <td>
                {e.taxonomie.famille} ({e.taxonomie.genre})
                <br />
                <small>{e.taxonomie.ordre}</small>
              </td>

              <td>
                {e.pays.nom}
                <br />
                <small>{e.pays.continent}</small>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}