from p5 import *
import time
import math as np
from open_csv import open_csv
t=1
started=0


def setup():
    size(400, 750)
    no_stroke()
    background(0)


lines = open_csv(file="../../sample_data/samples2.csv")
last_size = 1
last_pos = ((lines[1][1]*1000+lines[1][0])%width, (lines[1][2]*1000+lines[1][0])%height)
curr_pos = last_pos

def draw():
    global t
    global last_pos
    global curr_pos
    if t==1:
        background(30,20,30)
    print(started)
    r=lines[t][-1]*10+120
    g=(lines[t][-1]*25)
    b=(lines[t][-1]*10)
    if r > 255:
        r=255
    if g > 255:
        g=255
    if g < 100:
        g=0
    if b > 255:
        b=255
    
    fill(r, g, b, 140)
    circle_size = round(lines[t][-1]/3+1)
    curr_pos = (round(t*width/2/len(lines)*np.sin(t/4)+width/2), round(t*width/2/len(lines)*np.cos(t/4)+height/2))
    if started==1:
        t+=1
        circle(curr_pos[0], curr_pos[1], circle_size*10)
    last_pos = curr_pos
def mouse_pressed(event):
    global started
    started=1
run()