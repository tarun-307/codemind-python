a=int(input())
g=a
b=a*a
s=0
while b>0:
    r=b%10
    s=s+r
    b//=10
if s==g:
    print("Neon Number")
else:
    print("Not Neon Number")
    