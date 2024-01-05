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
    menu_choices = ['View Data', 'Visualize Data']
    _print_menu_opts(prompt, menu_choices, True)

    # TASK 4
    # to confirm user input
    user_choice = input('')
    sel_opt = _get_sel_opt(user_choice, menu_choices, True)  # gets option user selected

    while sel_opt is None:
        # if user entered an invalid input
        user_choice = input('Please choose a valid option from menu!\n')
        sel_opt = _get_sel_opt(user_choice, menu_choices, True)

    # if user input is valid
    print(f'You have chosen option {sel_opt[0]} - {sel_opt[1]}')

    if sel_opt[0] == 'X':
        quit()


# region HELPER FUNCTIONS
# these functions abstract away repetitive code to make project cleaner
def _print_menu_opts(prompt_txt, menu_choices, show_exit_opt=False):
    # prints out prompt to select a menu option then prints out menu options
    cur_index = 0
    print(prompt_txt)
    for choice in menu_choices:
        print(f'    [{chr(ord("A") + cur_index)}] {choice}')
        cur_index += 1

    if show_exit_opt:
        # to give user menu option to exit
        print(f'    [X] Exit')


def _get_sel_opt(user_input, menu_choices, use_exit_opt=False):
    # gets selected option
    # returns the details of the option user selected if it matches any option provided
    # returns an array of nones if opt is invalid

    cur_index = 0
    for c in menu_choices:
        if user_input.lower() == chr(ord('a') + cur_index):
            return chr(ord('A') + cur_index), c  # return the menu option after the corresponding alphabet user selected
        elif use_exit_opt and user_input.lower() == 'x':
            # if the users has chosen to end the program
            return 'X', 'Exit'

        cur_index += 1

    return None
# endregion
