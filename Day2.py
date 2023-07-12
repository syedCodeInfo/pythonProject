# Type conversion
# implicit, explicit

apple_amount ="10"
orange_amount = "20"
#casting string to float conversion
sum =  int(apple_amount)+int(orange_amount)

print(sum)

# print with end whitespace
print("New year",2023,"It is coming", sep='. ')

#Print Concatenated Strings
print("Hello "+"World !!!")


x =5
y =10
print(
    "This is x {} and this is y {}". format(x,y)
)

#input user get
'''name = input("Enter the name: ")
print("Your number is:",name)'''


# operators
#addition

''''Arithmetic operators
Assignment Operators
Comparison Operators
Logical Operators
Bitwise Operators
Special Operators'''''

#Arithmetic operators
add= 5+10
sub= 5-10
mul= 5*10
div = 5/10
floor_div = 10//3
power =6**2
print("add {}, sub = {},mul={}, div={}, floor_div={}, power={} ".format(add,sub,mul,div,floor_div,power))

#Assignment Operators
a1 = 10
a1 +=10
print("Assignment operator",a1)

'''-=	Subtraction Assignment	a -= 3 # a = a - 3
*=	Multiplication Assignment	a *= 4 # a = a * 4
/=	Division Assignment	a /= 3 # a = a / 3
%=	Remainder Assignment	a %= 10 # a = a % 10
**=	Exponent Assignment	a **= 10 # a = a ** 10'''


#Comparison Operators
mango_count = 5
apple_Count =10
'''print(mango_count!=apple_Count)
print(mango_count>apple_Count)
print(mango_count<apple_Count)
print(mango_count>=apple_Count)
print(mango_count<=apple_Count)'''

#Logical Operators
print( True and False)
print( True or False)
print( not False)

#bitwise operator

'''&	Bitwise AND	x & y = 0 (0000 0000)
|	Bitwise OR	x | y = 14 (0000 1110)
~	Bitwise NOT	~x = -11 (1111 0101)
^	Bitwise XOR	x ^ y = 14 (0000 1110)
>>	Bitwise right shift	x >> 2 = 2 (0000 0010)
<<	Bitwise left shift	x << 2 = 40 (0010 1000)'''
if(mango_count==10 & mango_count>10):
    print("it is true")
else:
    print("it is false")


xx= 10
print(~x==11)

# special Operators is, isnot
xx = 100
yy = 200

print(xx is not yy)


#Write a program to print the given number is odd or even.
#Write a program to find the sum of two numbers. a=100, b=200
# comparision operator two number equal or not