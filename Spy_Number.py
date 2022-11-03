num=int(input())
a=num
s=0
s1=1
while a>0:
    se=a%10
    s=s+se
    s1=s1*se
    a//=10
if s1==s:
    print("Spy Number")
else:
    print("Not Spy Number")
    