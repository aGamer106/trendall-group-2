import backroundPng from "/src/assets/image 2.png";
import bBlur from "/src/assets/Blur.png";
import Search from "./Search";
import Filters from "./Filters";
import Guide from "./Guide";
import "/src/index.css";

const blurB = () => {
  return (
    <div>
      <img alt="backround" src={backroundPng} className="backroundImg"></img>
      <img alt="backroundLayer" src={bBlur} className="backroungFade"></img>
      <div className="landing-text-container">
        <h1 className="title">Welcome to Beige</h1>
        <h3 className="flavour-text">
          Introducing the all-new Web Based AI supported potted artefact sorter
          created in collaboration with La Trobe University.
        </h3>
        <h3 className="flavour-text">
          If you’re new or need a reminder, explore the “Filter Guide” below.
        </h3>
        <Search></Search>
        <div className="button-container">
          <Filters></Filters>
          <Guide></Guide>
        </div>
      </div>
    </div>
  );
};

export default blurB;
