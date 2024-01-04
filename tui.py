"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def show_header(header_txt='Disneyland Review Analyser'):
    # SECTION A, TASK 1
    # to show welcome text to user
    print('-' * len(header_txt))
    print(header_txt)
    print('-' * len(header_txt))


def show_main_menu():
    # TASK 3
    # to display main menu options
    prompt = 'Please enter the letter which corresponds with your desired menu choice:'
    menu_choices = [
        ['A', 'View Data'],
        ['B', 'Visualize Data'],
        ['X', 'Exit']
    ]
    _show_menu_opts(prompt, menu_choices)


def _show_menu_opts(prompt_txt, menu_choices):
    print(prompt_txt)
    for choice in menu_choices:
        print(f'    [{choice[0]}] {choice[1]}')
