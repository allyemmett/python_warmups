# Write a function that builds a pyramid based on a number given 
"""
if 3 is given it would be

*
**
***
"""
def pyramid_shape(n):
    ls = []
    for i in range(1, n+1):
        ls.append("*"*i)
    print("\n".join(ls))

print(pyramid_shape(4))

"""
OR
def build_pyramid(x):
    counter = 1
    while counter < x:
        print(counter * "*")
        counter += 1

build_pyramid(9)
"""

# Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
"""
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********

"""
"""
def hello_frame(ls):
    row_len = 0
    for i in ls:
        if len(i) > row_len:
            row_len = len(i)
    row_len = row_len + 4
    print(row_len)

    ends = row_len * "*"
    print(ends)
    for i in ls:
        space = row_len - 4 - len(i)
        space_str = space * " "
        print(f"* {i}" + space_str + "*")
    print(ends)
hello_frame(["Hello", "World", "in", "a", "frame"])
"""

# Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?


def rotate_list(ls, offs):
    ofs = offs % len(ls)
    return ls[ofs] + ls[:ofs]

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 8))


