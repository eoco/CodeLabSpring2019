window.addEventListener('load', () => {
  const sounds = document.querySelectorAll(".sound");
  const pads = document.querySelectorAll(".pads div");
  const visual = document.querySelector(".visual");
  const colors = ["skyblue", "seagreen", "peru", "thistle", "teal", "orange"];

  pads.forEach((pad, index) => {
    pad.addEventListener("click", function() {
      sounds[index].currentTime = 0;
      sounds[index].play();

      createBubbles(index);
    });
  });

// Create function to make bubble visuals
  const createBubbles = (index) => {
    console.log(`creating bubblw with index # ${index}`);
    const bubble = document.createElement("div");
    visual.appendChild(bubble);
    console.log(`bubble added to visual div: ${bubble}`);
    // bubble.style.backgroundColor = "#ff0000";
    bubble.style.backgroundColor = colors[index];
    bubble.style.animation = "jump 1s ease";
    bubble.addEventListener("animationend", function() {
      visual.removeChild(bubble);
    })

  };

});
