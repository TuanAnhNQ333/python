#cấu trúc rẽ nhánh if else
if 100 > 50:
    print('hello')
#if condition : 
#   câu lệnh (tab để thụt lề)
n = 60
if (n >= 50) and (n <= 100):
    print('hello world')
    print('so beautiful')
if n % 2 == 0:
    print('chan') 
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum


# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)
def digit(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
list = [3,11,111,5555]
oldList = [digit(i) for i in list if i & 1]
print(oldList)
a, b = 100, 200
if a < b :
    print(a, 'less than', b)
elif a == b : 
    print(a, 'equal to', b)
else :
    print(a, 'greater than', b)
c, d = 100, 200
if c < d : print(c, 'less than', d) ; print('hello')
#toán tử ba ngôi : variable = statement if cond else statement
a, b = 100, 200
res = 'hello' if a < b else 'tuan anh'
print(res)
    