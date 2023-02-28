def solution(s, n):
    st=list(s)
    
    for i in range(len(st)):
        if st[i]==' ':
            continue

        if ord('a')<=ord(st[i])<=ord('z'): # 소문자일 때
            temp=ord(st[i])+n
            
            if temp>ord('z'):
                st[i]=chr(ord('a')-1+temp-ord('z'))
            else:
                st[i]=chr(temp)
                
        elif ord('A')<=ord(st[i])<=ord('Z'): # 대문자일 때
            temp=ord(st[i])+n
            
            if temp>ord('Z'):
                st[i]=chr(ord('A')-1+temp-ord('Z'))
            else:
                st[i]=chr(temp)

    return ''.join(st)