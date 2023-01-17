def isPrime(num):
    for x in range(2,num//2+1):
        if num%x==0:
            return False
    return True
sumn=0
numlis=list(map(int,input().split()))
for vl in numlis:
    if isPrime(vl) and vl!=1 and vl!=0:
        print("The prime numbers are -" ,vl)
        sumn+=vl
print(sumn)
    
