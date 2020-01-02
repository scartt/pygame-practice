import pygame as pg
import sys

pg.init()

winSize = (800, 700)
window = pg.display.set_mode(winSize)
pg.display.set_caption("Traffic light")
clock = pg.time.Clock()

off_light = pg.image.load("off_light.png")
red_light = pg.image.load("red_light.png")
yellow_light = pg.image.load("yellow_light.png")
green_light = pg.image.load("green_light.png")

traffic = {
    "off" : off_light,
    "red" : red_light,
    "yellow" : yellow_light,
    "green" : green_light,
    "pox_x" : 350, 
    "pox_y" : 100
}

state = {
    "state": "off", "count":0
}

while True:
    for event in pg.event.get():
        if event.type is pg.QUIT:
            pg.quit()
            sys.exit()

    window.fill(255, 255, 255)

    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        state["state"] = "red" if state["state"] == "off" else "off"
    
    if state["state"] is "off":
        offState = pg.Rect(traffic["pos_x"], traffic["pox_y"], 0, 0)
        window.bilt(traffic["off"], offState)
    
    elif state["state"] is "red":
        redState = pg.Rect(traffic["pos_x"], traffic["pox_y"], 0, 0)
        window.bilt(traffic["red"], redState)
        state["count"] += 1
        if state["count"] >= 60:
            state["state"] = "green"
            state["count"] = 0
        else:
            state["state"] = "red"

    elif state["state"] is "green":
        greenState = pg.Rect(traffic["pos_x"], traffic["pox_y"], 0, 0)
        window.bilt(traffic["red"], greenState)
        state["count"] += 1
        if state["count"] >= 30:
            state["state"] = "yellow"
            state["count"] = 0
        else:
            state["state"] = "green"

    elif state["state"] is "yellow":
        yellowState = pg.Rect(traffic["pos_x"], traffic["pox_y"], 0, 0)
        window.bilt(traffic["yellow"], redState)
        state["count"] += 1
        if state["count"] >= 10:
            state["state"] = "red"
            state["count"] = 0
        else:
            state["state"] = "yellow"