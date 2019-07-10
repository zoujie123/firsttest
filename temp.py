# -*- coding: utf-8 -*-
import cv2
import random
import numpy as np


#打开一张图片，读入灰度图
image_gray=cv2.imread("C:/Users/Administrator/Desktop/1.jpg",0)
#显示图像
'''
cv2.imshow('horse',image_gray)

key=cv2.waitkey(0)
if key==27:
    cv2.destroyAllWindows()
'''

#获得图像的值类型
print(image_gray.dtype)

#获得图像矩阵的高宽
height,width=image_gray.shape


#显示彩色图像
image=cv2.imread("C:/Users/Administrator/Desktop/2.jpg")
'''
cv2.imshow('horse_3',image)
'''

#获得图像尺寸
print(image.shape)

#图像切片
image_crop=image_gray[0:10,0:10]
cv2.imshow('crop',image_crop)

#图像通道分离
R,G,B=cv2.split(image)
cv2.imshow('R',R)
cv2.imshow('G',G)
cv2.imshow('B',B)

#改变颜色值
def random_color(image):
    R,G,B=cv2.split(image)
    
    #r通道
    r_change=random.randint(-20,20)
    if r_change==0:
        pass
    elif r_change>0:
        l=255-r_change
        R[R>l]=255
        R[R<=l]=(r_change+R[R<=l]).astype(image.dtype)
    else:
        l=0-r_change
        R[R>l]=0
        R[R<=l]=(r_change+R[R<=l]).astype(image.dtype)
      
    #g通道
    g_change=random.randint(-20,20)
    if g_change==0:
        pass
    elif g_change>0:
        l=255-g_change
        G[G>l]=255
        G[G<=l]=(g_change+G[G<=l]).astype(image.dtype)
    else:
        l=0-g_change
        G[G>l]=0
        G[R<=l]=(g_change+G[G<=l]).astype(image.dtype)
    
    #b通道
    b_change=random.randint(-20,20)
    if b_change==0:
        pass
    elif b_change>0:
        l=255-b_change
        B[B>l]=255
        B[B<=l]=(b_change+B[B<=l]).astype(image.dtype)
    else:
        l=0-b_change
        B[B>l]=0
        B[B<=l]=(b_change+B[B<=l]).astype(image.dtype)
        
    #
    image_new=cv2.merge(R,G,B)
    return image_new

#调用颜色改变函数
image_change_color=random_color(image)
cv2.imshow('image_change_color',image_change_color)

#图像旋转
image=cv2.imread("C:/Users/Administrator/Desktop/2.jpg",0)
rotation=cv2.getRotationMatrix2D((image.shape[1]/2,image.shape[0]/2),60,1)#参数分别为图像宽高、旋转角度、尺度
image_rotate=cv2.warpAffine(image,rotation,(image.shape[1],image.shape[0]))
cv2.imshow('image_rotate',image_rotate)

#映射变换
def random_warp(image):
    height,width,t=image.shape
    
    random_m=20
    x1=random.randint(-random_m,random_m)
    y1=random.randint(-random_m,random_m)
    
    x2=random.randint(width-random_m-1,width-1)
    y2=random.randint(-random_m,random_m)
    
    x3=random.randint(width-random_m-1,width-1)
    y3=random.randint(height-random_m-1,height-1)
    
    x4=random.randint(-random_m,random_m)
    y4=random.randint(height-random_m-1,height-1)
    
    x11=random.randint(-random_m,random_m)
    y11=random.randint(-random_m,random_m)
    
    x22=random.randint(width-random_m-1,width-1)
    y22=random.randint(-random_m,random_m)
    
    x33=random.randint(width-random_m-1,width-1)
    y33=random.randint(height-random_m-1,height-1)
    
    x44=random.randint(-random_m,random_m)
    y44=random.randint(height-random_m-1,height-1)
    
    ps1=np.float16([x1,y1],[x2,y2],[x3,y3],[x4,y4])
    ps2=np.float16([x11,y11],[x22,y22],[x33,y33],[x44,y44])
    
    w=cv2.getPerspectiveTransform(ps1,ps2)
    image_warp=cv2.warpPerspective(image,w,image.shape)
    
    return w,image_warp

#旋转映射
w,image_warp=random_warp(image)
cv2.imshow('perspective_image',image_warp)


    