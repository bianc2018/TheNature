#-*- coding:utf-8 _*-
"""
@author:Administrator
@file: terminal.py.py
@time: 2018/08/{DAY}
"""
import cv2 as cv
import numpy as np
# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc",size = 14)
class Terminal:
    def __init__(self,title = 'terminal',h=512,w=512,fil=255):
        self.h = h
        self.w = w
        self.fil = 255
        self.bg = np.zeros((self.h, self.w, 3), np.uint8)
        self.bg.fill(self.fil)
        self.title = title
        cv.namedWindow(self.title)
        pass
    def updata(self):
        cv.imshow(self.title, self.bg)
    def clear(self):
        self.bg = np.zeros((self.h, self.w, 3), np.uint8)
        self.bg.fill(self.fil)
        self.updata()
    def putText(self,text,pos):
        cv.putText(self.bg, text, pos,cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    """
        def vline(self,b,e,rbg,w):
        vec = Vector(e[0]-b[0],e[1]-b[1])
        dist = float(vec)
        vec.normalize()
        begin = Vector(b.x,b.y)
        cv.line(self.bg, b, e, rbg,w)
    """
    def close(self):
        cv.waitKey(0)
        cv.destroyAllWindows()
#全局变量
tm = Terminal()
if __name__ == "__main__":
    t = Terminal()
    t.updata()
    while True:
        print(cv.waitKey(0))
    t.close()
