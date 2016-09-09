
# coding: utf-8

# In[1]:

import numpy as np
from scipy import ndimage

import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter as ga


# In[2]:

def pol2cart(r,theta):
    temp = np.multiply(r,np.exp(np.multiply(1j,theta)))
    return temp.real, temp.imag
    
def cart2pol(x,y):
    r = np.sqrt(np.power(x,2) + np.power(y,2))
    theta = np.arctan2(y, x)
    return r, theta


# In[3]:

scores = np.array([6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10])


# In[9]:

sectors = np.arange(-np.pi/20, np.pi*2+np.pi/20, np.pi/10) + np.pi/2


# In[10]:

inner_bullseye_diam = 12.7
outer_bullseye_diam = 31.8

inner_triple_diam = 194.8
outer_triple_diam = 214.8

inner_double_diam = 320.0
outer_double_diam = 340.0


# In[21]:

dartboard = np.zeros([341,341])

r,theta = np.meshgrid(np.linspace(0,inner_bullseye_diam/2,inner_bullseye_diam*10/2),
                      np.linspace(0,np.pi*2+.2,inner_bullseye_diam*10/2))

x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = 50

r,theta = np.meshgrid(np.linspace(inner_bullseye_diam/2,outer_bullseye_diam/2,100),
                      np.linspace(0,np.pi*2+.2,100))
x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = 25

for i in np.arange(0,20):
    r,theta = np.meshgrid(np.linspace(outer_bullseye_diam/2,outer_double_diam/2,1500),
                          np.linspace(sectors[i],sectors[i+1],1500))
    x,y = np.round(pol2cart(r,theta)).astype(int)+ np.round(dartboard.shape[1]/2).astype(int)
    dartboard[x,y] = scores[i]
    


# In[22]:


r,theta = np.meshgrid(np.linspace(inner_triple_diam/2,outer_triple_diam/2,inner_triple_diam*10/2),
                      np.linspace(0,np.pi*2+.2,inner_triple_diam*10/2))

x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = dartboard[x,y]*3

r,theta = np.meshgrid(np.linspace(inner_double_diam/2,outer_double_diam/2,1500),
                      np.linspace(0,np.pi*2+.2,1500))

x,y = np.round(pol2cart(r,theta)).astype(int) + np.round(dartboard.shape[1]/2).astype(int)
dartboard[x,y] = dartboard[x,y]*2


# In[ ]:




# In[ ]:




# In[57]:

theta*180/np.pi


# In[ ]:




# In[23]:



##fig = plt.figure(figsize=(10,10))
##axes = fig.add_subplot(111)
plt.imshow(dartboard)
plt.colorbar()
plt.show()
##dartboard[0:500,0:500] = 0
##plt.imshow(dartboard2,alpha=.8)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[114]:

##dartboard[dartboard==0] = np.nan
test = ga(dartboard,30,mode='constant')
test[test<1.5] = np.nan


# In[103]:




# In[96]:

fig = plt.figure(figsize=(10,10))
axes = fig.add_subplot(111)
axes.imshow(test)
plt.show()


# In[115]:

dat = plt.imread('dartboard.png')
dat_small = dat[::4,::4,::1]
h = plt.imshow(dat_small,extent=[0,730,0,730],origin='upper')
h.axes.set_xlim(0,730)
h.axes.set_ylim(0,730)
g = plt.imshow(np.flipud(test),alpha=.7,origin='lower',extent=[140,590,140,590],cmap='nipy_spectral')
plt.colorbar()
plt.show()


# In[56]:

dat_small = dat[::4,::4,::1]


# In[85]:

test.shape


# In[ ]:



