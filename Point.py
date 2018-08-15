#-*- coding:utf-8 _*-
"""
@author:hql
@file: Point.py
@time: 2018/08/{DAY}
"""
import cv2 as cv
class Point:
    def __init__(self,x,y,w=1,rgb = (0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.rgb = rgb
    def pos(self):
        return (self.x,self.y)

