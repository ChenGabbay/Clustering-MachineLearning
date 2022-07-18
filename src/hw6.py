import numpy as np

def get_random_centroids(X, k):

    '''
    Each centroid is a point in RGB space (color) in the image. 
    This function should uniformly pick `k` centroids from the dataset.
    Input: a single image of shape `(num_pixels, 3)` and `k`, the number of centroids. 
    Notice we are flattening the image to a two dimentional array.
    Output: Randomly chosen centroids of shape `(k,3)` as a numpy array. 
    '''
    X = np.unique(X,axis=0)
    indexList = np.random.choice(range(len(X)), k, replace=False)
    centroids = [X[i] for i in indexList]              
    ###########################################################################
    # TODO: Implement the function.                                           #
    ###########################################################################
    pass
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    # make sure you return a numpy array
    return np.asarray(centroids).astype(np.float) 



def lp_distance(X, centroids, p=2):

    '''
    Inputs: 
    A single image of shape (num_pixels, 3)
    The centroids (k, 3)
    The distance parameter p

    output: numpy array of shape `(k, num_pixels)` thats holds the distances of 
    all points in RGB space from all centroids
    '''
    distances = []
    k = len(centroids)
    for i in range(k):
        currentCentroid = centroids[i]
        changedDataset = X-currentCentroid
        finalDataset = np.abs(changedDataset ** p)            
        
        distances.append(np.sum(finalDataset, axis=1)**(1/p))
        
    ###########################################################################
    # TODO: Implement the function.                                           #
    ###########################################################################
    pass
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return np.asarray(distances).astype(np.float) 

def kmeans(X, k, p ,max_iter=100):
    """
    Inputs:
    - X: a single image of shape (num_pixels, 3).
    - k: number of centroids.
    - p: the parameter governing the distance measure.
    - max_iter: the maximum number of iterations to perform.

    Outputs:
    - The calculated centroids as a numpy array.
    - The final assignment of all RGB points to the closest centroids as a numpy array.
    """
    classes = []
    centroids = get_random_centroids(X, k)
    
    for i in range(max_iter):
        oldCentroids = np.copy(centroids)
        distance = lp_distance(X,centroids,p)
        classes = np.argmin(distance,axis=0)
        for j in range(k):
            indexes = np.where(classes == j)
            centroids[j] = np.mean(X[indexes],axis=0)

        if np.array_equal(oldCentroids,centroids):
            break       
    
    ###########################################################################
    # TODO: Implement the function.                                           #
    ###########################################################################
    pass
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return centroids, classes

def kmeans_pp(X, k, p ,max_iter=100):
    """
    Your implenentation of the kmeans++ algorithm.
    Inputs:
    - X: a single image of shape (num_pixels, 3).
    - k: number of centroids.
    - p: the parameter governing the distance measure.
    - max_iter: the maximum number of iterations to perform.

    Outputs:
    - The calculated centroids as a numpy array.
    - The final assignment of all RGB points to the closest centroids as a numpy array.
    """
    classes = []
    centroids = get_random_centroids(X,1)
    for i in range(k-1):
        distances = lp_distance(X,centroids)
        minDistances = np.min(distances,axis=0)
        minDistances = minDistances/np.sum(minDistances)
        
        indexCentroid = np.random.choice(len(minDistances), 1, p = minDistances)
        centroids = np.append(centroids,X[indexCentroid], axis=0)
        
        
    for i in range(max_iter):
        oldCentroids = np.copy(centroids)
        distance = lp_distance(X,centroids,p)
        classes = np.argmin(distance,axis=0)
        for j in range(k):
            indexes = np.where(classes == j)
            centroids[j] = np.mean(X[indexes],axis=0)

        if np.array_equal(oldCentroids,centroids):
            break       
        
    ###########################################################################
    # TODO: Implement the function.                                           #
    ###########################################################################
    pass
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return centroids, classes
