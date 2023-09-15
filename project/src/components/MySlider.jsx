import React from "react-bootstrap/Carousel";
import { Carousel } from "react-bootstrap";
import "./MySlider.css";

export default function MySlider() {
  return (
    <div className="mt-5 shadow-lg">
      <Carousel>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://gadgets-africa.com/wp-content/uploads/2020/05/1_BGkB9VOJrhNPGuJDia8vgQ.jpeg"
            alt="First slide"
          />
          <Carousel.Caption>
            <h2>Smartphones</h2>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://api.time.com/wp-content/uploads/2017/05/laptops.jpg"
            alt="Second slide"
          />

          <Carousel.Caption>
            <h2>Laptops</h2>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/fragrances-lead-1620855440.jpg?crop=1.00xw:0.502xh;0,0&resize=1200:*"
            alt="Third slide"
          />

          <Carousel.Caption>
            <h2>Fragrances</h2>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://images.everydayhealth.com/images/what-are-natural-skin-care-products-alt-1440x810.jpg"
            alt="Fourth slide"
          />
          <Carousel.Caption>
            <h2>Skincare</h2>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://midwestcommunity.org/wp-content/uploads/2018/02/Groceries-ThinkstockPhotos-836782690.jpg"
            alt="Fifth slide"
          />

          <Carousel.Caption>
            <h2>Groceries</h2>
          </Carousel.Caption>
        </Carousel.Item>

        <Carousel.Item>
          <img
            className="d-block w-100"
            src="https://www.nawy.com/blog/wp-content/uploads/2022/06/Home-Decor.jpg"
            alt="Sixth slide"
          />

          <Carousel.Caption>
            <h2>Home Decoration</h2>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </div>
  );
}
