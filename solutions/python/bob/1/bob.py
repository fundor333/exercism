import re

def response(hey_bob):
    regex = re.compile('[^a-zA-Z?,]')
    hey_bob = regex.sub('', hey_bob)
    if len(hey_bob)==0:
        return "Fine. Be that way!"
    if hey_bob.isupper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!"
    if "?" == hey_bob[-1]:
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."