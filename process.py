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


# region HELPER FUNCTIONS

def get_rows(column, value):
    # returns rows where value of parsed column == parsed value
    rows = []
    for line in DATA_LIST:
        if _process_row(line)[column].lower() == value.lower():
            # add to return list if match
            rows.append(line)

    return rows


def _process_row(csv_line):
    # returns {review_id, rating, year_month, review_location, branch} of csv line parsed in
    return {'review_id': csv_line[0], 'rating': csv_line[1], 'year_month': csv_line[2], 'review_location': csv_line[3], 'branch': csv_line[4]}


def _add_branch(branch):
    # to add a branch to the list of branches if it hasn't already
    branch = branch.removeprefix('Disneyland_')
    if branch not in LIST_OF_BRANCHES:
        LIST_OF_BRANCHES.append(branch)

# endregion
