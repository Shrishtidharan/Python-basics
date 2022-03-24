#by defauly it takes only string
ss=input("Enter the word:")
li=list(ss)
#print(li)
newlist=[]
for x in li:
    if "a" in x or "e" in x or "i" in x or "o" in x or "u" in x:
         newlist.append(x)
         li.remove(x)
print("The list after removing vowels is:",li)
print("The vowels found in the word is",newlist)

