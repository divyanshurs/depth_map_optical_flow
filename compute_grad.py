import numpy as np
import sys
#from scipy.ndimage import convolve
import scipy
from scipy import signal
from scipy.ndimage import convolve1d

from copy import deepcopy
"""
STUDENT CODE BEGINS
Define 1D filters as global variables.

"""
g = [0.015625, 0.093750, 0.234375, 0.312500, 0.234375, 0.093750, 0.015625]
h = [ 0.03125, 0.12500, 0.15625, 0, -0.15625, -0.1250, -0.03125]
# g = np.array(g).reshape((len(g),1))
# h = np.array(h).reshape((len(h),1))

def compute_Ix(imgs):
    """
    params:
        @imgs: np.array(h, w, N)
    return value:
        Ix: np.array(h, w, N)
    """
    
    """
    STUDENT CODE BEGINS
    """
    # num_imgs = imgs.shape[2]
    # img_dim = imgs.shape[0]
    # #print(h.shape)
    # new_imgs = deepcopy(imgs)
    # final_imgs = deepcopy(imgs)

    # # for i in range(num_imgs):
    # #     img_int = imgs[:,:,i]
    # #     C = scipy.signal.convolve2d(img_int, h, mode='same') #convolving h in x
    # #     D = scipy.signal.convolve2d(C.T, g, mode='same') #convolving g in y
    # #     new_imgs[:,:,i] = D.T

    # for i in range(num_imgs):
    #     img_int = imgs[:,:,i]
    #     C = scipy.signal.convolve2d(img_int.T, h, mode='same') #convolving h in x
    #     D = scipy.signal.convolve2d(C.T, g, mode='same') #convolving g in y
    #     new_imgs[:,:,i] = D
        
    
    # #convolving over time now
    # for j in range(img_dim):
    #     t_int = new_imgs[:,j,:]
    #     E = scipy.signal.convolve2d(t_int, g, mode='same') #convolving g in t
    #     final_imgs[:,j,:] = E

    new_imgs = convolve1d(imgs, h, axis=1)
    final_imgs = convolve1d(new_imgs, g, axis=0)
    Ix = convolve1d(final_imgs, g, axis=2)
    return Ix

def compute_Iy(imgs):
    """
    params:
        @imgs: np.array(h, w, N)
    return value:
        Iy: np.array(h, w, N)
    """
    """
    STUDENT CODE BEGINS
    """
    num_imgs = imgs.shape[2]
    img_dim = imgs.shape[0]
    #print(h.shape)
    new_imgs = deepcopy(imgs)
    final_imgs = deepcopy(imgs)

    # for i in range(num_imgs):
    #     img_int = imgs[:,:,i]
    #     img_int = img_int.T #T because I have to do y here
    #     C = scipy.signal.convolve2d(img_int, h, mode='same') #convolving h in y
    #     D = scipy.signal.convolve2d(C.T, g, mode='same') #convolving g in x
    #     new_imgs[:,:,i] = D #coz its already inverted twice

    # for i in range(num_imgs):
    #     img_int = imgs[:,:,i]
    #     #img_int = img_int.T #T because I have to do y here
    #     C = scipy.signal.convolve2d(img_int, h, mode='same') #convolving h in y
    #     D = scipy.signal.convolve2d(C.T, g, mode='same') #convolving g in x
    #     new_imgs[:,:,i] = D.T #coz its already inverted twice

        
    # #convolving over time now
    # for j in range(img_dim):
    #     t_int = new_imgs[:,j,:]
    #     E = scipy.signal.convolve2d(t_int, g, mode='same') #convolving g in t
    #     final_imgs[:,j,:] = E


    # Iy = final_imgs

    new_imgs = convolve1d(imgs, g, axis=1)
    final_imgs = convolve1d(new_imgs, h, axis=0)
    Iy = convolve1d(final_imgs, g, axis=2)

    return Iy

def compute_It(imgs):
    """
    params:
        @imgs: np.array(h, w, N)
    return value:
        It: np.array(h, w, N)
    """
    """
    STUDENT CODE BEGINS
    """
    # num_imgs = imgs.shape[2]
    # img_dim = imgs.shape[0]
    # #print(h.shape)
    # new_imgs = deepcopy(imgs)
    # final_imgs = deepcopy(imgs)

    # for i in range(num_imgs):
    #     img_int = imgs[:,:,i]
    #     C = scipy.signal.convolve2d(img_int, g, mode='same') #convolving g in x
    #     D = scipy.signal.convolve2d(C.T, g, mode='same') #convolving g in y
    #     new_imgs[:,:,i] = D.T

        
    # #convolving over time now
    # for j in range(img_dim):
    #     t_int = new_imgs[:,j,:]
    #     E = scipy.signal.convolve2d(t_int, h, mode='same') #convolving g in t
    #     final_imgs[:,j,:] = E


    # It = final_imgs


    new_imgs = convolve1d(imgs, g, axis=1)
    final_imgs = convolve1d(new_imgs, g, axis=0)
    It = convolve1d(final_imgs, h, axis=2)

    return It
