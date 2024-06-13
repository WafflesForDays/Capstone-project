import math

def getWeapon(name):
    if name == "SHORTSWORD":
        ATKFRAMES = 7
        ATKCOOL = 4
        LOCALIFRAMES = 1
        HITBOX_X, HITBOX_Y = 3, 1
        OFFSET_X, OFFSET_Y = 3, 1
        VELOCITY_X, VELOCITY_Y = 0, 0
        DMG = 30
    elif name == "LANCE":
        ATKFRAMES = 24
        ATKCOOL = 10
        LOCALIFRAMES = 6
        HITBOX_X, HITBOX_Y = 7, 1
        OFFSET_X, OFFSET_Y = 7, 1
        VELOCITY_X, VELOCITY_Y = 0, 0
        DMG = 22
    elif name == "BROADSWORD":
        ATKFRAMES = 10
        ATKCOOL = 5
        LOCALIFRAMES = 10
        HITBOX_X, HITBOX_Y = 3, 4
        OFFSET_X, OFFSET_Y = 3, -1
        VELOCITY_X, VELOCITY_Y = 0, 0
        DMG = 32
    elif name == "MACE":
        ATKFRAMES = 10
        ATKCOOL = 40
        LOCALIFRAMES = 10
        HITBOX_X, HITBOX_Y = 5, 4
        OFFSET_X, OFFSET_Y = 4, -1
        VELOCITY_X, VELOCITY_Y = 0, 0
        DMG = 120
    elif name == "WHIP":
        ATKFRAMES = 6
        ATKCOOL = 3
        LOCALIFRAMES = 4
        HITBOX_X, HITBOX_Y = 15, 3
        OFFSET_X, OFFSET_Y = 15, 0
        VELOCITY_X, VELOCITY_Y = 0, 0
        DMG = 9
    elif name == "BOW":
        ATKFRAMES = 1
        ATKCOOL = 8
        LOCALIFRAMES = 2
        HITBOX_X, HITBOX_Y = 2, 2
        OFFSET_X, OFFSET_Y = 0, 0
        VELOCITY_X, VELOCITY_Y = 2, -3
        DMG = 5
    return ATKFRAMES, ATKCOOL, LOCALIFRAMES, HITBOX_X, HITBOX_Y, OFFSET_X, OFFSET_Y, DMG, VELOCITY_X, VELOCITY_Y