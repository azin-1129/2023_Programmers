def solution(s):
    if len(s)==4 or len(s)==6:
        for st in s:
            if ord(st)>ord('9'): # 알파벳 포함
                return False
    else:
        return False
    return True