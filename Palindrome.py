a=int(input())
b=a
res=0
while a>0:
    r=a%10
    res=res*10+r
    a//=10
if res==b:
    print("True")
else:
    print("False")