# Writea function that given an input list of integers,
# returns a list of only the odd numbers in the input list 

# numbers = [5,7,2,]

def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.
    """
    odd_items = []
    for item in numbers:
        if item % 2 != 0:
            odd_items.append(item)

    return odd_items


### Don't edit the following. #
stdin = input()               #
print all_odd(stdin)          #
###############################

# testing = all_odd()
# print testing

