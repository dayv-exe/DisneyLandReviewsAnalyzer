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

tui.show_header()
process.read_data()


# *** TASK 3 ***

# show main menu options
def show_main_menu():
    user_sel = tui.show_menu(
        prompt='Please enter the letter which corresponds with your desired menu choice:',
        menu_choices=['View Data', 'Visualize Data'],
        show_choice_confirmation=True,
        show_exit_opt=True
    )
    confirm_user_sel = tui.show_menu(
            prompt='Confirm selection:',
            menu_choices=['View Data', 'Visualize Data'],
            show_choice_confirmation=False,
            show_exit_opt=True
    )

    # region REMOVE BLOCK TO STOP SELECTION MATCHING RULE

    # the two selections (initial sel, and confirmation sel) must match for the program to proceed according to task 5?

    while not user_sel[0] == confirm_user_sel[0]:
        # to make sure both selections match
        user_sel = confirm_user_sel
        confirm_user_sel = tui.show_menu(
            prompt=f'You have chosen option {user_sel[0]} - {user_sel[1]}\n\nConfirm selection:',
            menu_choices=['View Data', 'Visualize Data'],
            show_choice_confirmation=False,
            show_exit_opt=True
        )

    # endregion

    if confirm_user_sel[0] == 'X':
        quit()


    show_sub_menu(confirm_user_sel)


def show_sub_menu(user_sel):
    tui.show_menu(
        prompt='Please enter the letter which corresponds with your desired menu choice:',
        menu_choices=['View Data', 'Visualize Data'],
        show_choice_confirmation=True,
        show_exit_opt=True
    )


show_main_menu()
