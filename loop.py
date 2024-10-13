from __future__ import print_function
#vòng lặp for
#hàm range(start, stop, step) sinh ra dãy số và sử dụng vòng for để duyệt qua từng số trong dãy sinh ra
a = range(1, 10, 1) 
for i in a :
    print(i, end = ' ')
n = 10
for i in range(n, 0, -1): 
    print(i, end = ' ')
n = 10
s = 1
for i in range(1, n + 1): 
    s *= i
print(s)
list = ["tuan", "anh", "deptrai"]
for index in range(len(list)):
    print(list[index])
else:
    print("inside else block")
#vòng lặp lồng nhau : nested loop
n = 5
for i in range(1, n):
    for j in range(i):
        print(i, end = ' ')
    print()
#câu lệnh continue
for letter in 'tuan anh dep trai':
    if letter == 'e' or letter == 't':
        continue
    print('current letter :', letter)
#câu lệnh break
for letter in 'tuan anh dep trai':
    if letter == 'e' or letter == 't' :
        break
print('current letter :', letter)
#câu lệnh pass 
for letter in 'tuan anh dep trai' :
    pass
print('last letter :', letter)
fruits = ["orange", "apple", "kiwi"]
for fruit in fruits :
    print(fruit)
