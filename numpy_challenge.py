#!/usr/bin/env python
# coding: utf-8

# In[3]:

import numpy as np


def matrix_multiplication(a, b):
    return np.dot(a, b)


# In[4]:


def multiplication_check(list_matrices):
    c = 0
    for i in range(len(list_matrices)-1):
        # число столбцов первого равно числу строк второго
        if len(list_matrices[i][0]) == len(list_matrices[i+1]):
            c += 1
    if c == len(list_matrices)-1:
        return True
    else:
        return False


# In[5]:


def multiply_matrices(list_matrices):
    mult = np.linalg.multi_dot(list_matrices)
    return mult


# In[ ]:


def compute_2d_distance(a, b):
    return np.sqrt(((a[0]-b[0])**2)+((a[1]-b[1])**2))


# In[ ]:


def compute_multidimensional_distance(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i]-b[i])**2
    return np.sqrt(d)


# In[ ]:

def compute_pair_distances(a):
    # refers to the compute multidimensional distance function
    b = np.zeros((len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            b[i][j] = compute_multidimensional_distance(a[i], a[j])
            b[j][i] = b[i][j]
    return b


if __name__ == "__main__":
    n1 = np.arange(50, 2, -3)
    n2 = np.array([[0, 1, 2], [3, 4, 5]])
    n3 = np.linspace(0, 1, 6)
