pos=0
def bsearch(num):
    lp=0
    up=len(numarr)-1
    while(lp<=up):
        # // - integer division
        midpos=(lp+up)//2
        if(numarr[midpos]==num):
            globals()['pos']=midpos
            return "Found at"
            break
        else:
            if(se>numarr[midpos]):
                lp=midpos+1
            else:
                up=midpos-1
               
    return "Not Found - "
numarr=[2,4,6,12,45,90,100]
se=int(input("Enter element to search - "))
print(bsearch(se),pos)
