#Numpy : thuc hien phep toan so hoc dung de code lai ML model
#Pandas : lam viec voi du lieu bang table
import Numpy as np 
from Numpy.random import rand
'''t = np.array([0., 1., 2., 3., 4., 5., 6,])
print(t)
print(t.ndim)
print(t.shape)
print(t[0], t[1], t[-1])
print(t[2:5], t[4:-1])
print(t[:2], t[3:])
 '''
t = np.array([[1., 2., 3.],
             [4., 5., 6.], 
             [10., 11., 12.]])
print(t)
print(t.ndim)
print(t.shape)
print(t[0,1])
print(t[:, 1])
print(t[:, 1].shape)
print(t[:, :-1])
print(t[:, 0:-1:2])

d = np.random.rand(4,1)
e = np.random.randint(-3, 8, size = (3, 3))
print(d)
print(e)
arr = np.identity(3)




























