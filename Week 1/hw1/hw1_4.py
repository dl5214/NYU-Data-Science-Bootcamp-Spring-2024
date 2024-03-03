# Write a function sum_of_integers(a, b) that takes two integers
# as input from the user and returns their sum.


def sum_of_integers(a, b):
    return a + b


def main():
    a = int(input("Enter the first integer (1 of 2): "))
    b = int(input("Enter the second integer (2 of 2): "))
    result = sum_of_integers(a, b)
    print(f"The sum of {a} and {b} is {result}")


if __name__ == '__main__':
    main()