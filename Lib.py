#-*- coding:utf-8 _*-
"""
@author:hql
@file: Lib
@time: 2018/08/{DAY}
"""
"""
物理基础运算库
"""
from Vector import Vector

def VectorCollision( m1 ,v1 ,m2 ,v2 ):
    m12 =  m1-m2
    mv2 = 2*m2*v2
    mv1 = 2*m1*v1
    x = (m12*v1+mv2)//(m1+m2)
    y = (-m12 * v2 + mv1) // (m1 + m2)
    return x,y

if __name__ == "__main__":
    m1 = 1
    m2 = 1
    v1 = Vector(100,0)
    v2 = Vector(0,100)

    print(VectorCollision(1000000000,v1,m2,v2))