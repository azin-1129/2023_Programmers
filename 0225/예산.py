def solution(d, budget):
    d.sort()
    cnt=0
    
    for ds in d:
        budget-=ds
        if budget<0:
            break
        cnt+=1
    
    answer = cnt
    return answer