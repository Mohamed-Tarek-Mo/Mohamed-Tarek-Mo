import React from "react";
import ProgressBar from "react-bootstrap/ProgressBar";

export default function About() {
  return (
    <div className="my-5 shadow-lg p-5">
      <div className="row align-items-center gx-md-5 gy-4 gy-md-0">
        <div className="col-md-6">
          <section>
            <img
              src="https://giovannicosmetics.com/wp-content/uploads/2020/04/For-Men.jpg"
              alt="about-me"
            />
          </section>
        </div>
        <div className="col-md-6 text-start text-warning">
          <section className="vstack gap-2">
            <h3 className="text-uppercase fst-italic fw-normal">about me</h3>
            <h2 className="text-uppercase fw-bolder ">personal details</h2>
            <p className="text-black">
              Here, I focus on a range of items and features that we use in life
              without giving them a second thought. such as Coca Cola. Dolor sit
              amet, consectetur adipisicing elit, sed do eiusmod tempor
              incididunt ut labore et dolore magna aliqua. Ut enim ad minim
              veniam, quis nostrud exercitation ullamco.
            </p>
          </section>
        </div>
      </div>

      <div className="row bg-light my-5">
        <div className="col-md-6 p-5 text-start text-black-50">
          It won’t be a bigger problem to find one video game lover in your
          neighbor. Since the introduction of Virtual Game, it has been
          achieving great heights so far as its popularity and technological
          advancement are concerned. The history of video game is as interesting
          as a fairy tale.
        </div>
        <div className="col-md-6 p-5 text-start text-black-50">
          The quality of today’s video game was not at all there when video game
          first conceptualized and played ever. During the formulative years,
          video games were created by using various interactive electronic
          devices with various display formats. The first ever video game was
          designed in 1947 by Thomas T. Goldsmith Jr.
        </div>
      </div>

      <div className="row">
        <div className="col-12 text-start mb-4 mt-5">
          <h4>Tools Expertness</h4>
        </div>
        <div className="col-md-6 my-3 text-start">
          <h5>HTML</h5>
          <ProgressBar now={95} label={`95%`} />
        </div>
        <div className="col-md-6 my-3 text-start">
          <h5>CSS</h5>
          <ProgressBar now={85} label={`85%`} />
        </div>
        <div className="col-md-6 my-3 text-start">
          <h5>JavaScript</h5>
          <ProgressBar now={70} label={`70%`} />
        </div>
        <div className="col-md-6 my-3 text-start">
          <h5>React</h5>
          <ProgressBar now={70} label={`70%`} />
        </div>
        <div className="col-md-6 my-3 text-start">
          <h5>Design</h5>
          <ProgressBar now={50} label={`50%`} />
        </div>
      </div>
    </div>
  );
}
