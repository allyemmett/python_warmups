# Write a function that takes in a list
# and returns items that are unique only
# f([1, 2, 3, 2, 5]) -> [1, 3, 5]

def unique_only(list_of_numbers):
    unique_list = []
    for item in list_of_numbers:
        if list_of_numbers.count(item) == 1:
            unique_list.append(item)
    return unique_list
    
list_of_numbers = [1, 2, 3, 2, 5]

print(unique_only(list_of_numbers))

"""
Solution with list comprehension

def find_uniq(ls):
    return [x for x in ls if ls.count(x) == 1] # reads as "I want x back for all things in list if only one quantity of"

print(find_uniq([1, 2, 3, 2, 5]))
"""
"""
Other solution with dictionary & element value

def find_uniq2(ls):
    tmp = {}
    for i in ls:
        if tmp.get(i): #get method returns value or no
            tmp[i].append(i)
            else:
                tmp[i] = [i]
    print(tmp)

    ret = []
    for k, v in tmp.items(): # key, value
        if len(v) == 1:
            ret.append(k)
    return ret

print(find_uniq2([1, 2, 3, 2, 5]))
"""
"""
OR make ret = [] into list comprehension

ret = [k for k, v in tmp.items() if len(v) == 1]
return ret

"""