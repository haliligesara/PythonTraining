# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

l1 = [1,2,3]
l2 = ['a', 'd', 'c']

def merge_lists(l1, l2):
    res = l1 + l2
    return res

print(merge_lists(l1,l2))








































# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)