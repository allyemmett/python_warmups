#  Write a program that asks for a password and if you guess it right
#  access granted otherwise exit()

pass_guess = input("Password: ")

if pass_guess == "password123":
    print("Access Granted")
else:
    exit(pass_guess)

#  Write a program that asks the user for a number n and prints the sum of the numbers 1 to n 

up_til = int(input("Give me a number\n>" )) # "\n" will create a new line with a carrot. Look up Escape Characters for more
# need "int" to turn into integer, if without then will be string & operators will not work.
cur_num = 1
total = 0

while(cur_num <= up_til):
    total += cur_num
    cur_num += 1

print(total)

