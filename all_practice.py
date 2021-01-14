#  Write a hello world program and run it in python
"""
message = "Hello World"
print(message)
"""

#  Write a program that asks for a your name and prints hello, <your name>
"""
name_input = input("What is your name\n >")
print(f"Hello, {name_input}")
"""

#  Write a function that checks whether a number is even (3 WAYS TO DO SO)
"""
def is_it_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
        
print(is_it_even(10)) # To call
"""


#  Write a program that asks for a password and if you guess it right access granted, otherwise exit()
"""
password = "strongPassword"
pass_guess = str(input("What is the password:\n >"))

if pass_guess == password:
    print("Access Granted")
else:
    print("Access Denied, password is wrong")
"""



#  Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

# Fizzbuzz
"""
given a number n:
    for all numbers 1..n:
        if the number divides evenly by 3 -> Fizz
        if the number divides evenly by 5 -> Buzz
        if the number divides evenly by 3 and 5 -> FizzBuzz
        otherwise -> n
"""

