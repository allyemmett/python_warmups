# Fizzbuzz

"""
given a number n:
    for all numbers 1..n:
        if the number divides evenly by 3 -> Fizz
        if the number divides evenly by 5 -> Buzz
        if the number divides evenly by 3 and 5 -> FizzBuzz
        otherwise -> n
"""
# Solution:
""" 
up_til = int(input("Number: > "))
for n in range(1, up_til + 1):
    if n % 15 == 0:
        print("FizzBuzz")
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

"""
# Solution as a function:
"""
def fizz_buzz():
    up_til = int(input("Number: > "))
    for n in range(1, up_til + 1):
        if n % 15 == 0:
         print("FizzBuzz")
        if n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
fizz_buzz()
"""
# TRY/EXCEPT BLOCK(code will try to run unless specify an exception)(ValueError is certain error being caught)
"""
try: 
    user_input = int(input("> "))
except: ValueError as err:
    print(f"that is not a valid number: {err}")
"""

#  Write a program that prints number of primes (divisible only by selves and 1)
def find_primes(n):
    primes = []
    num_to_check = 2
    while len(primes) < n:
        found_match = False
        for p in primes:
            if num_to_check % p == 0:
                found_match = True
                break
            if not found_match:
                primes.append(num_to_check)
            num_to_check += 1
        return primes

# print(find_primes(3))

#  Write a program that is a higher lower guessing game
def guessing_game(secret):
    print("Try to guess my number!")
    while(True):
        user_input = None
        try:
            user_input = int(input("> "))
        except Exception:
            pass
        if user_input:
            if user_input == secret:
                print("You got it, good guess!")
                return
            elif user_input > secret:
                print("Your number is too high")
            elif user_input < secret:
                print("Your number is too low")

# Write a program that prints the next 20 leap years (when year is multip by 4, except when divisible by 100, BUT if divisible by 400 & 100 then will be)
def leap_years(starting_year):
    upcoming_years = []
    current_year = starting_year

    while len(upcoming_years) < 20:
        if current_year % 4 == 0 and \
            current_year % 100 != 0 or current_year % 400 == 0:
            upcoming_years.append(current_year)
        current_year += 1

    return upcoming_years


print(leap_years(2001))




