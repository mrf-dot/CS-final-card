import os
from secrets import *
from colorama import init
from termcolor import cprint
from prettytable import PrettyTable
import cards
from dice import *
"""Used to implement switcher for user functions

"""
init()
name = ''


def help():
    instructions = {
        'help': 'Print the program instructions',
        'clear': 'Clear program output',
        'format': 'Toggles the formatting of the cards',
        'fetch': 'Fetch a card from an ordered deck',
        'random': 'Print a random card',
        'order': 'Print an ordered deck',
        'shuffle': 'Print a shuffled deck',
        'dice': 'Play a game of dice',
    }
    commands = PrettyTable()
    commands.field_names = ['Command', 'Description']
    for x, y in instructions.items():
        commands.add_row([x, y])
    print(commands)


def format():
    """Toggles formatting

    """
    cards.format_cards = not cards.format_cards
    print(f'formatting is {"on" if cards.format_cards else "off"}.')


def clear():
    """Clears the console

    """
    os.system('cls') if os.name == 'nt' else os.system('clear')


def fetch():
    """Returns a card based on it's position in an ordered deck (1-52)

    """
    try:

        fetch_num = int(input('Select a position in the deck (1-52): '))
        if fetch_num in range(1, 53):
            cards.cardify(cards.cards[fetch_num - 1])
        else:
            raise ValueError
    except:
        cprint('Enter a number between one and 52', 'red')
        fetch()


def random():
    """Returns a cryptographically random element in a list
    """
    cards.cardify(choice(cards.cards))


def order():
    """Prints out every element in a list

    """
    for x in cards.cards:
        cards.cardify(x)


def shuffle():
    """Prints out every element in a list in a random order
    """
    shuf_cards = []
    while len(shuf_cards) != len(cards.cards):
        local = choice(cards.cards)
        if local not in shuf_cards:
            shuf_cards.append(local)
    for x in shuf_cards:
        cards.cardify(x)


def dice():
    """Plays a game of dice with an automatic system

    """
    global name
    dice_name = name
    print(preperation_round)
    default_values = PrettyTable(['Player', 'Default value'])
    default_values.add_rows([[name, '$1000'], ['CPU', '$1250']])
    print(default_values)
    player_sum = prep_dice(1000, 'yourself')
    bot_sum = prep_dice(1250, 'the CPU')
    print(main_round)
    results = main_game(dice_name, player_sum, bot_sum)
    recap(results)
