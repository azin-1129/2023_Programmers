def solution(n, m):
    answer = [0,0]
    Y=[]
    
    for y in range(1,int(n**0.5)+1):
        if n%y==0:
            Y.append(y)
            if n%(n//y)==0 and y**2!=n:
                Y.append(n//y) # n의 약수 Y
    
    Y=sorted(Y, reverse=True) # 내림차순 정렬
    
    for y in Y:
        if m%y==0: # 최대 공약수
            answer[0]=y
            break
            
    if n>m:
        if n%m==0:
            answer[1]=n
        else:
            for i in range(2,m+1):
                if (n*i)%m==0:
                    answer[1]=n*i
                    break
    elif n<m:
        if m%n==0:
            answer[1]=m
        else:
            for i in range(2,n+1):
                if (m*i)%n==0:
                    answer[1]=m*i
                    break
    else:
        answer[1]=m
        
    
    return answer