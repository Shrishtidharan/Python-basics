li=[19,4,2,100]
print("the list is :",li)
print("lenghth is ",len(li))
ls=["Suriya",46,"Vijay",48]
print("list with dfferent data type",ls)
#list constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
#list indexing
print(li[1:3])
ac=["Suriya","Vijay","Rajini","Ajith"]
#changing the items with indexing
ac[1:2]=["Dhanush","kamal"]
print(ac)
# append -add element at the end of the list
ac.append("Vijay")
print("the new ac is :",ac)
#Insert at the specific position use insert method
ac.insert(0,"Karthi")
print("The ac after insert methid is",ac)
ls.extend(ac)
print(ls)
# we can also extend different objects like tuple(that should be indexed)
thistuple = ("kiwi", "orange")
ac.append(thistuple)
print("the ac list is extended with tuple:",ac)
#remove the list item with the value
ac.remove("Karthi")
print(ac)
# pop remove the list item with the index
#if index not specified remove the last item
ac.pop(3)
print("the list after pop is:",ac)
ac.pop()
print("list after pop is",ac)
#del -delete entire list or with specified index
del ls
#clear method removes all the element but retains the list
thislist.clear()
print(thislist)