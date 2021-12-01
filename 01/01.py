import numpy as np

#
# Exercise #1
#
input_array = np.loadtxt("./01/inputs.txt")
amount_of_increases = (np.divide(input_array, np.roll(input_array, 1)) > 1).sum()

print("Exercise 1: ", amount_of_increases)

#
# Exercise #2
#
def rolling_sum(a, n=4) :
    ret = np.cumsum(a)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:]

input_array = rolling_sum(input_array, n=3)
amount_of_increases = (np.divide(input_array, np.roll(input_array, 1)) > 1).sum()

print("Exercise 2: ", amount_of_increases)
