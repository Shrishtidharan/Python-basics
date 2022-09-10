x = input("Enter word to reverse each word -" )
strlis = x.split()
for it,words in enumerate(strlis):
    strlis[it]=words[::-1]
print(strlis)
res= " ".join(strlis)
print(res)
    
    


