#-*- coding:utf-8 _*-
"""
@author:hql
@file: Shape
@time: 2018/08/{DAY}
"""
from Vector import  Vector
class Shape:
    def __init__(self,type,**argv):
        try:
            self.type = type
            if type == "circle":
                self.radius = argv['radius']
            elif type == "rect":
                self.width =argv['width']
                self.height = argv['height']
        except Exception as e:
            print("err",e)
    def draw(self,Painter,Vec):
        if self.type == 'circle':
            x = Vec['x'] - self.radius
            y = Vec['y'] - self.radius
            d = 2*self.radius
            Painter.drawEllipse(x,y,d,d)
    def hit(self,vec1,vec2,shape):
        dist = (vec1-vec2).mag()
        r2 = self.radius+shape.radius
        if dist <= r2:
            return True
        else :
            return False
        pass
    pass

if __name__ =="__main__":
    s = Shape("circle",radius=100)
    print(help(Shape))