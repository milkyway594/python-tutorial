# break statement

for item in range(1, 6):
    if item == 3:
        break
    print(item)
print("the end")


# write a program to print a positive number when a user inputs and break when a user inputs a negative number
while True:
     number = float(input("enter a number"))
     if number < 0:
        break
     print ("you've entered: ", number)


# continue statement
for i in range(5):
    number = float(input("enter a number " ))
    if number < 0:
        continue
    print (number)

# exercise
# create a program so that all items of the language list are printed except swift and c++
languages =["python","java","swift","c","c++"]

for language in languages :

    if language in ["swift" ,"c++"] :

       continue
    print(language)