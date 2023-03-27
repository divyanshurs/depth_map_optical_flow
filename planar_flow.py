import numpy as np
import sys
def compute_planar_params(flow_x, flow_y, K,
                                up=[256, 0], down=[512, 256]):
    """
    params:
        @flow_x: np.array(h, w)
        @flow_y: np.array(h, w)
        @K: np.array(3, 3)
    return value:
        sol: np.array(8,)
    """

    flow_plane_x = flow_x[up[0]:down[0], up[1]:down[1]].flatten()
    flow_plane_y = flow_y[up[0]:down[0], up[1]:down[1]].flatten()
    flow_stack = np.vstack((flow_plane_x, flow_plane_y, np.zeros(flow_plane_x.shape[0])))
    K_inv = np.linalg.inv(K)
    flow_stack = K_inv@flow_stack
    ind_arr = []
    for i in range(up[0], down[0]):
        for j in range(up[1], down[1]):
            arr = K_inv@np.array([j,i,1])
            arr = arr/arr[2]
            ind_arr.append([arr[0], arr[1]])

    ind_arr = np.array(ind_arr).T
    x_vals = ind_arr[0,:]
    y_vals = ind_arr[1,:]
    u_vals = flow_stack[0,:]
    v_vals = flow_stack[1,:]
    x_square = x_vals**2
    xy = x_vals*y_vals
    y_square = y_vals**2
    first_row = np.vstack((x_square, xy, x_vals, y_vals, np.ones(x_square.shape[0]), np.zeros(x_square.shape[0]), np.zeros(x_square.shape[0]), np.zeros(x_square.shape[0]))).T
    second_row = np.vstack((xy, y_square, np.zeros(x_square.shape[0]), np.zeros(x_square.shape[0]), np.zeros(x_square.shape[0]), y_vals, x_vals, np.ones(x_square.shape[0]))).T
    # print(first_row[0,:])
    # print(second_row[0,:])
    A = np.vstack((first_row, second_row))
    
    B = np.hstack((u_vals, v_vals))
    sol = np.linalg.lstsq(A, B, rcond=None)[0]

    return sol
    
