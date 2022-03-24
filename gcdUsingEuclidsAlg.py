#Euclids alogorith recursion
def gcd(n1,n2):
    if n1==0:
        return n2
    else:
        return gcd(n2%n1,n1)
x=int(input("Enter the num1--"))
y=int(input("Enter the num2--"))
print(gcd(x,y))