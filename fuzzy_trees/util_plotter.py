"""
@author: Zhaoqing Liu
@email : Zhaoqing.Liu-1@student.uts.edu.au
@date  : 27/4/21 2:23 pm
@desc  :
"""
import matplotlib.pyplot as plt

COLOUR = ["b", "g", "r", "c", "m", "y", "k", "w"]


# The colours above are equivalent to the colours below:
# COLOUR = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]


def plot_multi_curves(q, title=None, x_label=None, y_label=None, x_limit=None, y_limit=None):
    """
    Plot the comparison of multiple curves.
    """
    # Read result from the queue "q" and save them.
    x_list = []
    y_list = []
    while not q.empty():
        res_list = q.get()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(res_list)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    # 1st step: Create a figure as a canvas.
    plt.figure()

    # 2nd step: Plot on the figure.
    # Plot all curves iteratively.
    for i, v in enumerate(res_list):
        plt.plot(v[0], v[1], color=COLOUR[i], linewidth=10.0, linestyle="-")

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xlim(x_limit)
    plt.ylim(y_limit)

    # 3rd step: Show the figure.
    plt.show()


def plot_multi_curves_dyn(q, x_list, y_list, title=None, x_label=None, y_label=None, x_limit=None, y_limit=None):
    pass


if __name__ == '__main__':
    plot_multi_curves([], [], "My Title", "x label", "y label", (10, 20), (-10, 0))
