#!/usr/bin/python3
"""
"5-test_indentation" module.
"""


def text_indentation(text):
    """split a text into lines along "?", ":", "." + 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
