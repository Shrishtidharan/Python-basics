arr=[]
for x in range(6):
    cr=int(input())
    arr.append(cr)
tr=int(input("Enter the target num - "))
flag=0
for x in range(0,len(arr)):
    for y in range(1,len(arr)):
        if(arr[x]+arr[y]==tr):
            flag=1
            print(x,y)
            break
if(flag==0):
    print("No combination exists...")    
        
        
