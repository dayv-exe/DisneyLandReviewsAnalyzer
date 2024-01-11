"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def show_header(header_txt, header_pattern_char):

    # *** SECTION A, TASK 1 ***

    # to show welcome text to user
    tell_user(header_pattern_char * len(header_txt))
    tell_user(header_txt)
    tell_user(header_pattern_char * len(header_txt))


def show_menu(title, menu_choices, show_choice_confirmation=False, show_exit_opt=False):
    # PRINTS MENU OPTIONS
    # RETURNS USER CHOICE (if valid)
    _print_menu_opts(title, menu_choices, show_exit_opt)

    user_input = ask_user('')
    sel_opt = _get_sel_opt(user_input, menu_choices, show_exit_opt)

    while sel_opt is None:
        user_input = ask_user('Please choose a valid option from menu!\n')
        sel_opt = _get_sel_opt(user_input, menu_choices, show_exit_opt)

    if show_choice_confirmation:
        tell_user(f'You have chosen option {sel_opt[0]} - {sel_opt[1]}\n')

    return sel_opt[0], sel_opt[1]  # returns users choice as the alphabet representing choice, then the choice text


def tell_user(text):
    print(text)


def ask_user(text):
    return input(text)


def show_review_text(rating, year_month, reviewer_location):
    # to print reviews in a uniformed manner
    tell_user(f'From {reviewer_location:}')
    tell_user(f"{'*' * int(rating)} ({rating} stars)")
    tell_user(f'Reviewed on: {year_month}')
    line_break()


def line_break():
    tell_user('')


def new_line():
    tell_user('\n')


def verify_name(initial_prompt, validation_prompt):
    # to ensure that any name user enters is a valid length and type
    user_input = ask_user(initial_prompt)
    while len(user_input) < 2:
        # make sure user input is valid
        user_input = ask_user(f'{validation_prompt} \n')

    return user_input


def verify_num(validation_prompt, num_range):
    # to ensure that any number user enters is a valid quantity and type
    user_input = ''
    valid = False

    while not valid:
        # prompts user to enter number
        user_input = ask_user(validation_prompt)
        try:
            # if the number is valid and falls within min and max values
            user_input = int(user_input)
            if num_range[0] <= user_input <= num_range[1]:
                valid = True
        except ValueError:
            # if user did not enter a number
            valid = False

    return int(user_input)

# region HELPER FUNCTIONS
# these functions abstract away repetitive code to make project cleaner


def _print_menu_opts(prompt_txt, menu_choices, show_exit_opt=False):
    # prints out prompt to select a menu option then prints out menu options
    # 'show_exit_opt=True' will cause the '[X] Exit' choice to be added to menu being printed
    cur_index = 0
    tell_user(prompt_txt)
    for choice in menu_choices:
        tell_user(f'    [{chr(ord("A") + cur_index)}] {choice}')
        cur_index += 1

    if show_exit_opt:
        # to give user menu option to exit
        tell_user(f'    [X] Exit')


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
