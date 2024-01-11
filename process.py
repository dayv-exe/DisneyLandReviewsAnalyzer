"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""


import csv

import tui


LIST_OF_BRANCHES = []
DATA_LIST = []


def read_dataset(file_path):
    # *** TASK 2 ***

    # to read data from dataset
    row_count = 0
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # to skip over header
        for line in csv_reader:
            DATA_LIST.append(line)
            _add_branch(_get_frm_row(line)['branch'])
            row_count += 1

    tui.tell_user(f'\nSuccessfully read {row_count} rows from dataset!\n')


def get_reviews(park_loc, reviewer_loc=None):
    # to get the name of branch or park and reviewer location from user

    # fetch list of reviews for parks in given loc then from that list, fetch list of reviews where reviewer loc == given reviewer loc

    # retrieve all reviews for this park
    reviews = get_rows('branch', loaded_branch_name(park_loc))

    if reviewer_loc is None:
        # if we only want to get total num of reviews
        return reviews

    # if reviews exists, get reviews from visitors in a certain location
    if len(reviews) > 0:
        reviews = get_rows('Reviewer_Location', reviewer_loc, reviews)
        return reviews
    else:
        return []


def get_pos_reviews(park_loc, reviewer_loc=None):
    # returns a list of positive reviews i.e. reviews 4 stars and above (3 stars in neutral, 2 or less is negative)
    reviews = get_reviews(park_loc, reviewer_loc)
    pos_reviews = []

    for review in reviews:
        if int(_get_frm_row(review)['rating']) >= 4:
            pos_reviews.append(review)

    return pos_reviews


def get_ave_rating(park_loc, selected_column='none', column_val=None):
    # to get average score of a park

    # implementation: selected_column='none' will cause func to return ave reviews of selected park, while selected_column='year'  will cause func to return average rating for selected park where year == column_val.

    # get rows of park reviews (if a column is selected, get rows where the column_value parsed == value of current row column)

    # retrieve all reviews for this park
    reviews = get_rows('branch', loaded_branch_name(park_loc))

    # if reviews exists, get reviews from given year
    # 'year-*' to search for the year instead of a specific month in a year e.g. 2014-* will return average of all reviews in 2014
    if len(reviews) > 0:
        if selected_column == 'year':
            # if we only want to get reviews in a certain year, filter out all other years
            reviews = get_rows('year_month', str(column_val) + '-*', reviews)  # get rows where year is year provided

        elif selected_column == 'reviewer_location':
            # if we only want to get reviews in a certain reviewer location, filter out all other review locations
            reviews = get_rows('reviewer_location', column_val, reviews)  # get rows where review_location is reviewer_location provided

        elif selected_column == 'month':
            # '*-month' to search for the months in all years e.g. *-3 will return average for all reviews in March of all years

            # if we only want to get reviews in a certain month and filter out all other reviews not from that month
            reviews = get_rows('year_month', '*-' + str(column_val), reviews)  # get rows where month is month parsed

        rating = []
        for review in reviews:
            # add value in rating column only to new array
            rating.append(int(_get_frm_row(review)['rating']))

        length = len(rating)  # store the length of the array
        rating_sum = sum(rating)  # get sum of numbers in the array
        if rating_sum > 0:
            # then divide by length of the array
            return rating_sum / length

        # return none of no ratings are found
        else:
            return None
    else:
        return None


def get_all_reviews():

    # *** TASK 10 ***

    # returns a list of dictionaries containing parks and their num of reviews
    parks_and_reviews = []
    for park in LIST_OF_BRANCHES:
        # loops through ever branch then returns all parks and their total reviews
        parks_and_reviews.append({
            'branch': park,
            'num_of_reviews': len(get_reviews(park)),
        })

    return parks_and_reviews


def get_all_ave_reviews():

    # *** TASK 11 ***

    # returns a list of dictionaries containing parks and their ave reviews
    parks_and_ave_reviews = []
    for park in LIST_OF_BRANCHES:
        # loops through ever branch then returns all parks and their total reviews
        parks_and_ave_reviews.append({
            'branch': park,
            'ave_reviews': get_ave_rating(park),
        })

    return parks_and_ave_reviews


