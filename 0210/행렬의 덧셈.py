def solution(arr1, arr2):
    temp=[[0]*len(arr1[0]) for _ in range(len(arr1))]
    
    for x in range(len(arr1)):
        for y in range(len(arr1[0])):
            temp[x][y]=arr1[x][y]+arr2[x][y]
    return temp