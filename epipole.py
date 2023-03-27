import numpy as np
import sys



def epipole(u,v,smin,thresh,num_iterations = 1000):
    ''' Takes flow (u,v) with confidence smin and finds the epipole using only the points with confidence above the threshold  
        (for both sampling and finding inliers)
        u, v and smin are (w,h), thresh is a scalar
        output should be best_ep and inliers, which have shapes, respectively (3,) and (n,) 
    '''

    """YOUR CODE HERE -- You can do the thresholding outside the RANSAC loop here
    """
    #print(np.where(smin>thresh))
    thresh_arr = np.where(smin>thresh)
    thresh_arr_flatten = np.where(smin.flatten()>thresh) #to give the corr index
    new_u = u[np.where(smin>thresh)[0], np.where(smin>thresh)[1]]
    new_v = v[np.where(smin>thresh)[0], np.where(smin>thresh)[1]]
    flow_mat = np.vstack((new_u, new_v, np.zeros(new_u.shape[0])))
    indices = np.argwhere(smin>thresh) - u.shape[0]//2
    indices_mat = np.vstack((indices[:,1], indices[:,0], np.ones(indices.shape[0])))

    """ END YOUR CODE
    """

    sample_size = 2

    eps = 10**-2

    best_num_inliers = -1
    best_inliers = None
    best_ep = None

    for i in range(num_iterations):
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(0,np.sum((smin>thresh))))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """YOUR CODE HERE
        """
        flow_x_1 = new_u[sample_indices[0]]
        flow_y_1 = new_v[sample_indices[0]]
        vec_1 = np.array([flow_x_1, flow_y_1, 0])

        flow_x_2 = new_u[sample_indices[1]]
        flow_y_2 = new_v[sample_indices[1]]
        vec_2 = np.array([flow_x_2, flow_y_2, 0])

        x_p_1 = np.append([indices[sample_indices[0]][1], indices[sample_indices[0]][0]], [1])
        x_p_2 = np.append([indices[sample_indices[1]][1], indices[sample_indices[1]][0]], [1])
        #x_p_1 = np.array([sample_indices[0], sample_indices[1], 1])
        cross_1 = np.cross(x_p_1.T, vec_1.T)
        cross_2 = np.cross(x_p_2.T, vec_2.T)

        cross_sampled = np.vstack((cross_1, cross_2))

        U,S,V_t=np.linalg.svd(cross_sampled)
        V = V_t.T
        E_vector = V[:,-1]
        
        test_f = flow_mat[:, test_indices]
        test_i = indices_mat[:,test_indices]
        cross_test = np.cross(test_i.T, test_f.T)
        distance_arr = abs(np.dot(cross_test, E_vector))
        test_inl = np.argwhere(distance_arr<=eps)
        test_inl = np.reshape(test_inl, (test_inl.shape[0],))
        inliers = np.concatenate((thresh_arr_flatten[0][sample_indices], thresh_arr_flatten[0][test_indices[test_inl]]))
        #inliers = list(sample_indices)


        # for p in range(test_indices.shape[0]):
        #     ind = test_indices[p]
        #     flow_x_test = new_u[ind]
        #     flow_y_test = new_v[ind]
        #     vec_test = np.array([flow_x_test, flow_y_test, 0])

        #     x_p_test = np.append(indices[p], [1])
        #     # print(vec_test)
        #     # print(x_p_test)

        #     cross_test = np.cross(x_p_test, vec_test)

        #     distance = np.dot(E_vector.T, cross_test)
        #     if(distance< eps):
        #         inliers.append(test_indices[p])




        """ END YOUR CODE
        """

        #NOTE: inliers need to be indices in original input (unthresholded), 
        #sample indices before test indices for the autograder
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_ep = E_vector
            best_inliers = inliers

    return best_ep, best_inliers