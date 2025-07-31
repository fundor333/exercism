import re


def is_pangram(sentence):
    temp = set(re.sub("[^a-zA-Z]+", "", sentence.lower()))
    return len(temp) == 26