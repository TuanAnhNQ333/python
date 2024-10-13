from math import *
# sqrt : square root, isqrt : int square root
# pow : power : luỹ thừa
print(sqrt(36))
print(pow(2, 10))
print(pow(10, 1/3))
print(pow(27, 1/3))
#ceil : làm tròn lên : 2.5 -> 3
print(ceil(2.3))
print(ceil(2.8))
#floor : làm tròn xuống : 2.5 -> 2
print(floor(2.9))
#factorial : giai thừa
print(factorial(100))
#gcd : greatest common divisor : ước chung lớn nhất
print(gcd(100, 450))
#comb :  tính tổ hợp chập k của n : Cn(k)
print(comb(10,3))
#perm : chỉnh hợp châp k của n : Ank
print(perm(10,3))
#fabs : giá trị tuyệt đối
print(fabs(-100))
#built-in function
print(abs(-100))
#round : làm tròn lên hoặc xuống theo giá trị 
print(round(2.52))
#sum : tính tổng
print(sum([1, 2, 3, 4, 5]))
#def function_name(parameters) :
    #statement
    #return expression -> function return 
# tạo 1 hàm : 
def fun() :
    print("tuan anh dep trai")
fun() # gọi hàm 
def add(num1 : int, num2 : int) -> int:
    """add two numbers"""
    num3 = num1 + num2 
    return num3
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"the addition of{num1} and {num2} results {ans}.")
def is_prime(n):
    if n in [2, 3] :
        return True
    if ( n == 1) or (n % 2 == 0) :
        return False
    r = 3 
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))
# dối số : parameter : là các giá trị được truyền vào trong dấu ngoặc của hàm.
def evenodd(x):
    if(x % 2 == 0):
        print("even")
    else:
        print("odd")
evenodd(2) # chẵn
evenodd(3) # lẻ
# đối số mặc định : tham số giả định giá trị mặc định nếu giá trị không được cung cấp trong lệnh gọi hàm cho đối số đó
def myfun(x, y = 50):
    print("x :", x)
    print("y :", y)
myfun(10)
# dối số từ khoá : cho phép người gọi chỉ định tên đối số cùng với các giá trị để người gọi không cần nhớ thứ tự tham số
def student(firstname, lastname):
    print(firstname, lastname)
student(firstname = 'Tuananh', lastname='deptrai')
student(lastname='tuananh', firstname='deptrai')
#lập luận vị trí : sử dụng đối số vị trí trong khi gọi hàm để đối số đầu tiên được gán dcho tên và đối số thứ 2 được gán cho tuổi
def nameage(name, age):
    print("hi, i am", name)
    print("my age is", age)
print("case-1 : ")
nameage("tuananhdeptrai", 20)
print("\ncase-2")
nameage(20, "tuananhdeptrai")
#đối số từ khoá : args và kwargs :  truyền 1 số lượng biến đổi các số cho 1 hàm bằng cách sử dụng ký hiệu đặc biệt
# *args : đối số không phải từ khoá
# *kwargs : đối số là từ khoá

    #đối số từ khoá có độ dài không đổi
def myfunny(*argv):
    for arg in argv:
        print(arg, end = ' ')
myfunny('hello', 'tuananh', 'deptrai')
    #đối số từ khoá có độ dài thay đổi
def myfunny2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myfunny2(first = 'tuananh', mid = 'deptrai', last = 'so 1')
    #chuỗi tài liệu : docsring : mô tả chức năng của hàm
    # print(funtion_name.__doc__)
def evenodd2(x):
    """function to check if the number is even or odd"""
    
    if(x % 2 == 0):
        print("even")
    else:
        print("odd")
print(evenodd2.__doc__)
# hàm lông nhau : các hàm lồng nhau có thể truy cập các biến của phạm vi bao quanh
def f1():
    s = 'tuan anh dep trai vcl'
    def f2(): 
        print(s)
    f2()
f1()
#hàm ẩn danh : là hàm không có tên, từ khoá def : hàm bình thường 
# lambda : hàm ẩn danh
def cube(x):
    return x*x*x
cube_v2 = lambda x : x*x*x
print(cube(7))
print(cube_v2(7))
#hàm đệ quy 
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial1(4))
#câu lệnh return : return [list]
def square_value(num):
    """this function returns the square value of the entered number"""
    return num **2
print(square_value(2))
print(square_value(-4))
#truyền theo tham chiếu và truyền giá trị
def myfunn(x):
    x[0] = 20
lst = [10, 11, 12, 13, 14, 15]
myfunn(lst)
print(lst)
def funn(x):
    x = [20, 30, 40]
lst = [10, 11, 12, 13, 14, 15]
funn(lst)
print(lst)
# hàm swap :
def swap(x, y):
    temp = x
    x = y
    y = temp
x = 2
y = 3
swap(x, y)
print(x)
print(y)




