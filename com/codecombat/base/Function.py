from com.codecombat.base import Self
from pip._vendor.distlib._backport.shutil import move


self = Self()


def isRange(target, dis):
    if target:
        if self.distanceTo(target) < dis:
            return True
    return False

def closeOrAttack(target, dis):
    if target:
        if isRange(target, dis):
            self.attack(target)
        else:
            closeTarget(target)
            
            
def closeTarget(target):
    if target:
        x = self.pos.x
        y = self.pos.y
        tx = target.pos.x
        ty = target.pos.y
        
        x += (tx - x) / 3
        y += (ty - y) / 3
        
        self.moveXY(x, y)
        
def cleveEnemy(dis=20,count = 6):
    nowCount = 0
    enemiey = self.findEnemies()
    
    for en in enemiey:
        if isRange(en , dis):
            nowCount += 1

    if nowCount > count:
        if self.isReady("cleave"):
            self.cleave()
            return True
    return False

def nearestEnemy():
    return self.findNearest(self.findEnemies())

def cleveOrAttack(dis = 7,count = 6):
    
    
    
        if not cleveEnemy():
            closeOrAttack(dis, count)

def flagAndPick(color="green"):
    flag = self.findFlag(color)
    if flag:
        self.pickUpFlag(flag)
        return True
    return False
