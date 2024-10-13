#task1 : in số
x = int(input())
y = int(input())
c = str(input())
f = float(input())
d = float(input())

print(x)
print(y)
print(c)
print(f"{f:.2f}") # in ra f với 2 chữ số sau dấu phẩy
print(f"{d:.9f}")
print('%.2f' %f)
print('%.9f' %f)
#task2 : 
x, y, z, t = map(int, input().split()) #nhập 4 số trên cùng 1 dòng
print(y,z,x,t, sep = ',') #in ra 4 só, cách nhau bởi dấu phẩy
print(x,y,z,t)
print(x - y + z * t)
#task 3
# chia nguyên : // 
from math import *
n = int(input())
print(n // 1000)
#task 4 : chia phép dư     