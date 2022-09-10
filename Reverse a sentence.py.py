x = input("Enter str - ")
strlis = x.split()
print(strlis)
reslis= []
for i in range(len(strlis)-1,-1,-1):
    reslis.append(strlis[i])
print(type(strlis))
print(reslis)
res = " ".join(reslis)
print(res)

