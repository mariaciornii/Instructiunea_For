a=eval(input("numarul a este egal cu "))
b=eval(input("numarul b este egal cu "))
if a%2!=0:
    for x in range(a, b+1, 2):
        print(x)
elif a%2==0:
    for b in range(a+1, b+1, 2):
        print(b)