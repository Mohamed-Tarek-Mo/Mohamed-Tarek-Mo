import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faEnvelope,
  faPhone,
  faLocationDot,
  faUser,
  faTag,
} from "@fortawesome/free-solid-svg-icons";

export default function Contact() {
  let [values, setValues] = useState({
    username: "",
  });
  let [errors, setErrors] = useState({
    username: "",
  });
  const setter = (e) => {
    setValues({
      ...values,
      [e.target.name]: e.target.value,
    });
  };
  let validate = (e) => {
    if (values.username.length < 3) {
      e.preventDefault();
      setErrors({
        ...errors,
        username: "Name must contain at least 3 characers",
      });
    } else {
      setErrors({
        username: "",
      });
    }
  };

  return (
    <div>
      <div className="row my-5 shadow-lg bg-light p-4">
        <div className="col-lg-5 my-5 p-4  ">
          <form
            onSubmit={validate}
            className="text-center align-items-center justify-content-center"
          >
            <div className="col-12 mb-5 pb-2 justify-content-center text-center text-success">
              <h3>
                <FontAwesomeIcon icon={faEnvelope} /> Contact us
              </h3>
            </div>

            <div className="p-2 mb-3 justify-content-center">
              <FontAwesomeIcon icon={faUser} className="me-3" />
              <input
                type="text"
                placeholder="Enter Your Name"
                className="col-10"
                name="username"
                onChange={setter}
                defaultValue={values.username}
                required
              />
              {errors.username && (
                <p className="text-danger">{errors.username}</p>
              )}
            </div>

            <div className="p-2 mb-3 justify-content-center">
              <FontAwesomeIcon icon={faEnvelope} className="me-3" />
              <input
                type="email"
                placeholder="Enter Your Email"
                className="col-10"
                required
              />
            </div>

            <div className="p-2 mb-3 justify-content-center">
              <FontAwesomeIcon icon={faTag} className="me-3" />
              <input
                type="text"
                placeholder="Enter The Subject"
                className="col-10 mb-3"
                required
              />
            </div>

            <div className="p-2 justify-content-center">
              <textarea
                className="col-10 w-100 mb-3"
                placeholder="Enter A Message"
                required
              ></textarea>
            </div>

            <div className="p-2 justify-content-center">
              <input
                type="submit"
                className="btn btn-primary w-50"
                value="Send Message"
              />
            </div>
          </form>
        </div>

        <div className="col-lg-7">
          <div className="w-100 h-75">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6052.237853447414!2d-73.9472660737277!3d40.6713484974526!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25b83e7660d3b%3A0x6c922b10d99212ac!2sCrown%20Heights%2C%20Brooklyn%2C%20NY%2C%20USA!5e0!3m2!1sen!2seg!4v1663787950281!5m2!1sen!2seg"
              frameborder="0"
              allowfullscreen=""
              className="w-100 h-100"
            ></iframe>
          </div>

          <br />

          <div className="row text-center">
            <div className="col-md-4">
              <a className="btn">
                <FontAwesomeIcon icon={faLocationDot} />
              </a>
              <p>Binghamton, New York</p>
              <p>4343 Hinkle Deegan Lake Road</p>
            </div>

            <div className="col-md-4">
              <a className="btn">
                <FontAwesomeIcon icon={faPhone} />
              </a>
              <p>00 (958) 9865 562</p>
              <p>Mon to Fri 9am to 6 pm</p>
            </div>

            <div className="col-md-4">
              <a className="btn">
                <FontAwesomeIcon icon={faEnvelope} />
              </a>
              <p>support@colorlib.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
