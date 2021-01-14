#  Write a hello world program and run it in python

message = "Hello world"

print(message) # or just print("hello world") with string

#  Write a program that asks for a your name and prints hello, <your name>

name = input("What is your name: ")
print(f"Hello, {name}")

#  Write a function that checks whether a number is even (3 WAYS TO DO SO)

def is_even(x): # need "def" for function
    if x % 2 == 0:
        return True
    else:
        return False


# Could also do
def is_even2(z):
    if z % 2 ==0:
        return True

# Could also do
def is_even3(n):
    return n % 2 == 0

# This is a helper function
def is_divisible(n, d):
    return n % d == 0

def is_even_again(n):
    return is_divisible(n, 2)

is_divisible(4, 2)
