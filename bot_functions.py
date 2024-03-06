import random

def print_help_message():
    return """
    **BOTEN ROSIE**\nJag är bortsprugna vovven Rosie. Här är några kommandon jag förstår:```
!help - Skriver ut det här meddelandet
!voff - Voffar tillbaka```
    """

def print_voff_message():
    list = ["Voff!", "Voff Voff!", "Vore gott med en bira, VOFF!", "VOFFIIIII!", "voffvoffvoff",
            ">:( Voff! (Översättning: Jag är grining)", "VOVVVVVVOO", ":D Voff! (Översättning: Jag är glad)", ":/ Voff... (Översättning: Jag är lite osäker)"]
    return list[random.randint(0, len(list)-1)]