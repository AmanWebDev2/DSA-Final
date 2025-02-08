"""
All about seperation of concern

GOAL - 
- Clean
- Easy to extend
- Easy to maintain
- Memory Efficient
- DRY
"""

"""
Pure Function -
1.Consistent Output:
    No matter how many times you call a pure function with the same input, you'll always get the same result. For example, a function that adds two numbers is pure because 2 + 3 is always 5.

No Side Effects:
2. A pure function doesn’t change any state outside of itself. It doesn’t modify global variables, write to a file, or print to the console. It just takes inputs and gives you an output.
"""
wizard = {"name": "aman", "power": "strength"}


# def change(char):
#     char["power"] = "fyling"
#     return char


# print(change(wizard))
# print(wizard)

# map, filter, reduce, zip

# map(action,data)


def action_multiply_by2(item: int):
    return item * 2


print(map(action_multiply_by2, [1, 2, 3]))  # map object
print(list(map(action_multiply_by2, [1, 2, 3])))


# filter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def action_even(item: int):
    return item % 2 == 0


print(list(filter(action_even, my_list)))


# zip
# zip two or more list together

my_list = [1, 2, 3]
your_list = [10, 20, 30]
print(list(zip(my_list, your_list)))  # [(1,0),(2,10),(3,10)]


# reduce
from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# 0 is the initial value for acc
print(reduce(accumulator, my_list, 0))
