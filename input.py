
# buoc 1 : nhap so
s = input('nhap 3 so : ')
#buoc 2 : tach 3 so do ra
a = s.split()
#buoc 3 : dung ham map để ánh xạ ép các phần tử trong list sang kiểu dữ liệu mong muốn
x, y, z = map(int,a )
print(x + y + z)
# nhap 4 so nguyen tren 1 dong
x, y, z, t = map(int, input('nhap 4 so nguyen : ').split())
print(x,y,z,t)
x, y, z, t = map(float, input('nhap 4 so thuc : ').split())
print(x,y,z,t)