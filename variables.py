import math

SCREENWIDTH = 1280
SCREENHEIGHT = 720
FPS = 60
SPAWNRATE = 5
TILESIZE = 8
GRAVITY = 0.1
TERMINALVELOCITY = 2

PLAYERSPEED = 3
PLAYERJUMP = 14
MAXJUMPS = 1
PLAYERIFRAMES = 30

weapons = ["SHORTSWORD", "LANCE", "BROADSWORD", "MACE", "WHIP", "BOW"]
projWeapons = ["BOW"]

def getVector(angle):
    angle = angle%360
    if angle <= 180:
        Vx = math.cos(angle)
        Vy = math.sin(angle)
    else:
        angle = 360 - angle
        Vx = -math.cos(angle)
        Vy = math.sin(angle)
    return Vx, Vy