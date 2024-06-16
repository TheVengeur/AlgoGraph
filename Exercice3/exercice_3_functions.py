# import time
# import matplotlib.pyplot as plt
# from numpy.polynomial import Polynomial as P
import time
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle


def function_1(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.

    The inside loop of the function for j in range(i) is running n² times with a value of j going from 0, to n² - 1
    the time complexity of the the function is therefore the sum of every numbers from 0 to n²
     which is the formula: S(n) = n x (n + 1) / 2
     or in this instance: S(n) = n² x ((n² - 1) + 1) / 2
     that can be simplified:
        S(n) = n² x n² / 2
        S(n) = n⁴ / 2
    Which can be simplified S(n) = O(n⁴)
    """
    temp_list = list()
    for i in range(n ** 2):
        temp = 0
        for j in range(i):
            temp += j
        temp_list.append(temp)
    sum(temp_list)


def function_2(n: int) -> None:
    """
    compute the time complexity of running
    this function as a function of n.

    do not hesitate to do some reseach about the
    complexity of the functions used and to average
    the measured times over a number of trials if necessary.

    the time complexity of each line inside the loop is considered to be O(n)
    therefore the three lines inside of the loop have a time complexity of O(n) + O(n) + O(n) = O(3n) that can be simplified O(n)
    So the time complexity of the function will be O(n) x O(n) = O(n²)
    """
    for i in range(n):
        temp_list = [j + i for j in range(n)]
        shuffle(temp_list)
        max(temp_list)


def tmp(ns, function):
    times = []

    for n in ns:
        start_time = time.time()
        function(n)
        times.append(time.time() - start_time)
    return times


def verify_bound(function, polynomial_degree: int, figure_numer: int) -> None:
    ns = [i for i in range(50)]
    times = []

    for _ in ns:
        times.append(tmp(ns, function))
    zipped_times = zip(*times)
    times = [sum(sub_times) / len(sub_times) for sub_times in zipped_times]
    polynomial_fit = np.polyfit(ns, times, polynomial_degree)
    polynomial_function = np.poly1d(polynomial_fit)
    polynomial_n = np.linspace(min(ns), max(ns), 50)
    polynomial_times = polynomial_function(polynomial_n)

    plt.subplot(1, 2, figure_numer)
    plt.plot(ns, times, '-', label='Measured times')
    plt.plot(polynomial_n, polynomial_times, '-', label='Fitted polynomial (degree ' + str(polynomial_degree) + ')')
    plt.title('Elapsed time computing ' + function.__name__)
    plt.xlabel('n')
    plt.ylabel('Time to compute f1(n) (seconds)')
    plt.legend()


def generate_bound():
    plt.figure(figsize=(14, 6))
    verify_bound(function_1, 4, 1)
    verify_bound(function_2, 2, 2)
    plt.show()
