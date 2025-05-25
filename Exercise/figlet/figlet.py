from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
list = figlet.getFonts()

if len(sys.argv) == 3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in list:
        text = input('Input: ')
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit('Invalid usage')

elif len(sys.argv) == 1:
    text = input('Input: ')
    figlet.setFont(font = random.choice(list))

else:
    sys.exit('Invalid usage')

print(figlet.renderText(text))