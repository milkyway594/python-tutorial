# dictionary
person1={"key1": 10, "key2": 20}
# editing an item
person1["key1"]="dennis"

# inserting another key
person1["key3"]=[40,50]

# removing an item
person1.pop("key3")


print(person1)
# printing a single item
print(person1["key1"])

print(person1.get("key1"))

print(person1.get("key3",["10"]))


person1["key1"]=["dennis"]


# # iterating through a dictionary

for key in person1:
    print(key)
    print(person1[key])


# sets in python
animals = {"dogs" , "cats", "tiger", "cats"}
print(animals)

# for empty set
animals = set()
print(animals)

# printing set using the set function
animals = set(["dogs" , "cats", "tiger", "cats"])
print(animals)

# adding items to a set
animals = {"dogs" , "cats", "tiger", "cats"}
animals.add("monkey")
print(animals)

# adding a list to a set
animals = {"dogs" , "cats", "tiger", "cats"}
wild_animals =["lion", "boar", "bear"]
animals.update(wild_animals,)
print(animals)

# removing item from a set
# using the discard method
animals = {"dogs" , "cats", "tiger", "cats"}
animals.discard("cats")
print(animals)

# using the remove method
animals = {"dogs" , "cats", "tiger", "cats"}
animals.remove("cats")
print(animals)

# removing all items in a set using clear method
animals = {"dogs" , "cats", "tiger", "cats"}
animals.clear()
print(animals)

# how to check if an item is in a set
animals = {"dogs" , "cats", "tiger", "cats"}
print ("cats" in animals)

# iterating through a set
for animals in animals:
    print(animals)

# union of set
domestic_animals={"dogs,", "cats", "elephant"}
wild_animals={"lion", "tiger", "elephant"}

animals = domestic_animals.union(wild_animals)
print(animals)

# union of set using pipe symbol|
domestic_animals={"dogs,", "cats", "elephant"}
wild_animals={"lion", "tiger", "elephant"}

animals = domestic_animals | (wild_animals)
print(animals)

# intersection of set
domestic_animals={"dogs,", "cats", "elephant"}
wild_animals={"lion", "tiger", "elephant"}

animals = domestic_animals.intersection(wild_animals)
print(animals)

# intersection of set using &
domestic_animals={"dogs,", "cats", "elephant"}
wild_animals={"lion", "tiger", "elephant"}

animals = domestic_animals&(wild_animals)
print(animals)


