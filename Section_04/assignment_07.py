# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:

def string_match(s1,s2):
    n = min(len(s1), len(s2))
    c= 0
    for i in range(n-2):
        if s1[i:i+2] == s2[i:i+2]:
            c+=1
    return c

print(string_match('xxcaazz', 'xxbaaz'))

