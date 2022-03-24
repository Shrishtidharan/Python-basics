n=int(input())
if(0<n<500):
    a=0
    b=1
    l=[a,b]
    while b<n+1:
        #parallel assigning of values
        a,b=b,a+b
        l.append(b)
    l.remove(0)
    print(l[n])