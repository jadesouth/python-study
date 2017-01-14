# -*- encoding=utf-8 -*-
from random import randint

import Soldiers

class Map(object):

    friends = []
    enemies = []
    deathFriends = []
    deathEnemies = []

    def __init__(self):
        for i in range(0, 4):
            self.friends.append(Soldiers.Soldiers('friend'))
            self.enemies.append(Soldiers.Soldiers('enemy'))

    def begin(self):
        while 0 < len(self.friends) and 0 < len(self.enemies):
	    print '-' * 20
	    print 'len friends: ', len(self.friends)
	    print 'len enemies: ', len(self.enemies)
            # 敌人射击
            for i in range(0, len(self.enemies) - 1):
		self.deathFriends = []
		self.deathEnemies = []
		#print 'into for enemies'
                point = self.enemies[i].attack()
		#print "point: ", point
                for j in range(0, len(self.friends) - 1):
		    print 'friend location: ', self.friends[j].location
		    for pnt in point:
			print 'enemie shoot: ', pnt
			if self.friends[j].location[0] == pnt[0] and self.friends[j].location[1] == pnt[1]:
			    self.deathFriends.append(j)
			    print "#%d Friend death." % j
			

            # 友军射击
            for i in range(0, len(self.friends) - 1):
                point = self.friends[i].attack()
                for j in range(0, len(self.enemies) - 1):
		    print 'enemies location: ', self.enemies[j].location
		    for pnt in point:
			print 'friend shoot: ', pnt
			if self.enemies[j].location[0] == pnt[0] and self.enemies[j].location[1] == pnt[1]:
			    self.deathEnemies.append(j)
			    print "#%d Enemiy death." % j


	    #print self.deathFriends
	    #print self.deathEnemies
	    #print len(self.deathFriends)
	    #print len(self.deathEnemies)
            # 剔除死亡的士兵 
            for i in range(0, len(self.deathFriends) - 1):
		print 'del %d friends: ' % i
                del self.friends[self.deathFriends[i]]
            for i in range(0, len(self.deathEnemies) - 1):
		print 'del %d enemies: ' % i
                del self.enemies[self.deathEnemies[i]]

        if 0 < len(self.friends):
            print "Friends Win!!!"
        if 0 < len(self.enemies):
            print "Friends Lost!!!"


map = Map()
map.begin()
