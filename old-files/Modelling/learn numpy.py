#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:01:47 2020

@author: skwa
"""

import numpy as np
"""
array = np.array([[1,2,3],[2,3,4]])
print(array)
print('number pf dim:',array.ndim)
print('shape',array.shape)
print('size:', array.size)
"""

"""
a =np.array([[2,23,4],[2,34,2]], dtype=np.int)
"""
"""
a = np.arange(10,20,2)
b = np.arange(12).reshape((3,4))
c = np.linspace(1,10,6).reshape((2,3))
print(c)
"""
"""
a = np.array([3.14,20,30,40])
b = np.arange(4)
"""
"""
print(a,b)
c=a-b
print(c)
print(b**2)
print(np.sin(a))
print(a<3)
print(b==3)
"""
"""
f = a.reshape((2,2))
print(f)
g = b.reshape((2,2))
print(g)
print(np.dot(f,g))
print(f*g)
print(f.dot(g))
"""
"""
a =np.random.random((2,4))
a =np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(np.sum(a,axis=1))
print(np.min(a,axis = 0))
print(np.max(a,axis = 1))
"""
"""
A = np.arange(2,14).reshape((3,4))

print(A)

print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A))
print(A.mean())
print(np.median(A))

print(np.cumsum(A))
print(np.diff(A))
a = np.array([[0,1,0,1],[1,0,1,0]])
print(a)

print(np.nonzero(a))
print(np.sort(a))


print((A.T).dot(A))
print(np.clip(A,8,9))

print(np.mean(A,axis    =1))

A=np.arange(3,15).reshape((3,4))
print(A)

print(A[2])
print(A[2][2])
print(A[2,:])
print(A[:,1])
"""
"""
print(A[1,1:3])
print(A.T)
for row in A.T:
    print(row)
"""
"""
print(A.flatten())
for item in A.flat:
    print(item)
"""

A= np.array([1,1,1])[np.newaxis,:]
B=np.array([2,2,2])[np.newaxis,:]
"""
print(A,B)
C = np.vstack((A,B))
D = np.hstack((A,B))
print(D,D.shape)
print(A.shape)
E = A[:,np.newaxis]
F = B[:,np.newaxis]
print(np.hstack((E,F)))

E = A[np.newaxis,:].T
print(E)
"""
"""
C = np.concatenate((A,B,B,A),axis=1)
print(C)

"""


























