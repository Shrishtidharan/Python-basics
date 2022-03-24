def fib(x):
    a=0
    b=1
    
    if x ==0:
        return 0
    elif x==1:
        return 1
    else:
        print(a)
        print(b)
        for i in range(2,x+1):
            c=a+b
            a=b
            b=c
    print(b)
         
print(fib(9))        
    