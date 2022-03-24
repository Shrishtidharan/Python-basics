#Program to Sort the list based on how close the number is to 50:
def myfunc(n):
  #abs is a method that returns absolute value without the sign
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)