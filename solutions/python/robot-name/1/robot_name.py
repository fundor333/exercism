import random
import string
from random import randint

ROBOTS_NAMES = set()


class Robot(object):
    def __init__(self):
        self.generate_name()

    def generate_name(self):
        flag = True
        name = ""
        while flag:
            name = ""
            name += random.choice(string.ascii_uppercase)
            name += random.choice(string.ascii_uppercase)
            name += str(randint(100, 999))
            if name not in ROBOTS_NAMES:
                flag = False
        self.name = name
        ROBOTS_NAMES.add(name)

    def reset(self):
        name = self.name
        self.generate_name()
        ROBOTS_NAMES.remove(name)
