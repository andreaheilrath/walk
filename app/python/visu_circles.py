from p5 import *
import time
from open_csv import open_csv

t=1



def setup():
    size(640, 360)
    no_stroke()
    background(204)

lines = open_csv()
last_size = 1
last_pos = ((lines[1][1]*1000+lines[1][0])%width, (lines[1][2]*1000+lines[1][0])%height)
curr_pos = last_pos

def draw():
    global t
    global last_pos
    global curr_pos
    t+=1
    fill((lines[t][1]*500)%255, (lines[t][2]*1010)%255, (lines[t][3]*1010)%255, 127)


    circle_size = round(last_size - lines[t][-1])
    curr_pos = (lines[t][1]*1000+lines[t][0]%width, (lines[t][2]*1000+lines[t][0])%height)
    circle(abs(last_pos[0]-curr_pos[0]), abs(last_pos[1]-curr_pos[1]), circle_size*10)
    last_pos = curr_pos

def key_pressed(event):
    background(204)

run()