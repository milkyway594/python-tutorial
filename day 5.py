# default argument

# def add_numbers(n1 = 100, n2 = 1000):
#     sum = n1 + n2
#     return sum
#
# sum = add_numbers(2.3)
# print (sum)
#
# # keyword argument
# def greet( name, message):
#     print ("hello", name)
#     print(message)
#
# greet("jake", "how are you doing")
# greet (name = "rowland", message ="howdy")


# local variables
# these are variables created inside a function and can omly be used with that function

# global variables
# it is declared outside a function and can be used outside a function


# list and tuples

# a list of integers
# numbers=  [1, 2, 3, 4 ]
#
# # mixed list
# random_list = [1, "two", 3, "four"]
# print(random_list)
# length =len(random_list)
# print(length)

# accessing list elements

languages = ["python", "java", "swift", "c", "c++"]

print(languages[2])

# negative indexing - -1,-2,-3....

languages = ["python", "java", "swift", "c", "c++"]

print(languages[-2])

# slicing a list
languages = ["python", "java", "swift", "c", "c++"]

print(languages[1:5])

# changing of items in a list
languages = ["python", "java", "swift", "c", "c++"]
languages [1] = "ruby"
print(languages)

# in statement
# print true if an element is present in a list and prints false otherwise
languages = ["python", "java", "swift", "c", "c++"]

print ("python" in languages)


# iterating through a list
for language in languages:
    print(languages)

# list methods
languages = ["python", "java", "swift", "c", "c++"]
# adding a new element
languages.append("rust")
# inserting an element into the selected index
languages.insert(3,"kotlin")
# removing an element
languages.remove("c++")
# copying an entire list
languages1 = languages.copy()
print (languages)

print (languages1)


# tuples
numbers = (21, -5, 6, 7)
print(numbers )


