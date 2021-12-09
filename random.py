#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time
from matplotlib.pyplot import figure
import random
import numpy as np
import string
import matplotlib.pyplot as plt
import timeit


# In[ ]:


# Task 1


# In[ ]:


i_s = []
times_random = []
times_numpy = []
# here maximum iteration number can be set
for i in range(10, 10**7, 1000000):
    i_s.append(i)
    start_time = time.time()
    [random.uniform(0, 1) for x in range(i)]
    times_random.append(time.time() - start_time)
    start_time = time.time()
    np.random.uniform(0, 1, (1, i))
    times_numpy.append(time.time() - start_time)
figure(figsize=(15, 12), dpi=80)
plt.plot(i_s, times_random, label="random")
plt.plot(i_s, times_numpy, label="numpy")
plt.legend()
plt.xlabel('times of iteration')
plt.ylabel('time of function')


# In[ ]:


# Task 2


# In[ ]:


def check_sorted(a):
    for i in range(0, len(a)-1):
        if (a[i] > a[i+1]):
            return False
    return True


def monkey_sort(a):
    while not check_sorted(a):
        random.shuffle(a)


mycode = '''
def monkey_sort(a):
    while not check_sorted(a):
        random.shuffle(a)
'''

# list 'a' is necessary

max_value = 60
out = []
out_std = []
for i in range(10, max_value, 10):
    b = timeit.repeat(stmt=mycode, repeat=i)
    out.append(np.mean(b))
    out_std.append(np.std(b))
plt.plot(out)


# In[ ]:


# Task 3


# In[ ]:


x = [0]
y = [0]
directions = ['up', 'down', 'left', 'right']
for i in range(100):
    direction = random.choice(directions)
    if direction == 'up':
        x.append(x[-1])
        y.append(y[-1]+1)
    if direction == 'down':
        x.append(x[-1])
        y.append(y[-1]-1)
    if direction == 'left':
        x.append(x[-1]-1)
        y.append(y[-1])
    if direction == 'right':
        x.append(x[-1]+1)
        y.append(y[-1])
plt.scatter(x, y)


# In[ ]:


# Task 4


# In[ ]:


n = 1000
a = np.zeros((n, n))
points = np.array([(0, 0), (0, n), (n, n//2)])
start = np.array((0, 0))
for i in range(n*n):
    new_point = random.randint(0, 2)
    start = (points[new_point]+start)//2
    a[start[0]][start[1]] = 1
figure(figsize=(12, 10), dpi=80)
a = np.flip(a, axis=0)
plt.imshow(a)


# In[ ]:


# Task 5


# In[ ]:


# enter 'a' - any text
ls = a.split(" ")
ls1 = []
for word in ls:
    if len(word) > 2:
        if word[-1] in string.punctuation:
            # if the last element is dot or comma
            word1 = ''.join(random.sample(word[1:-2], len(word)-3))
            word = word.replace(word[1:-2], word1)
            ls1.append(word)
        else:
            word1 = ''.join(random.sample(word[1:-1], len(word)-2))
            word = word.replace(word[1:-1], word1)
            ls1.append(word)
    else:
        ls1.append(word)
print(*ls1)
