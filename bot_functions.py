import random
from datetime import datetime

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

def print_rep_message():
    return """**Rosies Rep-planerare** <:krille:1214953899497099264>
Vill du: 
**1.** Kolla när alla kioskmongon kan repa?
**2.** Boka in ett rep?"""

def check_availability():
    now = datetime.now()
    _, week, _ = now.isocalendar()
    return "@everyone Vilka dagar kan alla repa/ses nästa vecka? Vecka " + str(week+1)
    