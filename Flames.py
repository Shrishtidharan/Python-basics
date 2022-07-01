x = input("Enter n1 - ")
y  = input("Enter n2 - ")
comman=[]
xs,ys=list(x),list(y)
ans = ['Friends','Love','Affection','Marriage','Enemy','Sister']
count = 0
for c in xs:
    if c in ys:
        count+=1
        comman.append(c)
print("Comman charecters are - ",comman)
        
print("Comman chrevter count",count)

while(len(ans)>1 ):
    rr= count%len(ans)-1
    if rr>=0:
        right = ans[rr + 1 : ]
        left =  ans[ : rr]
        ans=right+left
    else:
        ans = ans[ : len(ans) - 1]
    

print( "Status is - ",ans[0])


