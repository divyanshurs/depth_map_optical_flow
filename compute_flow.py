import numpy as np
import pdb
import sys

def flow_lk_patch(Ix, Iy, It, x, y, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
        @x: int
        @y: int
    return value:
        flow: np.array(2,)
        conf: np.array(1,)
    """
    """
    STUDENT CODE BEGINS
    """
    w = int(size/2)
    val_x = Ix[max(0,y-w):y+w+1, max(0,x-w):x+w+1].flatten()
    val_y = Iy[max(0,y-w):y+w+1, max(0,x-w):x+w+1].flatten()
    val_t = It[max(0,y-w):y+w+1, max(0,x-w):x+w+1].flatten()
    A = np.vstack((val_x, val_y)).T
    B = -np.reshape(val_t, (val_t.shape[0],1))
    P, D, Q = np.linalg.svd(A)
    flow = np.linalg.lstsq(A,B, rcond=None)[0].reshape((2,))
    conf = D[-1]


    """

    STUDENT CODE ENDS
    """
    return flow, conf


def flow_lk(Ix, Iy, It, size=5):
    """
    params:
        @Ix: np.array(h, w)
        @Iy: np.array(h, w)
        @It: np.array(h, w)
    return value:
        flow: np.array(h, w, 2)
        conf: np.array(h, w)
    """
    image_flow = np.zeros([Ix.shape[0], Ix.shape[1], 2])
    confidence = np.zeros([Ix.shape[0], Ix.shape[1]])
    for x in range(Ix.shape[1]):
        for y in range(Ix.shape[0]):
            flow, conf = flow_lk_patch(Ix, Iy, It, x, y)
            image_flow[y, x, :] = flow
            confidence[y, x] = conf
    return image_flow, confidence

    

