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
            _add_branch(_process_row(line)['branch'])
            row_count += 1

    tui.tell_user(f'\nSuccessfully read {row_count} lines from dataset!\n')


def num_of_reviews_from_loc(park_loc, reviewer_loc):

    # *** TASK 8 ***

    # to get the name of branch or park and reviewer location from user

    # fetch list of reviews for parks in given loc then from that list, fetch list of reviews where reviewer loc == given reviewer loc

    # retrieve all reviews for this park
    reviews = get_rows('branch', loaded_branch_name(park_loc))
    # if reviews exists, get reviews from visitors in a certain location
    if len(reviews) > 0:
        reviews = get_rows('Reviewer_Location', reviewer_loc, reviews)
        return reviews
    else:
        return []


# region HELPER FUNCTIONS

def get_rows(column, value, data_list=None):
    # returns rows where value of parsed column == parsed value
    if data_list is None:
        data_list = DATA_LIST
    rows = []
    for line in data_list:
        if _process_row(line)[column.lower()].lower() == value.lower():
            # add to return list if match
            rows.append(line)

    return rows


def _process_row(csv_line):
    # returns {review_id, rating, year_month, review_location, branch} of csv line parsed in
    return {'review_id': csv_line[0], 'rating': csv_line[1], 'year_month': csv_line[2], 'reviewer_location': csv_line[3], 'branch': csv_line[4]}


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
