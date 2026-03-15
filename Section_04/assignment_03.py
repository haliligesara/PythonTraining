# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# Your Code Below:

def f_sequence(l):
    for i in range(len(l)-2):
        if l[i] == 1 and l[i + 1] == 2 and l[i + 2] == 3:
            return True
    return False

l = []
print(f_sequence(l))