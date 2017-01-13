import random

class Arm(object):

    def shoot(self):
        return [[random.randint(0, 9), random.randint(0, 9)]]
