# Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].
"""
def num_to_list(num):
    returned_list = [int(i) for i in str(num)] # converts numbers to string
    return returned_list

print(num_to_list(1234))
"""
"""
OR
def num_to_list(num):
    out = []
    num2 = 0
    while(num != 0):
        num2 = num % 10
        out.insert(0, num2)
        num = int(num/10)
    return out
"""



# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.
"""
 # will return as [[1, 2, 3, 4][5, 6, 7, 8]]
def lists_merged():
    first_list = [1, 2, 3, 4]
    second_list = [5, 6, 7, 8]
    merged_list = [first_list, second_list]
    return merged_list

print(lists_merged())
"""
"""
CONCATENATION:
def lists_merged():
    first_list = [1, 2, 3, 4]
    second_list = [5, 6, 7, 8]
    merged_list = first_list + second_list
    return merged_list

print(lists_merged())
"""






# Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

def combining_lists():
    first_list = [1, 2, 3, 4]
    second_list = [5, 6, 7, 8]
    alternated_list = []