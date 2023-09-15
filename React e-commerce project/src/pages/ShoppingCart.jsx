import React, { useContext, useEffect, useState } from "react";
import { CounterContext } from "./../components/context/CounterContext";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

export default function ShoppingCart() {
  const context = useContext(CounterContext);

  let showList;
  showList = context.prodList.map((proId) => {
    parseInt(proId);
    return context.fullList.find((product) => {
      return product.id == proId;
    });
  });
  console.log(context.prodList);
  let [final, setFinal] = useState([]);
  useEffect(() => {
    setFinal(showList);
  }, []);

  function removeObjectWithId(arr, id) {
    const arrCopy = Array.from(arr);

    const objWithIdIndex = arrCopy.findIndex((obj) => obj.id === id);
    arrCopy.splice(objWithIdIndex, 1);
    return arrCopy;
  }

  const deleteItem = (e) => {
    let id = parseInt(e.target.id);
    const dummy = removeObjectWithId(final, id);
    setFinal(dummy);
    context.decrease();
  };

  {
    if (final) {
      return (
        <div className="px-4 pb-4">
          {final.map((item) => {
            return (
              <div key={item.id} className="row h-25 my-4 bg-dark text-white">
                <div className="col-3 px-0">
                  <img className="h-100 w-100" src={item.thumbnail} alt="" />
                </div>
                <div className="col-5 p-4 my-3">
                  <p>{item.title}</p>
                  <p>{item.description}</p>
                </div>
                <div className="col-2 text-success p-5 my-5">
                  <h6 className="text-white d-inline">Price:</h6> {item.price}$
                </div>
                <div className="col-2 text-danger d-flex align-items-center ">
                  <button onClick={deleteItem} className="bg-danger">
                    <h3 id={item.id} className="p-2 px-3 ">
                      Delete <FontAwesomeIcon icon={faTrash} />
                    </h3>
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      );
    } else {
      return (
        <h1 className="my-5 text-danger text-capitalize ">
          Please select some products
        </h1>
      );
    }
  }
}
