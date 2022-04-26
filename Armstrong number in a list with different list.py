num = int(input("Enter a number: "))
l=[]
for i in range(num):
    n=int(input())
    l.append(n)

for i in range(num):
    x = str(l[i])
    c= len(x)
    sum = 0
    temp = l[i]
    while temp > 0:
        digit = temp % 10
        sum += digit ** c
        temp //= 10
    if l[i] == sum:
            print(l[i],"is an Armstrong number")
    else:
            print(l[i],"is not an Armstrong number")