# given a list of numbers, return the one that 
# occurs an odd number of times. 
# your input list will only have one that 
# qualifys  

ls = [3, 4, 3, 3, 4]
def odd_number_app(ls):
    for n in ls:
        count_of_numbers = ls.count(n)
        odd_apps = [n]
        if count_of_numbers % 2 != 0:
            return odd_apps

print(odd_number_app(ls))


# Write a function that generates the Fibonacci 
# sequence 
# 1, 2, 3, 5, 8, 13, 21, 34.... 
# who's total elements is equal to the number 
# the user passes into the function 
# Bonus: Return a tuple (x, y) 
# where x is the list of all generated elements 
# and y is the sum of those elements

