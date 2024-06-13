def getStats(name):
    if name == "ZOMBIE":
        HEALTH = 80
        AITYPE = "ZOMBIE"
        SIZEX = 4
        SIZEY = 6
    elif name == "TROLL":
        HEALTH = 600
        AITYPE = "ZOMBIE"
        SIZEX = 12
        SIZEY = 12
    elif name == "TROLL_BULKY":
        HEALTH = 2500
        AITYPE = "ZOMBIE"
        SIZEX = 16
        SIZEY = 16
    elif name == "SLIME_GREEN":
        HEALTH = 29
        AITYPE = "SLIME"
        SIZEX = 4
        SIZEY = 4
    elif name == "SLIME_BLUE":
        HEALTH = 56
        AITYPE = "SLIME"
        SIZEX = 4
        SIZEY = 4
    elif name == "SLIME_PURPLE":
        HEALTH = 120
        AITYPE = "SLIME"
        SIZEX = 8
        SIZEY = 8
    elif name == "SLIME_RED":
        HEALTH = 220
        AITYPE = "SLIME"
        SIZEX = 4
        SIZEY = 4
    elif name == "BOSS_KINGSLIME":
        HEALTH = 5600
        AITYPE = "BOSS_KINGSLIME"
        SIZEX = 16
        SIZEY = 16
    elif name == "BOSS_SHADOWGUARDIAN":
        HEALTH = 8600
        AITYPE = "BOSS_SHADOWGUARDIAN"
        SIZEX = 16
        SIZEY = 16
    elif name == "SHADOWSTARSUMMON":
        HEALTH = 1 # Auto killed when scene switches from boss
        AITYPE = "SHADOWSTARSUMMON"
        SIZEX = 3
        SIZEY = 3
    elif name == "BOSS_GODSEEKER":
        HEALTH = 11000
        AITYPE = "BOSS_GODSEEKER"
        SIZEX = 8
        SIZEY = 8
    return HEALTH, AITYPE, SIZEX, SIZEY