def brute(s1:str,s2:str):
    n = len(s1)
    if s1 == s2:
        return True
    
    diffs = 0
    s1_mpp = [0]*26
    s2_mpp = [0]*26

    for i in range(n):
        if s1[i] != s2[i]:
            diffs += 1
        
        if diffs > 2:
            return False
    
    for char in s1:
        s1_mpp[ord(char) - ord('a')] += 1

    for char in s2:
        s2_mpp[ord(char) - ord('a')] += 1

    for i in range(26):
        if s1_mpp[i] != s2_mpp[i]:
            return False
        
    return True
        

def optimal(s1:str,s2:str):
    n = len(s1)
    if s1 == s2:
        return True
    
    diffs = 0
    first_idx = 0
    second_idx = 0

    for i in range(n):
        if s1[i] != s2[i]:
            diffs += 1

            if diffs > 2:
                return False
            elif diffs == 1:
                first_idx = i
            else:
                second_idx = i

    return s1[first_idx] == s2[second_idx] and s1[second_idx] == s2[first_idx]