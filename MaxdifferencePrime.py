"""Write a program that takes a range of integers as input and finds the difference between the largest and 
smallest prime numbers within that range. Implement a function maxpdis(l, r) that returns the desired difference.
Additionally, implement a helper function checkPrime(num) that determines whether a given number is prime or not. 
The program should prompt the user to enter the number of queries, followed by the lower and upper bounds of each query range. 
Finally, it should output the calculated difference for each query."""
def diff(stnum,lstnum):
    primeNumList=[]
    result = 0
    for num in range(stnum,lstnum+1):
        if isPrime(num) and num >1:
            primeNumList.append(num)
    primeNumList.sort()
    result= primeNumList[-1] - primeNumList[0]
    return result
def isPrime(num):
    for z in range(2,num//2 + 1):
        if num%z == 0:
            return False
    return True
gg=int(input("The number of queries -- "))
for z in range(gg):
    stnum=int(input("Start num - "))
    lstnum=int(input("End num - "))
    print("The differnce between largest and smallest prime in given range is - ",diff(stnum,lstnum))