def get_ave_reviews_by_loc(park_name):
    park_reviews = get_reviews(park_name)  # gets all reviews for selected park

    reviewer_locations = []  # will store all reviewer location for selected park
    return_list = []  # will store a collection of dict containing all reviewer locations and their respective averages

    for review in park_reviews:
        # from reviews of selected park, get a list of all the review_locations and add them to list if not already there
        if _get_frm_row(review)['reviewer_location'] not in reviewer_locations:
            reviewer_locations.append(_get_frm_row(review)['reviewer_location'])

    for rl in reviewer_locations:
        # then for every item in the reviewer_locations list, add average rating for each location to return list
        ave_rating = get_ave_rating(park_name, 'reviewer_location', rl)  # average rating of selected park where reviewer location == rl
        return_list.append({'reviewer_location': rl, 'average_rating': ave_rating})

    return return_list


def get_ave_month_rating(park_name):

    # *** TASK 13 ***

    # will return a list containing the average rating selected park received in every month

    ave_monthly_rating = []  # list that will contain the ave rating for each month, with index 0 representing january and so on

    for i in range(12):
        # loops 12 times to get reviews for all 12 months
        ave_monthly_rating.append(
            get_ave_rating(park_name, 'month', i + 1)
        )

    return ave_monthly_rating  # returns the average ratings for all 12 months


# region HELPER FUNCTIONS

def get_rows(column, value, data_list=None):
    # returns rows where value of parsed column == parsed value
    if data_list is None:
        data_list = DATA_LIST
    rows = []
    for line in data_list:
        if column.lower() == 'year_month' and not _get_frm_row(line)[column.lower()] == 'missing':

            # TO COMPARE YEAR MONTH VALUES

            # add an astrix after year and hyphen to search for all months in that year e.g. 2018-* will return all reviews for 2018 while 2018-3 will return reviews for March 2018
            year_month = value.split('-')  # splits the year month value to read strings before and after the hyphen
            if year_month[1] == '*':
                # if the string after the hyphen is an astrix then get all rows with the same year as provided
                if _get_frm_row(line)[column.lower()].split('-')[0] == year_month[0]:
                    rows.append(line)
            elif year_month[0] == '*':
                # if the string before the hyphen is an astrix then get all rows with the same month as provided
                if _get_frm_row(line)[column.lower()].split('-')[1] == year_month[1]:
                    rows.append(line)
            else:
                # if the char after the hyphen is not an astrix then get only row with the exact year_month that's provided
                if _get_frm_row(line)[column.lower()] == year_month[0] + '-' + year_month[1]:
                    rows.append(line)
        else:

            # TO COMPARE OTHER VALUES EXCEPT YEAR_MONTH

            if _get_frm_row(line)[column.lower()].lower() == value.lower():
                # add to return list if match
                rows.append(line)

    return rows


def _get_frm_row(row):
    # returns {review_id, rating, year_month, review_location, branch} of csv line parsed in
    return {'review_id': row[0], 'rating': row[1], 'year_month': row[2], 'reviewer_location': row[3], 'branch': row[4]}


def _add_branch(branch):
    # to add a branch to the list of branches if it hasn't already
    branch = clean_branch_name(branch)

    if branch not in LIST_OF_BRANCHES:
        LIST_OF_BRANCHES.append(branch)


def clean_branch_name(name):
    # returns the name of branch without 'Disneyland_'
    # e.g. paris instead of disneyland_paris
    return name.removeprefix('Disneyland_')


def loaded_branch_name(name, use_underscore=True):
    # returns the name of branch with 'Disneyland_'
    # e.g. paris will become Disneyland_Paris
    return 'Disneyland_' + name.capitalize() if use_underscore else 'Disneyland ' + name.capitalize()


# region SORTING ALGO
def quick_sort(array, key=None):
    # sorting algo entry point
    return _sort_array(array, 0, len(array) - 1, key)


def _sort_array(array, start, end, key=None):
    # uses QUICK SORT algorithm to sort an array
    if end > start:
        pivot = _lomuto_partition(array, start, end, key)
        _sort_array(array, start, pivot - 1, key)
        _sort_array(array, pivot + 1, end, key)

    return array


def _get_array_index(array_index, the_key):
    # return item in an array if no key is provided
    # return value of dictionary if key is provided
    return array_index if the_key is None else array_index[the_key]


def _lomuto_partition(array, start, end, key):
    # key allows algorithm to look into values in a dictionary which is what places are stored as
    pivot = array[end]  # selects last item in array as pivot
    pivot_val = pivot if key is None else pivot[key]  # check if key is provided meaning we are sorting dictionaries, key indicates what key in the dictionary algo should sort by

    i = start - 1

    for j in range(start, end):
        if _get_array_index(array[j], key) <= pivot_val:
            # swap and move 1st finger if 2nd finger is less than or equal to pivot
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]  # set new pivot pos
    return i + 1
# endregion


# endregion
