a,b=map(int,input().split())
z=1
while 1:
    m=a*z
    if m%b==0:
        print(m)
        break
    z+=1
    