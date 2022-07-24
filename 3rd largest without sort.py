x = [1,4,2,19,13,12,89]
f , s, t = x[0],0,0
for v in x:
    if v > f:
        t = s 
        s = f 
        f = v 
    elif v > s:
        t = s
        s = v
    
    elif v>t:
        t = v
print("3rd largest element is - " , t)