"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""


import csv


def read_data():
    # SECTION A, TASK 2
    # to read data from dataset
    file_path = './data/disneyland_reviews.csv'
    data_list = []
    row_count = 0
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # to skip over header
        for line in csv_reader:
            data_list.append(line)
            row_count += 1

    print(f"\nSuccessfully read {row_count} lines from dataset!\n")
