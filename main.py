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
import visual


# region MAIN FUNCTIONS


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

    # user_sel = None
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
        elif user_sel[0] == 'C':

            # *** TASK 9 ***

            # if user chooses 'B' (average score per year by park)
            ave_park_rating_yearly()

        elif user_sel[0] == 'D':

            # *** TASK 13 ***

            # if user chooses 'D' (average score per park by reviewer location)
            task_14()

    # -------------------------------------------------

    elif user_selection[0] == 'B':
        # navigates to visualize data submenu if user chooses 'B'
        user_sel = show_visualize_data_submenu()

        if user_sel[0] == 'A':

            # *** TASK 10 ***

            # to show chart of num of reviews for each park
            show_reviews_pie()

        elif user_sel[0] == 'B':

            # *** TASK 11 ***

            # if user chooses 'B' (average scores)
            show_ave_reviews_bar()

        elif user_sel[0] == 'C':

            # *** TASK 12 ***

            # if user chooses 'C' (ranking by nationality)
            show_top_reviewer_loc_for_park_pie()

        elif user_sel[0] == 'D':

            # *** TASK 13 ***

            # if user chooses 'D' (most popular month by park)
            task_13()


# endregion


# region SUB MENUS

def show_view_data_submenu():

    # *** VIEW DATA SUB MENU ***

    user_sel = tui.show_menu(
        title='Please enter one of the following options:',
        menu_choices=['View Reviews by Park', 'Number of Reviews by park and Reviewer Location', 'Average Score per Year by Park', 'Average Score per Park by Reviewer']
    )

    return user_sel


def show_visualize_data_submenu():

    # *** VISUALIZE DATA SUB MENU ***

    user_sel = tui.show_menu(
        title='Please enter one of the following options:',
        menu_choices=['Most Reviewed Parks', 'Average Scores', 'Park Ranking by Nationality', 'Most Popular Month by Park']
    )

    return user_sel

# endregion


# region SUB MENU FUNCTIONS

# region VEW DATA SUB MENU FUNC

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

        reviews = process.num_of_reviews(park_loc, reviewer_loc)

        if len(reviews) < 1:
            # if no reviews are found
            choice = tui.ask_user('No reviews found. Try again? (Y/N)')
        else:
            # if reviews are found
            choice = tui.ask_user(f'{process.loaded_branch_name(park_loc, False)} has received {len(reviews)} reviews from visitors from {reviewer_loc.capitalize()}.\nSearch again? (Y/N)\n')


def ave_park_rating_yearly():

    # *** TASK 9 ***

    choice = 'y'
    while choice == 'y':
        # to get the name of branch or park and year of reviews
        park_loc = tui.verify_name(
            initial_prompt='Please enter a branch location:\n',
            validation_prompt='Please enter a VALID branch location'
        )

        year = tui.verify_num(
            validation_prompt='Please choose years from 1900-2024:\n',
            num_range=[1900, 2024]
        )

        # gets the average rating
        ave_rating = process.ave_park_rating(park_loc, 'year', year)
        if ave_rating is None:
            # if no ratings are found
            choice = tui.ask_user('No ratings found. Search again? (Y/N)')
        else:
            # if the rating is found
            choice = tui.ask_user(f'The average rating for {process.loaded_branch_name(park_loc, False)} in {year} was {ave_rating} stars. Search again? (Y/N)')

# endregion


# region VISUALIZE DATA SUB MENU FUNC


def show_reviews_pie():

    # *** TASK 10 ***

    # to show a pie chart of how many reviews each park has gotten
    parks_and_reviews = process.get_all_park_reviews()  # gets reviews for all parks

    # list of parks and list of reviews
    parks = []
    total_reviews = []

    for park in parks_and_reviews:
        # adds parks to park list and add reviews to review list
        parks.append(park['branch'])
        total_reviews.append(park['num_of_reviews'])

    # show chart
    visual.show_pie_chart(parks, total_reviews)


