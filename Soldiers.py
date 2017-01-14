# -*- encoding=utf-8 -*-
import random

import People
import MachineGun
import Pistol

class Soldiers(People.People):

    kind = '' # 士兵种类[friend, enemy]
    weapons = '' # 士兵拥有的武器

    def __init__(self, kind):
	self.allWeapons = ['pistol', 'machineGun'] # 所有武器种类[pistol, machineGun]
        self.kind = kind
        random.shuffle(self.allWeapons)
        arms = self.allWeapons.pop()
        if 'pistol' == arms:
            self.weapons = Pistol.Pistol()
        elif 'machineGun' == arms:
            self.weapons = MachineGun.MachineGun()
        super(Soldiers, self).__init__()

    def attack(self):
        return self.weapons.shoot()

