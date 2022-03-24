#Bubble sort compares every adjacent elements
#number of iteration is length of element-1
#At end of each iteration,largest element is sorted at the last position
#No need to check that
def bbsort(nums):
    #outer loop-Number of iterations
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums [j] > nums [j+1]:
                #Swapping
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[28,12,34,100,5,4,2,1]
bbsort(nums)
print(nums)