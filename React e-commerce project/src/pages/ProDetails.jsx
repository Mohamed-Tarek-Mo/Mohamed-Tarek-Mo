import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ProductSlider from "../components/ProductSlider";
import { CounterContext } from "./../components/context/CounterContext";

export default function ProDetails() {
  let { id } = useParams();
  id = parseInt(id);
  const axios = require("axios");
  let [fullList, setFullList] = useState([]);
  let context = useContext(CounterContext);

  useEffect(() => {
    axios
      .get("https://dummyjson.com/products")
      .then(function (response) {
        setFullList(response.data.products);
      })
      .catch(function (error) {
        console.log(error);
      });
  }, []);

  let product = fullList.find((prod) => prod.id === id);

  return product ? (
    <div>
      <div className="row">
        <div className="col-md-6">
          {
            <ProductSlider
              images={product.images}
              title={product?.title}
            ></ProductSlider>
          }
        </div>

        <div className="col-md-6 p-5 text-start">
          <p className="text-uppercase text-center fs-4 p-3 my-4 bg-dark  text-white">
            {product?.title}
          </p>
          <p className="text-info">{product.description}</p>
          <p className="text-black-50">Brand: {product.brand}</p>
          <p className="text-black-50">Category: {product.category}</p>
          <p className="text-black-50">
            <span className="text-danger">{product.stock}</span> Products left
          </p>
          <p>
            Price: <span className="text-success">{product.price}$</span>
          </p>
          <div className="row justify-content-center">
            <button
              onClick={() => {
                context.increase();
              }}
              className="btn btn-warning w-50 my-5"
            >
              Buy Now
            </button>
          </div>
        </div>
      </div>
      <div className="row p-5">
        <h2 className="mb-5">Description</h2>
        <p>{product.description}</p>
      </div>
    </div>
  ) : (
    <h1 className="my-5 text-danger text-capitalize ">product not found</h1>
  );
}
