from pyfiglet import Figlet
import sys
import random
custom_fig = Figlet()
fonts = custom_fig.getFonts()


if len(sys.argv) == 1:
    entrada = input("Input: ")
    f = Figlet(font = random.choice(fonts))
    print(f.renderText(entrada))
else:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        entrada = input("Input: ")
        f = Figlet(font = sys.argv[2])
        print(f.renderText(entrada))