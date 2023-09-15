import React from "react";
import { Carousel } from "react-bootstrap";

export default function ProductSlider(props) {
  const images = props.images;
  const title = props.title;
  let keyCount = 0;

  return (
    <div className="my-5 shadow-lg">
      <Carousel>
        {images.map((image_) => {
          keyCount++;
          return (
            <Carousel.Item key={keyCount}>
              <img className="d-block w-100" src={image_} alt="" />
            </Carousel.Item>
          );
        })}
      </Carousel>
    </div>
  );
}
