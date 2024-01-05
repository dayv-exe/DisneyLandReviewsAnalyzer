"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import process
import tui


def run():
    tui.show_header()
    process.read_data()
    show_main_menu()


# *** TASK 3 ***

# show main menu options
def show_main_menu():
    user_sel = tui.show_menu(

        # *** TASK 3 ***

        # allow user to select choice
        title='Please enter the letter which corresponds with your desired menu choice:',
        menu_choices=['View Data', 'Visualize Data'],
        show_choice_confirmation=True,
        show_exit_opt=True
    )

    confirm_user_sel = tui.show_menu(

        # *** TASK 5 ***

        # allows user to confirm choice
        title='Confirm selection:',
        menu_choices=['View Data', 'Visualize Data'],
        show_choice_confirmation=False,
        show_exit_opt=True
    )

    # region REMOVE BLOCK TO STOP SELECTION MATCHING RULE

    # the two selections (initial sel, and confirmation sel) must match for the program to proceed according to task 5?

    while not user_sel[0] == confirm_user_sel[0]:
        # to make sure both choices selected match
        user_sel = confirm_user_sel
        confirm_user_sel = tui.show_menu(
            title=f'You have chosen option {user_sel[0]} - {user_sel[1]}\n\nConfirm selection:',
            menu_choices=['View Data', 'Visualize Data'],
            show_choice_confirmation=False,
            show_exit_opt=True
        )

    # endregion

    if confirm_user_sel[0] == 'X':
        # if user chooses to exit program
        quit()

    # if user chooses other options
    show_sub_menu(confirm_user_sel)


def show_sub_menu(user_selection):

    # *** TASK 6 ***

    user_sel = None
    if user_selection[0] == 'A':
        user_sel = tui.show_menu(
            title='Please enter one of the following options:',
            menu_choices=['View Reviews by Park', 'Number of Reviews by park and Reviewer Location', 'Average Score per Year by Park', 'Average Score per Park by Reviewer']
        )
    elif user_selection[0] == 'B':
        user_sel = tui.show_menu(
            title='Please enter one of the following options:',
            menu_choices=['Most Reviewed Parks', 'Average Scores', 'Park Ranking by Nationality', 'Most Popular Month by Park']
        )


run()
