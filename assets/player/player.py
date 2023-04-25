"""
Här är en simple klass som kommer att
styra spelaren

vi behöver lite importeringar
"""
import styles



# Player class
class Player():
    """
    PLayer class som kontrollerar player
    den börjar med Update som är som main
    för player class
    """
    def __init__(self):
        # Karaktär
        self.player = (styles.Colors["GREEN"] + "#")
        self.x = 5
        self.y = 4

        # Movement
        self.movement_obj = ""

        # Player Health
        self.health = 3



    # Update av player
    def update(self):
        """
        En simple update för player
        """

        # Kallar på player position update
        self.pos(self.movement_obj)

        # Kollar om player health är 0
        if self.health <= 0:
            # Death scene
            pass


    # Kordinater för Player
    def pos(self, obj):
        """
        Här är positionen för player
        """

        # Ställer in obj för update
        if self.movement_obj == "":
            self.movement_obj = obj

        # Kallar på obj för att updatera "x, y" på player
        p_pos = obj(self.x, self.y)

        # Skriver över / Updaterar player position
        self.x = p_pos[0]
        self.y = p_pos[1]



    # En function/metod som återlämnar player som en prefab
    def setPlayer_Character_Settings(self):
        """
        Här återlämnar vi en "dict" på vad player är
        alltså, char och pos för player.

        Om jag har tid så kommer det också att finnas:
        - Inventory
        - Health
        """

        # Player char dict
        player_char = {
            "char": self.player,
            "pos": [self.x, self.y]
        }

        # Återlämnar player_char till den som "kallar på denna functionen"
        return player_char


    # En tar damage function
    def TakeDamage(self, damage: int):
        self.health -= damage
