import re


def is_isogram(string):
    string = re.sub("[^a-zA-Z]+", "", string)
    return len(string) == len(set(string.lower()))