def brute(derived:list[int]):
    n = len(derived)
    original = [0] * n

    for i in range(1,n):
        original[i] = original[i-1] ^ derived[i-1]

    if original[-1] ^ derived[0] == derived[-1]:
        return True

    original[0] = 1
    for i in range(1,n):
        original[i] = original[i-1] ^ derived[i-1]

    if original[-1] ^ derived[0] == derived[-1]:
        return True
    
    return False


def optimal(derived:list[int]):
    xor = 0
    for num in derived:
        xor ^= num
    return xor == 0


derived = [1,1,0]
print(brute(derived))
