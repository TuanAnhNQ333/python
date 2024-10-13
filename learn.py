stra = int("59")
strb = 69 + 5
print(stra)
print(strb)
a = 'my team is %s %s year old' %('10', '12')
print(a)
s = '%s %s'
result = s %('1', '2')
print(result)
# %s : gia tri cua _str_ 
# %r : gia tri _repr_
# %d : gia tri cua 1 so nguyen 
# %<so chu so phan thap phan>f : gia tri cua 1 so chuyen sang so thuc
# >>> class something
# def _repr_(self)
#     return 'this is _repr_'
# def _str_(self)
#     return 'this is _str_'
# >>> thing = somethings : doi tuong cua lop thing, tuong tu nhu struc trong c
# >>> type(sthing) # thuoc lop somethings
item_name = 'computer'
item_qty = 10
name = 'tuan anh'
address = 'ha noi'
phone = '0346476176'
result = f'student: {name}\nAddress: {address}\nPhone:{phone}'
print(result)
r = '1:{one}, 2:{two}'.format(one=111,two=222)
print(r)
w = 'how{:*^50}chill'.format('tuananh')
print(w)
row1 = '. {:-<6} + {:-^15} + {:->10} +'.format('','','')
row2 = '. {:<6} + {:^15} + {:>10} +'.format('ID','HO VA TEN','NOI SINH')
row3 = '. {:<6} + {:^15} + {:>10} +'.format('5648','TUAN ANH','VIET NAM')
row4 = '. {:<6} + {:^15} + {:>10} +'.format('5648','NONAME','KOREA')
row5 = '. {:-<6} + {:-^15} + {:->10} +'.format('','','')
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)

