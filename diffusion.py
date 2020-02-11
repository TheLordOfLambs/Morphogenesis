# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.signal import convolve2d
import time

def fill(B,centre,radius) :
    
    for x in range(B.shape[0]) :
        for y in range(B.shape[1]) :
            
            if (x-centre[0])**2 + (y-centre[1])**2 <= radius**2 :
                B[x][y] = 1
                
                
    return B

def remove(B,centre,radius) :
    
    for x in range(B.shape[0]) :
        for y in range(B.shape[1]) :
            
            if (x-centre[0])**2 + (y-centre[1])**2 <= radius**2 :
                B[x][y] = 0
                
                
    return B
    

plt.close('all')

h = 500#480
H = 1500#720

D_A = 1                            # diffusion rate chimical A
D_B = 0.5                           # diffusion rate chimical B
f = 0.0545                           # feeding rate chimical A
k = 0.062                           # killing rate chimical B
dt = 1                               # time steps in sec
maxiter = 5000                        # iterations nubers
screen_rate = 100

'''
A = np.ones((h,H))
B = np.zeros((h,H))

B = fill(B,(250,750),20)
'''

laplace_filter = filt = np.array([[0.05,0.2,0.05],
                                  [0.2,-1,0.2],
                                  [0.05,0.2,0.05]])
'''
plt.figure(1)
plt.imshow(B)
plt.title("t = 0 sec")
plt.show()
'''
j=0
for i in tqdm(range(maxiter)) :
    
    lapA = convolve2d(A,laplace_filter,mode='same', boundary='symm')
    lapB = convolve2d(B,laplace_filter,mode='same', boundary='symm')
    
    A = A + dt*(D_A*lapA-A*B*B+f*(1-A))
    B = B + dt*(D_B*lapB+A*B*B-(k+f)*B)
    '''
    if i%50 == 0 :
        
        plt.imsave("{}.png".format(str(j).zfill(5)),B)
        j += 1
        
    '''
'''
    if  i%screen_rate == 0 :
        time.sleep(0.1)
        plt.figure(1)
        plt.title("t = {} sec".format(i*dt))
        plt.imshow(B)
        plt.show()
        plt.pause(0.1)

'''
plt.figure(1)
plt.imshow(B,cmap='jet')
plt.title("t = {} sec".format(maxiter*dt))
plt.show()