def show_ave_reviews_bar():

    # *** TASK 11 ***

    # to show the average reviews of each park in a bar chart
    parks_and_ave_reviews = process.get_all_park_ave_reviews()  # gets all ave reviews

    # list of parks and reviews
    parks = []
    ave_review = []

    for park in parks_and_ave_reviews:
        # add each park and review to lists
        parks.append(park['branch'])
        ave_review.append(park['ave_reviews'])

    # show bar chart
    visual.show_bar_chart(parks, ave_review, 'Average Reviews by Park', 'Stars')


def show_top_reviewer_loc_for_park_pie():

    # *** TASK 12 ***

    # to show a pie chart of the top 10 reviewer_location for selected park
    choice = 'y'
    while choice == 'y':

        # to get the name of branch or park and year of reviews
        park_loc = tui.verify_name(
            initial_prompt='Please enter a branch location:\n',
            validation_prompt='Please enter a VALID branch location'
        )

        tui.tell_user('Please wait program is processing data and not stuck in a loop!')
        loc_and_ave_ratings = process.get_ave_reviews_by_loc_for_park(park_loc)  # gets a collection of dictionaries containing reviewer locations and their average reviews

        if len(loc_and_ave_ratings) < 1:
            # if no reviews are found
            choice = tui.ask_user('No reviews found. Try again? (Y/N)\n')
        else:
            top_loc = []
            top_loc_ratings = []

            # sort reviews that are found
            loc_and_ave_ratings = process.quick_sort(loc_and_ave_ratings, 'average_rating')

            current_index = len(loc_and_ave_ratings) - 1  # to start plotting bar chart from the highest review
            for i in range(10):
                # plots the top 10 highest reviews
                top_loc.append(loc_and_ave_ratings[current_index]['reviewer_location'])
                top_loc_ratings.append(loc_and_ave_ratings[current_index]['average_rating'])
                current_index -= 1

            visual.show_bar_chart(top_loc, top_loc_ratings, f'Top 10 Nationalities Reviews', 'Average Stars')
            choice = tui.ask_user('Try another park? (Y/N)\n')


def task_13():

    # *** TASK 13 ***

    # to show the average review selected park has gotten for every month

    # get all reviews for selected park
    choice = 'y'
    while choice == 'y':

        # to get the name of branch or park and year of reviews
        park_loc = tui.verify_name(
            initial_prompt='Please enter a branch location:\n',
            validation_prompt='Please enter a VALID branch location'
        )

        ratings = process.get_ave_month_rating_for_park(park_loc)  # gets average ratings for all months
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if len(ratings) > 0:
            # show bar chart
            visual.show_bar_chart(months, ratings, f'Most popular months for {park_loc.capitalize()}.', 'Stars')
            choice = tui.ask_user('Try another park? (Y/N)\n')
        else:
            # if no results were found
            choice = tui.ask_user('No ratings found. Try another park? (Y/N)\n')


def task_14():

    # *** TASK 14 ***

    # to get average rating for every park from every reviewer location

    parks = process.LIST_OF_BRANCHES
    average_ratings_and_locations = []

    tui.tell_user('Please wait program is processing data and not stuck in a loop!')
    for park in parks:
        # get the average rating and reviewer location for current park
        current_rating_and_loc = process.get_ave_reviews_by_loc_for_park(park)
        average_ratings_and_locations.append(current_rating_and_loc)

        # if reviews exist, display it
        tui.line_break()
        tui.tell_user(f'--- {process.loaded_branch_name(park, False)} Reviews ---')  # shows the name of current park
        tui.line_break()

        for rl in current_rating_and_loc:
            # displays each of the rating and review location for all reviewer locations gotten for current park
            tui.tell_user(f'-Reviewer location: {rl["reviewer_location"].capitalize()}, Average rating: {rl["average_rating"]} stars')


# endregion


# endregion


run()
