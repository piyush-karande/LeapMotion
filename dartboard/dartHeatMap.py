import numpy as np

import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter as ga

# Function to convert polar coordinates to cartesian
def pol2cart(r,theta):
    temp = np.multiply(r,np.exp(np.multiply(1j,theta)))
    return temp.real, temp.imag

# Defining dartboard parameters

scores = np.array([6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10])
sectors = np.arange(-np.pi/20, np.pi*2+np.pi/20, np.pi/10) + np.pi/2

inner_bullseye_diam = 12.7
outer_bullseye_diam = 31.8

inner_triple_diam = 194.8
outer_triple_diam = 214.8

inner_double_diam = 320.0
outer_double_diam = 340.0

# Initializing dartboard as a matrix

dartboard = np.zeros([341,341])

# Setting the scores for inner bullseye
r,theta = np.meshgrid(np.linspace(0,inner_bullseye_diam/2,inner_bullseye_diam*10/2),
                      np.linspace(0,np.pi*2+.2,inner_bullseye_diam*10/2))

x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = 50

# Setting the scores for inner bullseye
r,theta = np.meshgrid(np.linspace(inner_bullseye_diam/2,outer_bullseye_diam/2,100),
                      np.linspace(0,np.pi*2+.2,100))
x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = 25

# Setting the scores for individual sectors
for i in np.arange(0,20):
    r,theta = np.meshgrid(np.linspace(outer_bullseye_diam/2,outer_double_diam/2,1500),
                          np.linspace(sectors[i],sectors[i+1],1500))
    x,y = np.round(pol2cart(r,theta)).astype(int)+ np.round(dartboard.shape[1]/2).astype(int)
    dartboard[x,y] = scores[i]

# Setting the scores for triple ring
r,theta = np.meshgrid(np.linspace(inner_triple_diam/2,outer_triple_diam/2,inner_triple_diam*10/2),
                      np.linspace(0,np.pi*2+.2,inner_triple_diam*10/2))

x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = dartboard[x,y]*3

# Setting the scores for double ring
r,theta = np.meshgrid(np.linspace(inner_double_diam/2,outer_double_diam/2,1500),
                      np.linspace(0,np.pi*2+.2,1500))

x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = dartboard[x,y]*2

# Applying the Sperical Ditribution of dart throws
# at each points with standard deviation 30mm
heatmap = ga(dartboard,30,mode='constant')

# Ignoring small values outside the dartboard
heatmap[heatmap<1.5] = np.nan

# Plotting image and overlaying with heatmap

dat = plt.imread('dartboard.png')
dat_small = dat[::4,::4,::1]
h = plt.imshow(dat_small,extent=[0,730,0,730],origin='upper')
h.axes.set_xlim(0,730)
h.axes.set_ylim(0,730)
g = plt.imshow(np.flipud(heatmap),alpha=.7,origin='lower',extent=[140,590,140,590],cmap='nipy_spectral')
plt.colorbar()
plt.show()
