"""
Här är en keylogger som kommer att samla all
input och skicka vidare till player


här under är importeringar, keyboard är för
spelets keylogger
"""
import keyboard
from assets.player import player as p




# Extras:
world = ""  # För att kontrollera world evetns
player = p.Player()
max_x = 7   # Defalut för att ta bort möjliga buggar
max_y = 7   # Defalut för att ta bort möjliga buggar





# Player Movement
@player.pos
def p_movement(x, y):
    """
    Enkel movement på vart player rör sig
    """

    # Kollar om en keyboard key var nedtryckt och om player går utanför kartan
    if keyboard.is_pressed("w"):
        if y < 1:
            y = (max_y -1)

            # spawnar en båt och monster
            world.båt_spawner()
            world.monster_spawner()
        else:
            y -= 1
    if keyboard.is_pressed("s"):
        if y > (max_y -1):
            y = 0

            # spawnar en båt och monster
            world.båt_spawner()
            world.monster_spawner()
        else:
            y += 1

    if keyboard.is_pressed("a"):
        if x < 1:
            x = (max_x -1)

            # spawnar en båt och monster
            world.båt_spawner()
            world.monster_spawner()
        else:
            x -= 1
    if keyboard.is_pressed("d"):
        if x > (max_x -1):
            x = 0

            # spawnar en båt och monster
            world.båt_spawner()
            world.monster_spawner()
        else:
            x += 1


    # Återlämnar kordinaterna i en lista
    return [x, y]





# Återlämnar player
def setPlayer():
    return player
