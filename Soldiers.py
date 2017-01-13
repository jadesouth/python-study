# -*- encoding=utf-8 -*-
import random

import People

class Soldiers(People):

    kind = '' # 士兵种类[friend, enemy]
    weapons = '' # 士兵拥有的武器
    allWeapons = ['pistol', 'machineGun'] # 所有武器种类[pistol, machineGun]

    def __init__(self, kind):
        self.kind = kind
        random.shuffle(self.allWeapons)
        arms = self.allWeapons.pop()
        if 'pistol' == arms:
            self.weapons = Pistol()
        elif 'machineGun' == arms:
            self.weapons = MachineGun()
        super(Soldiers, self).__init(self)

    def attack(self):
        return self.weapons.shoot()

