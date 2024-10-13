name = "alice"
age = 30.888
print(f"my name is {name} and I am {round(age,1 )} years old.")
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
radius = radius + 1 
print(area)
# nhập giá trị
num = int(input("enter an integer:"))
print(f"integer: {num}, Type : {type(num)}")
arr = input("enter a list of numbers separated by spaces : ").split()
arr = [int(x) for x in arr] #list comprehension 
print(f"list: {arr}, Type: {type(arr)}")
a = 0
if (a): # if a == true
    print("a is positive")
elif a < 0:
    print("a is negative")
else:
    print("a is false")
a = [1, 2, 3]
print(sorted(a, reverse=True))


# nhập 3 cạnh tam giác và kiểm tra
num1, num2, num3 = map(int, input().split())
num1, num2, num3 = sorted([num1, num2, num3])
'''print(sorted(b, reverse=True)) # sắp xếp lại mảng b đã cho'''
if (num1 + num2 > num3) and (num3 > num1 - num2):
    print("true")
else:
    print("false")

#loop
# for : biết sẵn số lần lặp, while : dừng khi thoả mãn đk
for i in range(5):
    print(i, end=' ')
a = [2, 5, 3]
for i in a:
    print(i, end=' ')

















