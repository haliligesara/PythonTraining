# Assignment 3:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable will contain only 4 characters

    Example:
    ---------------
    chars = "<<>>"
    word = "hello"
    result - should contain the following string: <<hello>>

"""

chars = "[[]]"
word = "Cool"

# Expected Result Printed: [[Cool]]

# Your code below:

def move_middle(string1, string2):
    result = string1[0:len(string1)//2] + string2 + string1[len(string1)//2:]
    return result

print(move_middle(chars, word))































# Solution Below:
# print(chars[:2] + word + chars[2:])


