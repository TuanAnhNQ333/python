
f = lambda x: x**2
a = [[2, 9], [5, 6], [3, 9]]
a.sort(key=lambda x:x[0])
print(f(5))
print(a)
high_ord_func = lambda x, func: x + func(x) #3 + 3*3
print(high_ord_func(3, lambda x:x**2))
#string processing
s= "hello?"
print(len("hehehe"))
for letter in "hehehe":
    print(letter, end=' ')
print()
print(s[:-1] + 'there')
b = "silver"
print("%s is a metal" %b)

b = [i for i in range(10) if i %2== 0]
squares = {x:x*x for x in range(6)}
c = [[i, j] for i in range(3) for j in range(3)]
#flatten list : chuyen tu 2 chieu ve 1 chieu
d = [j for i in c for j in i]
print(b)
print(c) #lap qua tung phan tu cua mang c 
print(squares)
print(d)

#title dictionary
dct = dict()
#dct = {}
dct = {'csev' : 2,
       'zqian' : 1,
       'cwen' :2}
for key, val in dct.items():
    print(str(key) + '\t' + str(val))

counts = dict()
names = ['csev', 'cwen', 'anh', 'em', 'em']
for name in names:
    counts[name] = counts.get(name, 0) + 1  #dem so lan xuat hien
print(counts)

#pickle : luu obj 
with open('baitap.py', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    print(content)
    for line in content:
        print(line, end='')
#encoding : ma hoa bang UTF-8
#entire fiel : file.read()
# first k char : file.read(k)
# the first line : file.readline()
'''with open('baitap.py', 'w') as file:
    file.write('new content \nOur data here:')
content = open('baitap.py')
print(content.read())'''

import pickle
a = ['a', 'b', 'c']
with open('data.pkl', 'wb') as data:
    pickle.dump(a, data)













