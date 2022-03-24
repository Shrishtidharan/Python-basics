#Selection sort is efficient than bubble sort,
#Swapping occurs only once per iteration,Minimum value is found at end of each iteration
#and sorted

def selectionsort(numarr):
    #outer for loop for assigning minimu value to first
    for i in range(len(numarr)):
        minpos=i
        for j in range(i+1,len(numarr)):
            #Checking the assigned value with every element tp find min
            if numarr[j]<numarr[minpos]:
                #after this iteration min value is sorted at first
                minpos=j
        #Swapping ith element with min element
        temp=numarr[i]
        numarr[i]=numarr[minpos]
        numarr[minpos]=temp
numarr=[5,3,7,2,8,9,1]
selectionsort(numarr)
print(numarr)
