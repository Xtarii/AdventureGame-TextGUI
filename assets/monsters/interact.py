"""
Här är scripten som kommer att fungera som en interact event om man
"interactar" med monster
"""
import os, styles




# Start av filen när main kallas
def main(player):
    """
    Interaction med monster, det kommer att sluta i en fight


    Så i denna kommer att köra en battle
    """

    # Story telling
    print(styles.Colors["FAIL"] + """
Jag använde mitt fiskespö.
Men det stora monster verkade
inte bry sig, trots allt - det
monsteret såg ut att ha hud av
pansar eller något annat super
hårt material.


Så jag startade min båt och slydde
    """ + styles.Colors["ENDC"])


    # Delay
    input(styles.Colors["BLUE"] + "< continue/enter > " + styles.Colors["ENDC"])
