# [Lists, Strings] Challenges
# Write a function that returns the largest element in a list

def get_largest(col):
    if col:
        tmp = col[0] # check if anything in collection
        for i in col:
            if tmp < i:
                tmp = i
        return tmp
    return None

print(get_largest([1, 2, 3, 4]))



# Write a function that checks whether an element occurs in a list

x = [1, 2, 3, 4, 5]

def is_in(ls, elm): 
    # could do "return ls in elm"
    for item in ls:
        if item == elm:
            return True
    return False

print(is_in(x, 3))


# Write a function that returns the elements of odd positions in a list

# f(x) -> x if odd

def odd_pos(ls):
    return ls[1::2] # Array splicing, start on first index and stop on end. "hopping" with format [start : stop : step]
    
print(odd_pos(x)) # returns [2, 4],


# Write a function that computes the running total of a list

def total_up_list(ls):
    total = 0 # need total = 0 to make += i an integer
    for i in ls:
        total += i # only can do this because of line 44
    return total

print(total_up_list([1, 2, 3, 4, 5, 6]))

# Write a function that tests whether a string is a palindrome

# "racecar" <=> "racecar" -> True
#  "Justin" <=> "Justin" -> False

# check_this = "racecar"
# print(check_this == check_this[::-1]) # [::-1] reverses word

def is_palindrome(s):
    i = 0
    j = len(s) -1 # need -1 because index of word begins with 0
    while i < j:
        if s[i] != s[j]: # i is first index and j is last
            return False
        i += 1 # i = i + 1 (reassigns i)
        j -= 1 #
    return True


check_this = "Justin"
print(is_palindrome(check_this))


# [BONUS SPICY CHALLENGE]
# Write a function that reverses a list, if you can do it in place
def rev_inplace(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

y = [1, 2, 3, 4, 5, 6, 7]
print(y)
rev_inplace(y)
print(y)

start, stop = 0, 9
start, stop = stop, start # can use as a method for flipping
print(start, stop)

