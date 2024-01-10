"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt


def show_pie_chart(labels, sizes):
    # to show a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.show()


def show_bar_chart(labels, counts, title, y_label):
    # to show bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, counts)

    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.show()
