import React, { useContext, useEffect, useState } from "react";
import "./products.css";
import { NavLink } from "react-router-dom";
import { CounterContext } from "./context/CounterContext";

export default function Products() {
  const axios = require("axios");
  let [prods, setProds] = useState([]);
  let [fullList, setFullList] = useState([]);
  let context = useContext(CounterContext);
  let filtList, filtered, filtBtn;
  filtBtn = document.querySelectorAll(".filt li button");

  useEffect(() => {
    axios
      .get("https://dummyjson.com/products")
      .then(function (response) {
        setFullList(response.data.products);
        setProds(response.data.products);
      })
      .catch(function (error) {
        console.log(error);
      });
  }, []);

  filtered = (e) => {
    let filter = e.target.name;
    filtList = fullList;
    if (!(filter == "all")) {
      filtList = fullList;
      filtList = fullList.filter((product) => product.category == filter);
    }
    filtBtn.forEach((btn) => {
      btn.classList.remove("active");
    });
    setProds(filtList);
    e.target.classList.add("active");
  };

  let [cartList, setCartList] = useState("");
  let dummy = [];
  const inCart = (e) => {
    context.increase();
    dummy.push(e.target.id);
    setCartList([...cartList, e.target.id]);
  };

  useEffect(() => {
    context.getList(cartList);
  }, [cartList]);

  return (
    <div className=" my-5 ">
      <div className="row shadow-lg mt-5">
        <ul className="filt my-5">
          <li>
            <button
              name="all"
              className="text-uppercase filter-btn btn text-sm fw-semibold active"
              onClick={filtered}
            >
              All
            </button>
          </li>
          <li>
            <button
              name="smartphones"
              className="text-uppercase filter-btn btn text-sm fw-semibold"
              onClick={filtered}
            >
              smartphones
            </button>
          </li>
          <li>
            <button
              name="laptops"
              className="text-uppercase filter-btn btn text-sm fw-semibold"
              onClick={filtered}
            >
              laptops
            </button>
          </li>
          <li>
            <button
              name="fragrances"
              className="text-uppercase filter-btn btn text-sm fw-semibold"
              onClick={filtered}
            >
              fragrances
            </button>
          </li>
          <li>
            <button
              name="skincare"
              className="text-uppercase filter-btn btn text-sm fw-semibold"
              onClick={filtered}
            >
              skincare
            </button>
          </li>
          <li>
            <button
              name="groceries"
              className="text-uppercase filter-btn btn text-sm fw-semibold"
              onClick={filtered}
            >
              groceries
            </button>
          </li>
          <li>
            <button
              name="home-decoration"
              className="text-uppercase filter-btn btn text-sm fw-semibold"
              onClick={filtered}
            >
              home-decoration
            </button>
          </li>
        </ul>
      </div>

      <div className="row">
        <div className="d-flex flex-wrap gap-2 justify-content-center shadow-lg p-5">
          {prods.map((product) => {
            return (
              <div
                className="prod p-2 lh-base bg-light position-relative"
                key={product.id}
              >
                <NavLink to={`/home/products/${product.id}`}>
                  <img src={product.thumbnail} className="w-100 mb-3"></img>
                </NavLink>
                <h3>{product.title}</h3>
                <p className="mb-5">{product.description}</p>
                <button
                  id={product.id}
                  onClick={inCart}
                  className="position-absolute bottom-0 translate-middle w-75 "
                >
                  <span>{product.price}$</span>
                </button>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
