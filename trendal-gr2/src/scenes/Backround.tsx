import backroundPng from "/src/assets/image 2.png";
import bBlur from "/src/assets/Blur.png";
import "/src/index.css";

const blurB = () => {
  return (
    <div>
      <img alt="backround" src={backroundPng} className="backroundImg"></img>
      <img alt="backroundLayer" src={bBlur} className="backroungFade"></img>
    </div>
  );
};

export default blurB;
