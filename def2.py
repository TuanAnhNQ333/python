import argparse
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

parser = argparse.ArgumentParser(description="greet a person based on input")
parser = add_argument('--name', type=str, help = "name of the person")
parser = add_argument('--age', type=int, help = "Age of the person")

args = parser.parse_args()
print(greet(args.name, args.age))

def val(x):
    x = 12
    print(x, id(x))
x = 10
val(x)
print(x, id(x))
def obj(x):
    x.append(15)
    print(x, id(x))
x = {10}
obj(x)
print(x, id(x))


def print_args(**kwargs):
    for key, val in kwargs.items():
        print(f'{key}: {val}')
print_args(a = 1, b = 2, c = 3, d = 4)






















