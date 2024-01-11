"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt


def show_pie_chart(labels, sizes):

    def size_lbl(pct):
        # to show slice percent and size inside slice of pie chart
        _abs = int(round(pct/100.*sum(sizes)))
        return f'{_abs}\n({pct: .1f}%)'

    # to show a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct=lambda pct: size_lbl(pct))
    plt.show()


def show_bar_chart(labels, counts, title, y_label):
    # to show bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, counts)

    ax.set_ylabel(y_label)
    ax.set_title(title)

    plt.show()
