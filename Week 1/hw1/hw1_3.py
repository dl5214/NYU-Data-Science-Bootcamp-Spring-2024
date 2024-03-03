# Write a program that iterates from 1 to 20,
# printing each number and whether it's odd or even.


def main():
    for i in range(1,21):  # 21 exclusive
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")


if __name__ == '__main__':
    main()