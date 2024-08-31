# function
def greet(name):
    print('hello', name)
    print("how do yo do")

greet()

# argument

greet("jack")

# passing multiple argument

def add_numbers(n1, n2):
    suma = number1 + number2
    print(suma)

number1 = 3
number2 = 4

add_numbers(number1, number2)

# return value from a function
def add_numbers(n1, n2):
    result = number1 + number2
    return result

number1 = 3
number2 = 4

result = add_numbers(number1, number2)
print("the sum is", result)

# function to find average marks

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    average_marks = sum_of_marks / total_subject
    return average_marks

def compute_grade(average_marks):
     if average_marks >= 80:
         grade ="A"
     elif average_marks >= 60:
         grade = "B"
     elif average_marks >= 50:
             grade = "C"
     else:
         grade= "F"

     return grade


marks =[55, 64, 75, 80,65]
average_marks = find_average_marks(marks)


print("your average mark is : ",average_marks )

grade = compute_grade(average_marks)
print ("your grade is: ", grade)

# define two functions to add two numbers and multiply two numbers

def add_number(n1, n2):
    add = number_1 + number_2
    return add

def multiply_number(n1,n2):
    product = number_1 * number_2
    return product


number_1 = float(input("enter the first number: " ))
number_2 = float(input("enter the second number: " ))

add = add_number(number_1,number_2)
print ("the addition of the number entered is: ", add)


product = multiply_number(number_1, number_2)
print ("the addition of the number entered is: ", product)