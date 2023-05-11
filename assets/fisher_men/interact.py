"""
Denna scripten kommer att fungera som en interakt när man "interactar" med
fiskebåtar som spawnas random på kartan, men det kommer bara att spawna en
åt gången med en 1/3 att dem faktist spawnar.
"""
import os, styles, random, time



# Detta kallas på om man inte svarar rätt
def fel_svar(player):
    """
    Skådesplar att fiskaren blir arg
    och ireterad
    """

    # Rensar skärmen
    os.system("cls")

    # Text
    print(styles.Colors["FAIL"] + """
Jasså, så du kör bara iväg.
Drar du från alla dina problem?
Det är inte skärskilt trevligt.
Hoppas att alla monster kommer
och tar dig, usch så gräsligt man
kan bete sig mot andra >=(
    """ + styles.Colors["ENDC"])

    # Loadingline, och sen återgår man till spelet
    styles.loadLineDL(sleep=0.3, text="Kastar loss...")



# Funktioner över vad som kan hända
def svar_0(player):
    """
    Svarar på en liten konversation, det är konversation 0
    """

    # Players svar på sjömanens konversation
    print(styles.Colors["GREEN"] + """
<1>    Jag jagar efter monster!!! - så säg
       mig...var kan jag hitta dem?

<2>    Jag är ny här, vad är det du
       pratar om??""" + styles.Colors["ENDC"])

    # Spelar historian typ, alltså tar in player input och sen skickar vi det vidare
    svar = input(styles.Colors["BOLD"] + "> " + styles.Colors["ENDC"])

    # Om svar == 1 då ska sjömanen bli förvirrad
    if svar == "1":
        # Rensar skärmen
        os.system("cls")

        # Historia
        print(styles.Colors["WARNING"] + """
Vad i hela....vill du jaga monster,
jag rekomenderar inte det så jag
tänker inte berätta att dem bor
under vattenet - men jag kan önska
dina farliga drömar lycka till, om
du överlever....då överlever du.
        """ + styles.Colors["ENDC"])

        # Loadingline innan man återgår till spelet
        styles.loadLineDL(sleep=0.3, text="Kastar loss...")

    elif svar == "2":
        # Utför det som ska hända när man trycker på två, så vi börjar med att rensa skärmen
        os.system("cls")

        # Historian
        print(styles.Colors["WARNING"] + """
Sanna mina ord unge, dem här vattnen
är förbannade för evigt. Åk här ifrån
så fort du kan...innan dem kommer...
        """ + styles.Colors["ENDC"])

        # Alternativ
        print(styles.Colors["BLUE"] + """
<1>   Jag kanske borde åka här ifrån.

<2>   Jag tänker stanna.""" + styles.Colors["ENDC"])

        # Svar
        svar = input("> ")


        # Om svar är 1:
        if svar == "1":
            print(styles.Colors["GREEN"] + """
Det var ett bra alternativ, åk
tillbaka till Bahamas du, där du
hör hemma.
            """ + styles.Colors["ENDC"])

            # Åker hem
            styles.loadLineDSE(text="Åker hem... ")

            # Continue Delay
            input(styles.Colors["BLUE"] + "< continue/enter > " + styles.Colors["ENDC"])
            # Rensar skärmen
            os.system("cls")


            # End
            print(styles.Colors["GREEN"] + """
Grattis, du klarade dig helskinad.

Vat inte riktigt om man kan säga
att du van men du klarade dig.
            """ + styles.Colors["ENDC"])
            os.sys.exit(0)

        # Om svar är 2:
        if svar == "2":
            print(styles.Colors["WARNING"] + """
Gör som du vill, jag kan inte
stoppa dig. Men sanna min ord
det här är inte ett ställa för
barn.
            """ + styles.Colors["ENDC"])

        # Fel svar
        else:
            fel_svar(player)

    else:
        # Kallar på fel svar
        fel_svar(player)


# Svar 1 funktion för vad som ska hända om man får 1
def svar_1(player):
    """
    Denna kommer att köras om 1 i convers blir vald
    """

    # Svaret på 1
    print(styles.Colors["BLUE"] + """
Men vad urar jag om, du gör som du
vill. Jag tänker inte stoppa dig.
    """ + styles.Colors["ENDC"])



# Konversationer
convers = {
    0: {
        "txt": styles.Colors["WARNING"] + """
Hej där, vad gör du här ute?...vet du inte
om att haven här är fulla med monster. Dem
tog mitt ben för ett tag sen, det gjorde ont,
men jag överlever.

Var försiktig här ute, man vet inte vad man
stötter på. Om bara haven var som förut
        """ + styles.Colors["ENDC"],

        "exe": svar_0
    },

    1: {
        "txt": styles.Colors["FAIL"] + """
En ung person som dig borde inte vara här uti,
en sjöman kan sjunka till botten på bara några
sekunder.
        """ + styles.Colors["ENDC"],
        "exe": svar_1
    }
}



# Här är start av denna filen när main kallas
def main(player):
    """
    Detta kommer att sluta i en historia
    """

    # Skriver conversationens text
    what = random.randint(0, (len(convers) - 1))
    print(convers[what]["txt"])

    # Kör en delay för att man ska hinna läsa först
    time.sleep(1)

    # Kör funktionen i covers[<number>]["exe"] med player som argument
    convers[what]["exe"](player)

    # En continue funktion
    input(styles.Colors["BLUE"] + "< continue/enter > " + styles.Colors["ENDC"])
    # Rensar skärmen
    os.system("cls")
