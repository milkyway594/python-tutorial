print('hello world')
print ("python 3 is awesome")

print(5)
print(34.5)

city="lagos"
print(city)

destination_city="new york"
city = destination_city
print(city)

# ASSIGNING IDENTIFIER
print("my","city:", city )

# GETTING USER INPUT
name=input("enter name: ")
print (name)

# CHECKING OF TYPE OF DATA BEING INPUTTED

# EXAMPLE 1
number=input("enter number: ")
print(type(number))

# EXAMPLE 2
number1 = 5.5
print(type(number1))

# DATATYPE

# INT
number=int(input("enter number: "))
print(type(number))

# FLOAT
number=float(input("enter number: "))
print(type(number))

# comment - USE # TO COMMENT ON CODE

# operators
# addition +
# subtraction -
# multiplication *
# exponent **
# division /
# floor division //
# remainder %

# EXAMPLE

x=5
result = x * 6
print(result)

# concatenation of strings

str1 =("hey ")
str2 =("jude")
res = (str1 + str2)
print(res)


# assignment operator

# EXAMPLE
x= 10
x += 10 # x= x+10
x -= 10# x= x-10

# EXERCISE

# MY SOLUTION
fee = 4535
discount = 10/100
discount = fee * discount
amount_to_pay = fee - discount
print(amount_to_pay)

# MUNIR SOLUTION
print("enter your distance in km: " )
distance = float(input())
distance = (distance * 0.621371)/1
print( "your distance in miles is : ", distance)

distance_km = float(input("enter the didtance: "))
conversion_rate = 0.621371
distance_miles = distance_km * conversion_rate
print("the distance in miles is: ", distance_miles)

# boolean
result1 = True
result2 = False

print(result1, result2 )

# comparison operator
# less than <
# greater than >
# equal !=
# not equal ==
# greater than or equal to >=
# less than or equal to <=



number = 6
print(number!=10)

# logical operators
# and true if both operands are true
# or  true if either of the operands are true
# not true if the operand is false




# if-else statement
x= int(input("enter the value of x: "))
if x ==50:
    print("it is higher")
else:
    print("it is lower")

# if elif
#FIRST EXAMPLE

x= int(input("enter the value of x: "))
if x ==50:
     print("it is higher")
elif x<=10:
     print("it is medium")

else:
     print("it is lower")

# SECOND EXAMPLE
number = float(input ("your desired number: "))
if  number >=0:
        print("the number is positive")
elif number ==0:
        print("the number is 0")
else:
        print("the number is negative")

# WHILE LOOP

# EXAMPLE

count = 5
while count<= 10:
    print(count)
    count= count + 1

# EXAMPLE 2
# COLLECT THE INPUT OF USER TO PRINT THE MULTIPLE OF NUMBER 1 THROGH 10

number = int(input( "enter the number"))
count = 1
while count <= 10:
    product = number * count

    print(number, "x", count,"=",product,)
    count = count + 1