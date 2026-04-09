from cart.cart import *
from roller.roller import *

while True:
    cmd = input("Input command: ")
    if 'exit' in cmd.lower():
        ext = str(input("Data may be lost if you exit without saving, would you like to save before exiting? (y/n): "))
        if 'n' in ext:
            break
        elif 'y' in ext:
            commandParseCart('save')
            break
        else:
            print('Not a valid response, please try again')
    elif 'help' in cmd.lower():
        f = open("help.txt", "r")
        print(f.read())
        f.close()
    elif 'roll' in cmd.lower():
        commandParseRoller(cmd)
    else:
        commandParseCart(cmd)