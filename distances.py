import numpy as np
from numpy.linalg import norm
from scipy import spatial
import math

def cosine_distance(u,data):
    cos_dists = []

    for i in range(len(data)):
        result = 1 - spatial.distance.cosine(u, data[i])    
        cos_dists.append(result)
    
    return cos_dists 

def euclidean_distance(point, data):
    # returns the euclidean distance between a point and all points from a specific data
    return np.sqrt(np.sum((point - data)**2, axis=1))

def most_common(lst):
    '''Returns the most common element in a list'''
    return max(set(lst), key=lst.count)

"""
def cosine_distance(u,data):
    cosine_dists = []
    
    for i in range(len(data)):
        produc = 0
        produc = np.dot(u,data[i])
        distance = 0 
        mag_u = 0    # ||u||
        mag_v = 0    # ||v||
        n = len(u)

        for j in range(n):
            mag_u += (u[j])**2
            mag_v += (data[i][j])**2

        mag_u = math.sqrt(mag_u)
        mag_v = math.sqrt(mag_v)
        distance = 1 - (produc/(mag_u*mag_v))
        cosine_dists.append(distance)

    return cosine_dists 

def euclidean_distance(p,q):
    n = len(p)
    sum = 0
    for i in range(n):
        sum += (q[i] - p[i])**2

    return math.sqrt(sum)

"""
