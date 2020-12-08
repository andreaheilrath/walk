export const clock = (p) => {
  let cx, cy;
  let secondsRadius;
  let minutesRadius;
  let hoursRadius;
  let clockDiameter;

  p.setup = () => {
    p.createCanvas(400, 400);

  };


  p.draw = () => {
    // Draw the clock background
    p.background(100*p.pAccelerationX, 100*p.pAccelerationY, 100*p.pAccelerationZ);
    p.fill = (255);
    p.ellipse(p.width/2 + p.int(100*p.sin(p.millis()/400)), p.height/2 + p.int(100*p.cos(p.millis()/400)), 25, 25);

  };
};
