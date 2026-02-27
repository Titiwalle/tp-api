import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import PageAjoutEspece from "./pages/PageAjoutEspece";
import PageListe from "./pages/PageListe";
import PageDetail from "./pages/PageDetail";
import PageTableau from "./pages/PageTableau";
import PageAjoutImage from "./pages/PageAjoutImage";
import "./App.css";

function App() {
  return (
    <BrowserRouter>

      {/* Bandeau fixe */}
      <header className="navbar">
        <nav>
          <Link to="/">Liste</Link>
          <Link to="/tableau">Tableau</Link>
          <Link to="/ajout">Ajouter une espèce</Link>
          <Link to="/image">Ajouter une image</Link>
          {/* <Link to="/espece/:id">Détail</Link> */}
        </nav>
      </header>

      {/* Contenu des pages */}
      <main className="content">
        <Routes>
          <Route path="/" element={<PageListe />} />
          <Route path="/ajout" element={<PageAjoutEspece />} />
          {/* <Route path="/espece/:id" element={<PageDetail />} /> */}
          <Route path="/tableau" element={<PageTableau />} />
          <Route path="/image" element={<PageAjoutImage />} />
        </Routes>
      </main>

    </BrowserRouter>
  );
}

export default App;