import React, { useEffect, useState } from "react";
import { CounterContext } from "./CounterContext";

export default function CounterProvider(props) {
  let [count, setCount] = useState(0);
  let [prodList, setProdList] = useState([]);

  const axios = require("axios");
  let [fullList, setFullList] = useState([]);

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

  let increase = () => {
    setCount(count + 1);
  };
  let decrease = () => {
    if (count) setCount(count - 1);
  };
  let getList = (arr) => {
    setProdList(arr);
  };

  let counter = {
    count,
    increase,
    decrease,
    prodList,
    getList,
    fullList,
  };
  return (
    <CounterContext.Provider value={counter}>
      {props.children}
    </CounterContext.Provider>
  );
}
