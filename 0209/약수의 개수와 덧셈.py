def solution(left, right):
    sum=0
    
    for i in range(left,right+1):
        if int(i**0.5)**2==i: # 홀수
            sum-=i
        else:
            sum+=i
    return sum