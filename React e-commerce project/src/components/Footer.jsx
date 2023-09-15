import React, { Component } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faFacebook,
  faTwitter,
  faLinkedin,
  faGithub,
} from "@fortawesome/free-brands-svg-icons";

export default function Footer() {
  return (
    <div className="mt-5">
      <footer className="bg-dark text-white p-4">
        <div className="row text-start">
          <div className="col-md-4">
            <p>
              Lorem ipsum dolor sit, amet consectetur adipisicing elit.
              Similique asperiores amet illum perferendis quasi blanditiis
              recusandae distinctio doloremque sit, fugit fugiat repellendus
              porro iste nesciunt voluptatum eius alias maxime sunt.
            </p>
          </div>
          <div className="col-md-4">
            <p>
              Lorem ipsum dolor sit, amet consectetur adipisicing elit.
              Similique asperiores amet illum perferendis quasi blanditiis
              recusandae distinctio doloremque sit, fugit fugiat repellendus
              porro iste nesciunt voluptatum eius alias maxime sunt.
            </p>
          </div>
          <div className="col-md-4 text-center">
            <h3>Contact Us</h3>
            <p>
              E-mail: <a href="#"> Example@Example.com</a>
            </p>
            <p>
              <a href="#" className="mx-2">
                <FontAwesomeIcon icon={faFacebook} />
              </a>
              <a href="#" className="mx-2">
                <FontAwesomeIcon icon={faTwitter} />
              </a>
              <a href="#" className="mx-2">
                <FontAwesomeIcon icon={faLinkedin} />
              </a>
              <a href="#" className="mx-2">
                <FontAwesomeIcon icon={faGithub} />
              </a>
            </p>
          </div>
        </div>
        <div className="row">
          <div className="col mt-5">
            all copy rights &copy; reserved to Mohamed Tarek
          </div>
        </div>
      </footer>
    </div>
  );
}
