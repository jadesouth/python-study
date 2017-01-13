import random

class People(object):

    location = [0, 0]

    def __init__(self):
        self.location = [random.randint(0, 9), random.randint(0, 9)]

    def move(self):
        self.location = [random.randint(0, 9), random.randint(0, 9)]

