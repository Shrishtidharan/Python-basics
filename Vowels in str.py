x =input().lower()
vowels={"a", "e", "i", "o", "u"}
scount={}
for z in range(len(x)):
    if x[z]  in vowels:
        scount[x[z]] = 1+scount.get(x[z],0)
print(scount)
