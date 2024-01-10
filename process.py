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

    tui.tell_user(f'\nSuccessfully read {row_count} lines from dataset!\n')


def num_of_reviews(park_loc, reviewer_loc=None):
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


def ave_park_rating(park_loc, year=None):
    # to get average score of a park

    # get rows of park reviews where year and park name == parsed arguments

    # retrieve all reviews for this park
    reviews = get_rows('branch', loaded_branch_name(park_loc))

    # if reviews exists, get reviews from given year
    # '-*' to search for all months in the year instead of a specific month in a year
    if len(reviews) > 0:
        if year is not None:
            # if we only want to get reviews in a certain year, filter out all other years
            reviews = get_rows('year_month', str(year) + '-*', reviews)  # get rows where year is year provided
        rating = []
        for review in reviews:
            # add value in rating column only to new array
            rating.append(int(_get_frm_row(review)['rating']))

        length = len(rating)  # store the length of the array
        ave = sum(rating)  # get sum of numbers in the array
        if ave > 0:
            # then divide by length of the array
            return ave / length

        # return none of no ratings are found
        else:
            return None
    else:
        return None


def get_all_park_reviews():

    # *** TASK 10 ***

    # returns a list of dictionaries containing parks and their num of reviews
    parks_and_reviews = []
    for park in LIST_OF_BRANCHES:
        # loops through ever branch then returns all parks and their total reviews
        parks_and_reviews.append({
            'branch': park,
            'num_of_reviews': len(num_of_reviews(park)),
        })

    return parks_and_reviews


def get_all_park_ave_reviews():

    # *** TASK 11 ***

    # returns a list of dictionaries containing parks and their ave reviews
    parks_and_ave_reviews = []
    for park in LIST_OF_BRANCHES:
        # loops through ever branch then returns all parks and their total reviews
        parks_and_ave_reviews.append({
            'branch': park,
            'ave_reviews': ave_park_rating(park),
        })

    return parks_and_ave_reviews


# region HELPER FUNCTIONS

def get_rows(column, value, data_list=None):
    # returns rows where value of parsed column == parsed value
    if data_list is None:
        data_list = DATA_LIST
    rows = []
    for line in data_list:
        if column.lower() == 'year_month':

            # TO COMPARE YEAR MONTH VALUES

            # add an astrix after year and hyphen to search for all months in that year e.g. 2018-* will return all reviews for 2018 while 2018-3 will return reviews for March 2018
            year_month = value.split('-')  # splits the year month value to read strings before and after the hyphen
            if year_month[1] == '*':
                # if the string after the hyphen is an astrix then get all rows with the same year as provided
                if _get_frm_row(line)[column.lower()].split('-')[0] == year_month[0]:
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

# endregion
