import numpy as np
import sys
def depth(flow, confidence, ep, K, thres=10):
    """
    params:
        @flow: np.array(h, w, 2)
        @confidence: np.array(h, w)
        @K: np.array(3, 3)
    return value:
        depth_map: np.array(h, w)
    """
    depth_map = np.zeros_like(confidence)
    thresh_arr = np.where(confidence>thres)
    flow_u = flow[:,:,0]
    flow_v = flow[:,:,1]
    flow_u = flow_u[thresh_arr]
    flow_v = flow_v[thresh_arr]
    flow_mat = np.vstack((flow_u, flow_v, np.zeros(flow_u.shape[0])))
    flow_mat = np.linalg.inv(K)@flow_mat #normalising
 
    indices = np.argwhere(confidence>thres) #- flow.shape[0]//2
    #print(indices)
    indices_mat = np.vstack((indices[:,1], indices[:,0], np.ones(indices.shape[0])))
    indices_normal = np.linalg.inv(K)@indices_mat #normalising 

    ep = ep #+ flow.shape[0]//2
    #print(ep)
    ep = np.reshape(ep, (3,1))
    ep = np.linalg.inv(K)@ep #normalising

    num = np.linalg.norm((indices_normal - ep), axis=0)
    den = np.linalg.norm(flow_mat, axis=0)
    depth = num/den
    depth_map[thresh_arr] = depth

    """
    STUDENT CODE BEGINS
    """

    truncated_depth_map = np.maximum(depth_map, 0)
    valid_depths = truncated_depth_map[truncated_depth_map > 0]
    # You can change the depth bound for better visualization if your depth is in different scale
    depth_bound = valid_depths.mean() + 10 * np.std(valid_depths)
    print(f'depth bound: {depth_bound}')

    truncated_depth_map[truncated_depth_map > depth_bound] = 0
    truncated_depth_map = truncated_depth_map / truncated_depth_map.max()
    """
    STUDENT CODE ENDS
    """

    return truncated_depth_map
