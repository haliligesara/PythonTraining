# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

def grow_string(s):
    ns = ''
    for i in range(0,len(s)):
        ns += s[0:i]
    return ns+s


print(grow_string('ab'))

