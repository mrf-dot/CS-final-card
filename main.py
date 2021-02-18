from termcolor import cprint
from getpass import getuser
import commands

def changeName():
    changeName = input('What would you like me to call you?: ')
    commands.name = changeName if changeName else getuser()


def main():
    """Initiates the program

    """
    commands.clear()
    changeName()
    commands.clear()
    commands.help()
    while True:
        selection = input('Select an option: ').lower()
        default = lambda: cprint(f'\"{selection}\" is not a valid command.', 'red')
        getattr(commands, selection, lambda: default())()


if __name__ == '__main__':
    main()
