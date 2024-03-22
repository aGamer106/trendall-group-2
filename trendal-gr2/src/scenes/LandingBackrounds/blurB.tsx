import backroundPng from "/src/assets/image 2.png";
import bBlur from "/src/assets/Blur.png";
import "/src/scenes/LandingBackrounds/backround.css";

const blurB = () => {
  return (
    <div>
      <img alt="backround" src={backroundPng} className="image1"></img>
      <img alt="backroundLayer" src={bBlur} className="image2"></img>
    </div>
  );
};

export default blurB;
