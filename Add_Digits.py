def t(a):
    while a>9:
        a=(a%10)+(a//10)
    return a
a=int(input())
print(t(a))
    