import React, { useContext } from "react";
import { Container, Navbar, Nav } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faStore, faCartShopping } from "@fortawesome/free-solid-svg-icons";
import { CounterContext } from "./context/CounterContext";

export default function NavBar() {
  let context = useContext(CounterContext);
  return (
    <Navbar bg="light" expand="lg" className="sticky-top shadow">
      <Container>
        <Navbar.Brand href="#home">
          <NavLink className="nav-link" to="Home">
            <FontAwesomeIcon icon={faStore} className="me-2"></FontAwesomeIcon>
            Ecommerce
          </NavLink>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            <NavLink className="nav-link" to="cart">
              <FontAwesomeIcon icon={faCartShopping} /> {context.count}
            </NavLink>
            <NavLink className="nav-link" to="Home">
              Home
            </NavLink>
            <NavLink className="nav-link" to="About">
              About
            </NavLink>
            <NavLink className="nav-link" to="Contact">
              Contact us
            </NavLink>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
