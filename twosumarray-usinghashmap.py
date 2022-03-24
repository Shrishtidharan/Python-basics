arr=[]
hmap={}
 #hashmap is initially empty  -- value:index
for i in range(6):
    ip=int(input())
    arr.append(ip)
target= int(input("Enter the target -"))
# here it is index and vl is value in array with respect to insex
for it,vl in enumerate(arr):
    diff=target-vl
    if diff in hmap:
        print( [hmap[diff],it])
    hmap[vl]=it
