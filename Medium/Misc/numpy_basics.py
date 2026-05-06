from numpy import array
import numpy as np
'''l = [1.0, 2.0]
print(type(l))

a = array(l)
print(type(a))
print(a)


print(a.shape)
print(a.dtype)
#print(np.__version__)'''
# Create a length-10 integer array filled with zeros
'''z=np.ones((2,3), dtype=float)
q=np.full((3,), 0)
g=np.arange( 20)
print(g)
print(q)
print(z)
print(len(z))'''
# Create an array of five values evenly spaced between 0 and 1
'''z=np.linspace(0, 20, 5)
print(z)'''
'''p=np.random.random((3, 4))
print(p)'''
#p=np.random.randint(0, 10, (3, 5))
'''p=np.random.randint(100)'''
#p=np.eye(3,dtype=str)
#p=np.eye(3)
#p=np.diag([1,2,3])
'''p=np.full((3,3),'0',dtype=int)
np.fill_diagonal(p,4)
print(p)'''
'''a = np.array([1, 2, 3], dtype=np.int16)
print(a.dtype)
print(a)'''
'''x1 = np.random.randint(10, size=6) # One-dimensional array
print(x1.ndim)
print(x1)
x3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x3.ndim)
print(x3)'''
x3=np.random.randint(0,10,(3,5,5),dtype=int)
'''print(x3)
print(x3.ndim)
print(x3.shape)'''
#print(x3.itemsize)
print(x3.size)
print(x3.nbytes)














