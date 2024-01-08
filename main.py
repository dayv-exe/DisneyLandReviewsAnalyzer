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
    tui.show_header(
        header_txt='Disneyland Review Analyser',
        header_pattern_char='-'
    )
    process.read_dataset(file_path='./data/disneyland_reviews.csv')
    show_main_menu()


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
        # navigates to view data sub menu if user chooses 'A'
        user_sel = show_view_data_submenu()

        if user_sel[0] == 'A':

            # *** TASK 7 ***

            # if while in view data sub menu user chooses 'A' (view reviews by park)
            view_reviews_by_park()

        elif user_sel[0] == 'B':

            # *** TASK 8 ***

            # if user chooses 'B' (number of reviews by park and reviewer location)
            num_of_reviews_by_park()

    # -------------------------------------------------

    elif user_selection[0] == 'B':
        # navigates to visualize data submenu if user chooses 'B'
        user_sel = show_visualize_data_submenu()


# region SUB MENUS

def show_view_data_submenu():
    user_sel = tui.show_menu(
        title='Please enter one of the following options:',
        menu_choices=['View Reviews by Park', 'Number of Reviews by park and Reviewer Location', 'Average Score per Year by Park', 'Average Score per Park by Reviewer']
    )

    return user_sel


def show_visualize_data_submenu():
    user_sel = tui.show_menu(
        title='Please enter one of the following options:',
        menu_choices=['Most Reviewed Parks', 'Average Scores', 'Park Ranking by Nationality', 'Most Popular Month by Park']
    )

    return user_sel

# endregion


# region SUB MENU FUNCTIONS

def view_reviews_by_park():

    # *** TASK 7 ***

    choice = 'y'
    while choice.lower() == 'y':
        # to get the name of branch or park from user
        park_name = tui.verify_name(
            initial_prompt='Please enter a branch location to view reviews: \n',
            validation_prompt='Please enter a VALID branch location to view reviews: \n'
        )

        # get a list of rows where the branch name matches name user provided
        reviews = process.get_rows('branch', 'disneyland_' + park_name)

        if len(reviews) < 1:
            # if there are no reviews for branch uer entered prompt them to try again
            choice = tui.ask_user(f'No results! Try another park? (Y/N)\n')
        else:
            # if reviews exist, display it
            tui.line_break()
            tui.tell_user(f'--- {process.loaded_branch_name(reviews[0][4], False)} Reviews ---')
            tui.line_break()
            for review in reviews:
                tui.show_review_text(review[1], review[2], review[3])
            choice = tui.ask_user(f'Try another park? (Y/N)\n')


def num_of_reviews_by_park():

    # *** TASK 8 ***

    choice = 'y'
    while choice.lower() == 'y':

        # to get the name of branch or park and reviewer location from user
        park_loc = tui.verify_name(
            initial_prompt='Please enter a branch location:\n',
            validation_prompt='Please enter a VALID branch location'
        )

        reviewer_loc = tui.verify_name(
            initial_prompt='Please enter a preferred reviewer location:\n',
            validation_prompt='Please enter a VALID preferred reviewer location: \n'
        )

        # fetch list of reviews for parks in given loc then from that list, fetch list of reviews where reviewer loc == given reviewer loc

        # retrieve all reviews for this park
        reviews = process.get_rows('branch', process.loaded_branch_name(park_loc))
        # if reviews exists, get reviews from visitors in a certain location
        if len(reviews) > 0:

            reviews = process.get_rows('Reviewer_Location', reviewer_loc, reviews)
            if len(reviews) > 0:
                # if reviews from visitors from user parsed location exists
                c = tui.ask_user(f'{process.loaded_branch_name(park_loc, False)} has {len(reviews)} reviews from visitors from {reviewer_loc.capitalize()}. Try another search? (Y/N)\n')
            else:
                c = tui.ask_user('No reviews found. Try another search? (Y/N)\n')
        else:
            c = tui.ask_user('No such branch exists. Try another search? (Y/N)\n')

        choice = c


# endregion


run()
