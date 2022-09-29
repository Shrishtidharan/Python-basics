def isPrime(x):
    flag = True
    for a in range(2,x//2 + 1):
        if x % a == 0:
            flag = False
            break
    return flag
arr = [2,4,5,7,8]
sum = 0
for qq in arr:
    if isPrime(qq):
        print(qq,end="  ")
        sum += qq
print("Sum of prime number is - ",sum)
