"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def show_header(header_txt='Disneyland Review Analyser'):

    # *** SECTION A, TASK 1 ***

    # to show welcome text to user
    print('-' * len(header_txt))
    print(header_txt)
    print('-' * len(header_txt))


def show_menu(prompt, menu_choices, show_choice_confirmation=False, show_exit_opt=False):
    # PRINTS MENU OPTIONS
    # RETURNS USER CHOICE (if valid)
    _print_menu_opts(prompt, menu_choices, show_exit_opt)
    sel_opt = None

    user_input = input('')
    sel_opt = _get_sel_opt(user_input, menu_choices, show_exit_opt)

    while sel_opt is None:
        user_input = input('Please choose a valid option from menu!\n')
        sel_opt = _get_sel_opt(user_input, menu_choices, show_exit_opt)

    if show_choice_confirmation:
        print(f'You have chosen option {sel_opt[0]} - {sel_opt[1]}\n')

    return sel_opt[0], sel_opt[1]  # returns users choice as the alphabet representing choice, then the choice text

def show_sub_menu(sel_opt):

    # *** TASK 6 ***

    if sel_opt[0] == 'A':
        # if menu option 'A' is selected
        sub_menu_a = ['View Reviews by Park', 'Number of Reviews by park and Reviewer Location', 'Average Score per Year by Park', 'Average Score per Park by Reviewer']
        _print_menu_opts('\nPlease enter one of the following options:', sub_menu_a)

    elif sel_opt[0] == 'B':
        # if menu option 'B' is selected
        sub_menu_b = ['Most Reviewed Parks', 'Average Scores', 'Park Ranking by Nationality', 'Most Popular Month by Park']
        _print_menu_opts('\nPlease enter one of the following options:', sub_menu_b)


# region HELPER FUNCTIONS
# these functions abstract away repetitive code to make project cleaner
def _print_menu_opts(prompt_txt, menu_choices, show_exit_opt=False):
    # prints out prompt to select a menu option then prints out menu options
    # 'show_exit_opt=True' will cause the '[X] Exit' choice to be added to menu being printed
    cur_index = 0
    print(prompt_txt)
    for choice in menu_choices:
        print(f'    [{chr(ord("A") + cur_index)}] {choice}')
        cur_index += 1

    if show_exit_opt:
        # to give user menu option to exit
        print(f'    [X] Exit')


def _get_sel_opt(user_input, menu_choices, allow_exit_opt=False):
    # gets selected option
    # returns the details of the option user selected if it matches any option provided (returns the alphabet and choice text)
    # returns None if option user selected is invalid
    # 'allow_exit_opt=True' will allow for func to return 'X, Exit' for further processing in caller function

    cur_index = 0
    for c in menu_choices:
        if user_input.lower() == chr(ord('a') + cur_index):
            return chr(ord('A') + cur_index), c  # return the menu option after the corresponding alphabet user selected
        elif allow_exit_opt and user_input.lower() == 'x':
            # if the users has chosen to end the program
            return 'X', 'Exit'

        cur_index += 1

    return None
# endregion
