# tạo lớp đối tượng và các thuộc tính :
#self đại diện cho sự thể hiện của 1 lớp, dùng để liên kết thuộc tính của lớp, tham chiếu đến các thuộc tính thể hiện
class hotboy:
    attr1 = "deptrai"
    def __init__(self, name): #__init__ được sd để tạo các đối tượng của 1 lớp, đc gọi là constructor
        self.name = name
    def speak(self):
        print("my name is {}".format(self.name))
bomay = hotboy("bomay")
tuananh = hotboy("tuananh")
bomay = hotboy("bomay")
tuananh = hotboy("tuananh")
bomay.speak()
tuananh.speak()
print("bo may is a {}".format(bomay.__class__.attr1))
print("tuananh is also a {}".format(tuananh.__class__.attr1))
print("my name is {}".format(bomay.name))
print("my name is {}".format(tuananh.name))
# inheritance : kế thừa : là khả năng của 1 lớp để bắt nguồn hoặc kế thừa các thuộc tính từ một số lớp khác.
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
class B(A):
    def __init__(self, something):
        # calling init of parent class 
        A.__init__(self, something)
        print("B init called")
        self.something = something
        A.__init__(self, something)
obj = B("something")
class person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)
    def detail(self):
        print("my name is {}".format(self.name))
        print("id : {}".format(self.id))
class employee(person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, id)
    def detail(self):
        print("my name is {}".format(self.name))
        print("id : {}".format(self.id))
        print("post : {}".format(self.post))
a = employee('tuananh deptrai vcl', 20235648, 30000000, "intern")
a.display()
a.detail()
# polymorphism : đa hình : oop kế thừa và ghi đè phương thức trong các lớp 
class bird:
    def intro(self):
        print("there are many type of birds")
    def flight(self):
        print("most of the bird can fly")
class sparrow(bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(bird):
    def flight(self):
        print("ostriches cannot fly")
obj_bird = bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
