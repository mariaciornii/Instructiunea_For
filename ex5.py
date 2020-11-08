n=eval(input("numarul n este egalu cu: "))
sum=0

for a in range(0, n+1):
    if ((a%3==0)and(a%5==0)):
        sum+=a
print(sum)