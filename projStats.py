from variables import *

def getStats(name):
    if name == "SHADOWLASERWALL":
        SIZEX = TILESIZE
        SIZEY = 160*TILESIZE
    elif name == "SHADOWBULLET":
        SIZEX = TILESIZE
        SIZEY = TILESIZE
    elif name == "SEEKER":
        SIZEX = TILESIZE*2
        SIZEY = TILESIZE*2
    return SIZEX, SIZEY