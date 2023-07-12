#python namespace

'''Local (function), Global(Module), built-in'''
global_x = 100

def function1():
    local_y = 200
    print("i am local variable:",local_y)
    print(global_x)


print(global_x)
function1()

#python flow controls
'''if else, for, while, break , continue, and pass'''

'''user_input = float(input("Enter the mark?"))
#90 A, 75 B,65 C
if(user_input>90):
    print("A Grade")
elif(user_input>75 and user_input<90):
    print("B Grade")
elif(user_input>65 and user_input<75):
    print("C Grade")
else:
    print("Sorry you are failed")'''

# looping -- for and while
animals = ["lion","tiger","Shepart"]
for item in animals:
    print(item)
for item in range(10):
    print(item)






#break and continue

for i in range(5):
    if i==3:
        continue
    print(i)

#pass

n = 10
if n>10:
    pass
print("Hello world")

# function declaration

#calculator add, subtraction, multiplication
x = 10
y = 10
print("--------Calculator----------------")
def addition(x,y):
    z =x+y
    return z

def subtraction(x,y):
    z =x-y
    return z

def multiplication(x,y):
    z =x*y
    return z

#calling the function
add_output = addition(x,y)
sub_output = subtraction(x,y)
mul_output = multiplication(x,y)
print("add:{}, sub:{},mul:{}".format(add_output,sub_output,mul_output))
print("--------End Calculator----------------")

# Library function , sqrt, print,math
import math
sr_root = math.sqrt(25)
print(sr_root)
sqrt = pow(2,3)
print(sqrt)

