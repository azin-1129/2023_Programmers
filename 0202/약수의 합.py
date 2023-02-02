n=int(input())

div=[]

for i in range(1,int(n**0.5)+1):
    if n%i==0:
        div.append(i)
        if i**2!=n:
            div.append(n//i)

answer=sum(div)

print(div,answer)