#list comprehension
#creating a new list based on the old list
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "k" in x]

print(newlist)
numlist=[s for s in range(1,10)]
print(numlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)