import React from "react";
import profile_picture from "./github_profile_picture.jpg";

export const InfoCard = () => {
  return (
    <div
      style={{
        animation: "slidein 3s",
        position: "fixed",
        backgroundColor: "mintcream",
        display: "flex",
        alignItems: "center",
        right: "0",
        top: "9%",
        zIndex: "1",
        maxWidth: "100%",
        maxHeight: "fit-content",
        border: "1px solid whitesmoke",
      }}>
      <div
        style={{
          maxWidth: "50%",
          display: "flex",
          flexWrap: "wrap",
          margin: "0 20px 0 20px",
          color: "black",
          border: "2px dashed black",
        }}>
        <span style={{ padding: "0 20px"}}>Nick Bierman</span>
      </div>
      <div style={{color: "black"}}>
        <p>
          Software Engineer and stathead passionate about the intersection of
          sports & tech.
        </p>
        <p>
          I love using data visualization to dive under the hood of player
          performance.
        </p>
        <div
          style={{
            display: "flex",
            maxWidth: "90%",
            maxHeight: "fit-content",
            justifyContent: "space-around",
            fontSize: "30px"
          }}>
          <a href="https://github.com/nicholasbierman">
            <i class="devicon-github-original"></i>
          </a>
          <a href="https://www.linkedin.com/in/nicholas-bierman-950970105/">
            <i class="devicon-linkedin-plain"></i>
          </a>
        </div>
      </div>
    </div>
  );
};
