# Create a function that takes in a number and returns it's 
# length, you can't use the len() function
""" SOLUTION I TRIED WITH NO LUCK
list_for_count = [234]
def length_of(list_for_count):
    for n in list_for_count:
        count_of = list_for_count.count(n)
        if count_of != 0:
            return(n, count_of)

length_of(list_for_count)
"""
# Class Solution with loop
def num_len(n):
    string_num = str(n) # int to string
    total_len = 0
    for _ in string_num:
        total_len += 1
    return total_len

print(num_len(199867))

"""
# OR WIHOUT INT TO STRING
def num_len2(n)
    current = n
    total = 0
    while(current > 0):
        current = current // 10
        total += 1
    return total

print(num_len2(199867))
"""



# write a function that takes in two lists 

# and only returns elements that are found in both 

ls1 = [1, 2, 5, 2, 0, 0, 0]
ls2 = [9, 1, 4, 2, 0, 0, 1]

def two_lists(ls1, ls2):
    one_set = set(ls1)
    two_set = set(ls2)
    both = one_set.intersection(two_set)
    if len(both) > 0:
        return(both)

print(two_lists(ls1, ls2))

"""
# OR
def find_shared(ls1, ls2):
    return set(ls1).intersection(set(ls2))

print(find_shared(ls1, ls2))
"""
"""
# OR
def find_shared2(ls1, ls2)
    tmp = []
    for n in ls1:
        for i in ls2:
            if n == i:
                tmp.append(n)
                break
    return tmp

print(find_shared(ls1, ls2))
"""
  

# write a function that checks for the larges number 

# palindrome from 1*1 up to x*y 

# example 1*11 is a 11 a palindrome, the  

# function should take an x and a y and  

# only give you back the largest 

def find_number_pal(x, y):
    return max() #given a list, gives largest element

    print([i*j for i in range(1, x+1) for j in range(1, y+1)])
find_number_pal(3, 4)