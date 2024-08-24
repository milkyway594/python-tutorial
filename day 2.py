# for range
# python sequencing
# example 1
text = "python"
for cha in text:
    print(cha)

# example 2
languages = ["english","french", "spanish"]

for language in languages:
    print(language)

# python range
# example 1
for count in range(1,6):
    print(count)
# example 2
number = int(input("enter an integer: "))
for number in range(1, number):
    print(number)

# multiplication of 6 from 1 to 10 using while loop
count = 10
while count >=1 :
    product = count * 6
    print( "6", " *", count, "=", product)
    count -= 1

# multiplication of 6 from 1 to 10 using while loop
number = int(input( "enter the number"))
count = 10
while count >= 1:
    product = number * count
    print(number, "x", count,"=",product,)
    count = count - 1

# multiplication of 6 from 1 to 10 using for loop
for i in range(1, 13):
    product = i * 6
    print("6", " *", i, "=", product)

# multiplication of 6 from 10 to 1 using for loop
for i in range(13, 0, -1):
    product = i * 7
    print("7", " *", i, "=", product)

# a program to find the sum of numbers from 1 to 100
suma = 0
for i in range(1, 101):
    suma = suma + i
    print("the sum of 1  to  100  is :", suma)