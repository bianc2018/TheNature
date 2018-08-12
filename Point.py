#-*- coding:utf-8 _*-
"""
@author:hql
@file: Point.py
@time: 2018/08/{DAY}
"""
import cv2 as cv
from terminal import tm
class Point:
    def __init__(self,x,y,w=1,rgb = (0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.rgb = rgb
    def pos(self):
        return (self.x,self.y)
    def filp(self):
        cv.circle(tm.bg,(int(self.x),int(self.y)),self.w,self.rgb,-1)
        tm.updata()
    def display(self):
        cv.circle(tm.bg,(int(self.x),int(self.y)),self.w,self.rgb,-1)
import random

class Walker(Point):
    def __init__(self,x = int(tm.w/2),y= int(tm.h/2)):
        super(Walker,self).__init__(x,y)
        pass
    def step(self):
        sx = random.randint(-1,1)
        sy = random.randint(-1,1)
        self.x +=sx
        self.y +=sy
        if self.x <0:
            self.x=0
        if self.x>tm.w:
            self.x = tm.w
        if self.y <0:
            self.y=0
        if self.y>tm.h:
            self.y = tm.h


if __name__ == "__main__":
    p = Walker()
    while True:
        p.step()
        p.display()
        print(p.pos())
        if cv.waitKey(1) == 'q':
            break
    tm.close()

