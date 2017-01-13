# -*- encoding=utf-8 -*-
from random import randint

import Soldiers

class Map(object):

    friends = []
    enemies = []

    def __init__(self):
        for i in range(0, 4):
            self.friends.append(Soldiers('friend'))
            self.enemies.append(Soldiers('enemy'))

    def begin(self):
        while 0 >= len(self.friends) or 0 >= len(self.enemies):
            # 敌人射击
            for i in self.enemies:
                point = self.enemies[i].attack()
                for j in self.friends:
                    if self.friends[j].location[0] == point[0] and self.friends[j].location[1] == point[1]:
                        deathFriends.append(j)
                        print "#%d Friend death."

            # 友军射击
            for i in self.friends:
                point = self.friends[i].attack()
                for j in self.enemies:
                    if self.enemies[j].location[0] == point[0] and self.enemies[j].location[1] == point[1]:
                        deathEnemies.append(j)
                        print "#%d Enemiy death."

            # 剔除死亡的士兵 
            for i in deathFriends:
                del self.friends[deathFriends[i]]
            for i in deathEnemies:
                del self.Enemiies[deathEnemies[i]]

        if 0 < len(self.friends):
            print "Friends Win!!!"
        if 0 < len(self.enemies):
            print "Friends Lost!!!"

