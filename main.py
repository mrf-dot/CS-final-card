from colorama import init
from termcolor import cprint
from getpass import getuser
import commands

init()


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
        try:
            getattr(commands, selection)()
        except BaseException as e:
            print(e)
            cprint(f'\"{selection}\" is not a valid command.', 'red')


if __name__ == '__main__':
    main()
