#-*- coding:utf-8 _*-
"""
@author:hql
@file: TheBox2D
@time: 2018/08/{DAY}
"""
from Point import Point
from Vector import  Vector
from Lib import VectorCollision

class BaseObj:
    def __init__(self,shape,x=None,y=None,vx=None,vy=None,w=1,random = False):
        if random:
            self.loc = Vector()
            self.v = Vector()
        else:
            self.loc = Vector(x, y)
            self.v = Vector(vx, vy)
        self.w = w
        self.shape = shape
    def E(self):
        return 0.5 * self.w * (self.v.mag()**2)
    def Move(self,t=1):
        self.loc = self.loc+self.v
    def Stress(self,f,t=1):
        """
        f = ma
        a = f/m
        v = at
        :param f:
        :param t:
        :return:
        """
        #print(f)
        self.v = self.v + (f//self.w)*t
        if self.v.mag()<1:
            self.v = self.v*0

    def __str__(self):
        return f"w:{self.w},loc:{self.loc},v:{self.v}"

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow
from PyQt5.QtCore import Qt,QBasicTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import random
from Shape import  Shape
class Box2D(QMainWindow):
    """
    创建一个2d盒子，存在物品进行移动 ，实现物体间的物理碰撞
    """
    def __init__(self,width=500,height=500,dfps = 100,objnum = 5):
        super().__init__()
        self.width = width
        self.height = height
        self.dfps = dfps
        self.objlist = []
        self.time = 0
        shape = Shape('circle',radius=20)
        for i in range(0,objnum):
            self.objlist.append(BaseObj(shape,random=True))
        self.initUI()

    def initAccessory(self):
        self.timer = QBasicTimer()
        self.timer.start(self.dfps, self)

        self.label =  QLabel("e:"+str(self.E()),self)
    def initUI(self):
        self.initAccessory()
        self.setGeometry(300, 300, self.width, self.height)
        self.setWindowTitle('BOX2D')
        self.show()
    def E(self):
        e = 0
        for obj in self.objlist:
            e+=obj.E()
        return e
    def Friction(self,m,v):
        g = 9.8
        u = 0.2
        c=~(v.normalize()) #方向
        return u*m*g*c

    def timerEvent(self, e):
        self.time+=1
        size = len(self.objlist)
        for i in range(0,size):
            self.objlist[i].Stress(self.Friction(self.objlist[i].w,self.objlist[i].v))
            for j in range(i+1,size):
                if self.objlist[i].shape.hit(self.objlist[i].loc,self.objlist[j].loc,self.objlist[j].shape):
                    print("hit",self.objlist[i],self.objlist[j])
                    self.objlist[i].v,self.objlist[j].v = VectorCollision(self.objlist[i].w,self.objlist[i].v,self.objlist[j].w,self.objlist[j].v)

            self.objlist[i].Move()
            self.hit(self.objlist[i])
        print(f"v={self.objlist[0]}")
        self.label.setText(f"e:{int(self.E())},time:{self.time}")
        self.label.adjustSize()
        self.repaint()

       # QApplication.processEvents()
    def hit(self,obj):
        pos = obj.loc

        if pos['x'] <10:
            obj.loc['x'] = 0
            obj.v['x'] = -obj.v['x']
        elif pos['x']>self.width-10:
            obj.loc['x'] = self.width
            obj.v['x'] = -obj.v['x']

        if pos['y'] <10:
            obj.loc['y'] = 0
            obj.v['y'] = -obj.v['y']
        elif pos['y']>self.height-10:
            obj.loc['y'] = self.height
            obj.v['y'] = -obj.v['y']

    def paintEvent(self,e):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setPen(Qt.red)
        r = 10
        for obj in self.objlist:
            obj.shape.draw(qp,obj.loc)
import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = Box2D()
    sys.exit(app.exec_())