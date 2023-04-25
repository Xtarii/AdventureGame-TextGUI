"""
Här kommer en gameloop att vara, och alla
andra saker som kommer få spelet att köra


så vi behöver importera några saker,
"""
import time, os
from assets.player import movement
from assets.world import world as w




# Extras
map_x = 14
map_y = 7
delay = 0.1
player = movement.setPlayer()
world = w.World(player, map_x, map_y)

# Sätter movements max x och y till kartans x och y
movement.max_x = map_x
movement.max_y = map_y
# Sätter movements world till world
movement.world = world





# Start
while True:
    # Tar bort allt skräp på skärmen
    os.system("cls")

    # Updaterar player
    player.update()
    # Kallar på World update
    world.update()


    # Time Delay
    time.sleep(delay)
