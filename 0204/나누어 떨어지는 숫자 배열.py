def solution(arr, divisor):
    sol=[i for i in arr if i%divisor==0]
    
    if len(sol)==0:
        return [-1]
    else:
        return sorted(sol)