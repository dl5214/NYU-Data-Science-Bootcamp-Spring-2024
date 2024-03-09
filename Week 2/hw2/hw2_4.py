# 4)Create a 4x4 NumPy array filled with random integers between 1 and 100.
# Then, reshape this array into two separate 2D arrays, where one represents the rows
# and the other represents the columns. Write a function, preferably using a lambda function,
# to calculate the sum of each row and each column separately, and return the results
# as two separate NumPy arrays

import numpy as np


def main():
    array = np.random.randint(1, 100, (4, 4))
    print("====== Original 4 x 4 array ======")
    print(array)

    # Function to calculate the sum of each row and each column
    # Using lambda functions as requested
    row_sums = np.apply_along_axis(lambda x: np.sum(x), 1, array)
    col_sums = np.apply_along_axis(lambda x: np.sum(x), 0, array)

    print("====== Row_sum array ======")
    print(row_sums)

    print("====== Col_sum array ======")
    print(col_sums)


if __name__ == '__main__':
    main()
