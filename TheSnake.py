#-*- coding:utf-8 _*-
"""
@author:hql
@file: TheSnake
@time: 2018/08/{DAY}
"""
from terminal import tm
from Point import Point
import random
from copy import deepcopy

class Snake:
    body = list()
    fps = 20 #p/s
    asp = '8' # 2 y++ 4 x-- 6 x++ 8 y--
    w = 5
    speed = 1 # 1 pi/ms
    def __init__(self,bseep = 1,size = 5,w=5,fps=50,basp = 2):
        self.fps = fps
        self.speed = bseep
        self.w = w
        self.asp = basp
        bx = random.randint(0, tm.w)
        by = random.randint(0, tm.h)
        for  i in range(0,size):
            p = Point(bx+i*w,by+i*w,self.w)
            self.body.append(deepcopy(p))
        pass
    def Change(self,key):
        print(key)
        self.asp = key
    def __dist(self,p1,p2):
        return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    def MoveBody(self,p,d):
        if self.asp == '2':
            p.y+=d
            if p.y>tm.h:
                p.y=0
        elif self.asp == '4':
            p.x-=d
            if p.x<0:
                p.x = tm.w
        elif self.asp == '6':
            p.x+=d
            if p.x>tm.w:
                p.x = 0
        elif self.asp == '8':
            p.y-=d
            if p.y<0:
                p.y = tm.h
        else:
            print(self.asp)
            self.asp = '2'
        return p
    def Move(self,t):
        size = len(self.body)
        node = 1
        head = self.body[-1]
        print(node)
        #print(size,node,head.pos())
        for i in range(0,node):
            head = self.MoveBody(head,self.w)
            #print("add",head.pos())
            self.body.append(deepcopy(head))

        self.body = self.body[node:]

    def Eat(self,p):
        head = self.body[-1]
        if self.__dist(p.pos(),head.pos())<self.w*2:
            self.body.append(p)
            return 1
        return 0
    def display(self):
        size = len(self.body)
        i = size -1
        while i>=0:
            self.body[i].display()
            i-=1
"""
import time

time_start=time.time()
time_end=time.time()
print('totally cost',time_end-time_start)
"""
import time
import cv2 as cv
def GetPoint(w):
    bx = random.randint(0, tm.w)
    by = random.randint(0, tm.h)
    return Point(bx, by, w)

if __name__ == "__main__":
    snake = Snake()
    food = GetPoint(snake.w)

    while True:
        tm.clear()

        snake.display()
        food.display()
        tm.putText(f"size:{len(snake.body)}", (0, 50))

        tm.updata()
        snake.Move(0)
        if snake.Eat(food)==1:
            food = GetPoint(snake.w)
        time.sleep(0.1)
        c = cv.waitKey(50)
        if c==-1:
            continue
        elif c == 113:
            break
        elif chr(c) in ['2','4','6','8']:
            snake.Change(chr(c))

    tm.close()