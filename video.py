# -*- coding: utf-8 -*-


import cv2
import glob

fps = 25 #frames per seconds
 
img_array = []
for filename in glob.glob('Images/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
