function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(100*pAccelerationX, 100*pAccelerationY, 100*pAccelerationZ);
  fill = (255);
  ellipse(width/2 + int(100*sin(millis()/400)), height/2 + int(100*cos(millis()/400)), 25, 25);
}