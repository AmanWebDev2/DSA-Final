"""
Pattern -> https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/
"""


def one(n: int):
    for _ in range(n):
        for _ in range(n):
            print("*", end=" ")
        print("")


def two(n: int):
    for row in range(n):
        for _ in range(row + 1):
            print("*", end=" ")
        print()


def three(n: int):
    for row in range(n):
        for col in range(row + 1):
            print(col + 1, end=" ")
        print()


def four(n: int):
    for row in range(1, n + 1):
        for _ in range(row):
            print(row, end=" ")
        print()


def five(n: int):
    for row in range(1, n + 1):
        star = n - row + 1
        for _ in range(1, star + 1):
            print("*", end=" ")
        print()


def six(n: int):
    for row in range(1, n + 1):
        star = n + 1 - row
        for col in range(1, star + 1):
            print(col, end=" ")
        print()


def seven(n: int):
    for row in range(1, n + 1):
        for col in range(1, 2 * n):
            if (col + row >= n + 1) and (col - row <= n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# one(5)
# two(5)
# three(5)
# four(5)
# five(5)
# six(5)
seven(5)
