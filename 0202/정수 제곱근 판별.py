n=int(input())

if (n**0.5)%1>0:
    print(-1)
else:
    print(int((n**0.5+1)**2))