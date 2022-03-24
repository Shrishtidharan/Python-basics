s="Shiru"
v=s[::-1]
if(s==v):
    print("True",v)
else:
    print("False,its not a palindrome")
x = "malayalam"
 
w = ""
for i in x:
    #Since i +w every charecter is appended before w
    w = i + w
 
if (x == w):
    print("Yes",w)
else:
    print("No")