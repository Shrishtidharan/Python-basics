n = int(input("Enter size of array- "))
arr = list(map(int,input().split()))
ct = int(input("Enter number of repetation - "))
ans =[]
for elem in arr:
    if arr.count(elem) == ct:
        ans.append(elem)
print(min(ans))
