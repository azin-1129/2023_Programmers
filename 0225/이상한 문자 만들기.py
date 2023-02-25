def solution(s):
    words=s.split(' ')
    
    for i in range(len(words)):
        word=words[i]
        print('word:',word)
        
        temp=[]
        for j in range(len(word)):
            if j%2==0: # 짝수 인덱스
                temp.append(word[j].upper())
            else:
                temp.append(word[j])

        print('temp:',temp)
        
        words[i]=''.join(temp)
    answer=' '.join(words)
    print(answer)
    return answer

solution('try hello world')