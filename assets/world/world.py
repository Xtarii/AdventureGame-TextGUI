"""
Main för världs updateringen,
så här är kort sagt det som skriver ut världen
"""
import styles
from random import randint
# Imports för interact av monster och fiskare
from assets.fisher_men import interact as f_interact
from assets.monsters import interact as m_interact





# World Class
class World():
    """
    Här är classen som kontrollerar världen
    """
    def __init__(self, player, world_x, world_y):
        # Player
        self.player = player

        # Världs prefabs och storlek (chunks)
        self.world_tile = (styles.Colors["BLUE"] + "#")
        self.world_x = world_x
        self.world_y = world_y

        # Världens event rareity, alltså hur rare är ett monster eller en båt
        self.båt_rareity = 3
        self.monster_rareity = 5
        self.max_monster = 3
        # Världs event prefabs och extras
        self.båt = {}
        self.monster = {}



    # Update
    def update(self):
        """
        En enkel world update function/metod

        Den kommer att skapa världen och skriva den i terminalen
        """
        # Får players char och pos
        player_specs = self.player.setPlayer_Character_Settings()
        player_pos = player_specs["pos"]
        # Gör om till användbar data
        self.player_x, self.player_y = player_pos


        # Genererar världens chunk
        world_chunk = ""
        for y in range(self.world_y):
            for x in range(self.world_x):
                # Kollar om pos i render world är lika med player pos
                if x == self.player_x and y == self.player_y:
                    world_chunk += player_specs["char"]
                    continue

                # Annars lägger vi till båtar (en båt) monster eller vatten
                elif self.båt != {} and x == self.båt["pos"][0] and y == self.båt["pos"][1]:
                    # Lägger till båt
                    world_chunk += self.båt["char"]
                    continue

                # Spawnar Monster
                if len(self.monster) != 0:
                    for i in range(len(self.monster)):
                        if x == self.monster[i]["pos"][0] and y == self.monster[i]["pos"][1]:
                            world_chunk += self.monster[i]["char"]
                            break
                    else:
                        world_chunk += self.world_tile
                else:
                    # Lägger till vatten
                    world_chunk += self.world_tile

            # Gör världen till en fyrkant
            world_chunk += "\n"


        # Gör en "print()" för att vissa världen, så typ en render
        print(world_chunk)
        # Kallar på player interact
        self.player_overlap_obj_event_starter()



    # Kollar om player pos == obj pos
    def player_overlap_obj_event_starter(self):
        """
        Denna script kommer också att kolla om players pos är lika
        med pos av båt eller monster
        """
        # Kollar om player pos är på monster pos
        for x in range(len(self.monster)):
            m = self.monster[x]

            if m["pos"][0] == self.player_x and m["pos"][1] == self.player_y:
                # Detta kommer att aktiveras om players pos är lika med något monsters pos
                m_interact.main(self.player)

        # Kollar om player pos är lika med en båts pos
        if self.båt != {} and self.båt["pos"][0] == self.player_x and self.båt["pos"][1] == self.player_y:
            # Detta kommer däremot att aktiveras om player är vid en båt
            f_interact.main(self.player)



    # Spawnar en båt
    def båt_spawner(self):
        """
        Spawnar båtar
        """

        # Settings för x och y
        while True:
            x = randint(1, self.world_x)
            y = randint(1, self.world_y)

            if x != self.player_x and y != self.player_y:
                False
                break


        # Returnar båt eller inte
        if randint(1, self.båt_rareity) == 1:
            self.båt = {
                "char": (styles.Colors["WARNING"] + "#" + styles.Colors["ENDC"]),
                "pos": [x, y]
            }

    # Spawnar monster
    def monster_spawner(self):
        """
        Spawner monster
        """

        self.monster = {}

        # Skapar monster efter max monster
        for i in range(randint(0, self.max_monster)):
            # Settings för x och y
            while True:
                x = randint(1, self.world_x)
                y = randint(1, self.world_y)

                if x != self.player_x and y != self.player_y:
                    False
                    break


            # Skapar monster
            self.monster[i] = {
                "char": (styles.Colors["FAIL"] + "#" + styles.Colors["ENDC"]),
                "pos": [x, y]
            }
