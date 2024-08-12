import numpy as np
from numpy.polynomial import Polynomial
import math
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def plot_poly(a, b, p):
    # Generate x values for plotting the polynomial curve
    x_new = np.linspace(min(a), max(a), 500)  # 500 points between min and max of original x values
    y_new = p(x_new)  # Evaluate the polynomial at x_new

    # Plot the original points
    plt.scatter(a, b, color='red', label='Original Points')

    # Plot the polynomial curve
    plt.plot(x_new, y_new, color='blue', label='4th Degree Polynomial Fit')

    # Add labels and legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('4th Degree Polynomial Fit')
    plt.legend()

    # Show the plot
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    x = np.array([8, -15, 2, 4, -2, -11, 5, -10, -6])
    y = np.array([13924, -5097, 5494, 5904, 5394, -5361, 6703, -4022, 2094])

    poly = Polynomial.fit(x, y, 4)

    plot_poly(x, y, poly)

    coeff = poly.convert().coef

    print(math.ceil(coeff[0]))
