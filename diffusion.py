# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:12:52 2020

@author: Angelo Charry
"""

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.signal import convolve2d


def fill(B,centre,radius) :
    """
    This fonction add a chemical with a circular distribution
    """
    
    for x in range(B.shape[0]) :
        for y in range(B.shape[1]) :
            
            if (x-centre[0])**2 + (y-centre[1])**2 <= radius**2 :
                B[x][y] = 1
                
                
    return B

def remove(B,centre,radius) :
    """
    This fonction remove a chemical with a circular distribution
    """
    
    for x in range(B.shape[0]) :
        for y in range(B.shape[1]) :
            
            if (x-centre[0])**2 + (y-centre[1])**2 <= radius**2 :
                B[x][y] = 0
                
                
    return B
    

plt.close('all')

h = 480                            # hauteur
l = 720                            # largeur

D_A = 1                            # diffusion rate chimical A
D_B = 0.5                           # diffusion rate chimical B
f = 0.0545                           # feeding rate chimical A
k = 0.062                           # killing rate chimical B
dt = 1                               # time steps in sec
maxiter = 60                        # iterations nubers
screen_rate = 1                      # rate of images saving
image_path = "Images/"              # where the images will be saved




# initializing the grid
A = np.ones((h,l))
B = np.zeros((h,l))

B = fill(B,(240,360),10) # filling the grid with chemical B


laplace_filter = filt = np.array([[0.05,0.2,0.05],
                                  [0.2,-1,0.2],
                                  [0.05,0.2,0.05]])

plt.figure(1)
plt.imshow(B)
plt.title("t = 0 sec")
plt.show()

j=0
for i in tqdm(range(maxiter)) :
    
    lapA = convolve2d(A,laplace_filter,mode='same', boundary='symm')
    lapB = convolve2d(B,laplace_filter,mode='same', boundary='symm')
    
    A = A + dt*(D_A*lapA-A*B*B+f*(1-A))
    B = B + dt*(D_B*lapB+A*B*B-(k+f)*B)
    
    if i%screen_rate == 0 :
        
        try :
            plt.imsave(image_path+"{}.png".format(str(j).zfill(5)),B) #saving the image
            j += 1
        except FileNotFoundError:
            os.mkdir("Images/")
            plt.imsave(image_path+"{}.png".format(str(j).zfill(5)),B) #saving the image
            j += 1
            
        

