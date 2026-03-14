# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:
l = [1,2,3,4,5,6,7]
s = 'in the end everything will be okay'

def multi_merge(l, s):
    res = l + s.split() + list(s)
    return res

print(multi_merge(l,s))






































# Solution:

# def multi_merge(list_a, str):
#     return list_a + str.split() + list(str)
#
# print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
