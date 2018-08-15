#-*- coding:utf-8 _*-
"""
@author:hql
@file: Vector
@time: 2018/08/{DAY}
"""
"""
__cmp__(self, other)：定义了所有比较操作符的行为。应该在 self < other 时返回一个负整数，在 self == other 时返回0，在 self > other 时返回正整数。
__eq__(self, other)：定义等于操作符(==)的行为。
__ne__(self, other)：定义不等于操作符(!=)的行为(定义了 eq 的情况下也必须再定义 ne!)
__le__(self, other)：定义小于等于操作符(<)的行为。
__ge__(self, other)：定义大于等于操作符(>)的行为。
数值操作符

__pos__(self) 实现取正操作，例如 +some_object
__invert__(self) 实现取反操作符 ~
__add__(self, other) 实现加法操作
__sub__(self, other) 实现减法操作
__radd__(self, other) 实现反射加法操作
__rsub__(self, other) 实现反射减法操作
__floordiv__(self, other) 实现使用 // 操作符的整数除法
__iadd__(self, other) 实现加法赋值操作。
__isub__(self, other) 实现减法赋值操作。
__int__(self) 实现到int的类型转换。
__long__(self) 实现到long的类型转换。
"""
import math
import cv2 as cv
import random
class Vector:
    """
    向量类（x,y）
    """
    x=0
    y=0
    def __init__(self,x=None,y=None):
        if x==None or y==None:
            self.x,self.y = self.Random()
        else:
            self.x =  x
            self.y =  y
    def Random(self,rx1=0,rx2= 50,ry1=0,ry2=50):
        return random.randint(rx1,rx2),random.randint(ry1,ry2)
    #向量加减
    def __add__(self, vec):
        return Vector(self.x+vec.x,self.y+vec.y)
    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)
    #向量乘除
    def __floordiv__(self, vec):
        return Vector(self.x/vec,self.y/vec)
    def __mul__(self, vec):
        if type(vec) == Vector:
            return self.dot(vec)
        else:
            return Vector(self.x*vec,self.y*vec)
    def __rmul__(self, other):
        return self.__mul__(other)
    #向量点乘
    def dot(self,vec):
        return self.x*vec.x+self.y*vec.y
    #取反 ~
    def __invert__(self):
        return Vector(-self.x,-self.y)
    #数值
    #长度
    def mag(self):
        return (self.x**2+self.y**2)**0.5
    #向量的方向
    def heading2D(self):
        """
                math.degrees(x) # 将 弧度 转换为 角度, 如 degrees(math.pi/2) ， 返回90.0
                math.radians(x) # 将 角度 转换为 弧度
        """
        if self.x==0:
            if self.y>=0:
                return math.pi
            else:
                return -math.pi
        at = self.y/self.x
        return math.atan(at)
    #夹角方向
    def angle(self,vec):
        """
        dot = |self||vec|cosa
        :param vec:
        :return:
        """
        dot = self*vec
        sm = self.mag()
        vm = vec.mag()
        return math.acos(dot/(sm*vm))
    #向量单位化
    def normalize(self):
        d = self.mag()
        if d == 0:
            return self
        return self//d
    #输出
    def pos(self):
        return (self.x,self.y)
    def __int__(self):
        return int(self.mag())
    def __float__(self):
        return self.mag()
    def __str__(self):
        return f"<{self.x},{self.y}>"
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __getitem__(self, item):
        return self.__dict__[item]
    #画图

def vc( m1 ,v1 ,m2 ,v2 ):
    m12 =  m1-m2
    mv2 = 2*m2*v2
    mv1 = 2*m1*v1
    x = (m12*v1+mv2)//(m1+m2)
    y = (-m12 * v2 + mv1) // (m1 + m2)
    return x,y

if __name__ == "__main__":
    v1 = Vector(10,-2)
    print(~v1)