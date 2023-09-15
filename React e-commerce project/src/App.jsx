import "./App.css";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";
import { Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import ProDetails from "./pages/ProDetails";
import ErrorPage from "./pages/ErrorPage";
import ShoppingCart from "./pages/ShoppingCart";

function App() {
  return (
    <div className="App bgGradient">
      <NavBar></NavBar>
      <div className="container bg-white pt-3">
        <Routes>
          <Route path="/" element={<Navigate to={"/home"} />}></Route>
          <Route path="/home" element={<Home />}></Route>
          <Route path="/about" element={<About />}></Route>
          <Route path="/contact" element={<Contact />}></Route>
          <Route path="/cart" element={<ShoppingCart />}></Route>
          <Route path="/home/products/:id" element={<ProDetails />} />
          <Route path="*" element={<ErrorPage />} />
        </Routes>
      </div>
      <Footer></Footer>
    </div>
  );
}

export default App;
