import re

def isPrime(stingNum, k):
    #intNumber = int(stingNum, k)
    intNumber = int(stingNum)
    if stingNum == '1' or '0' in stingNum:
        return False

    for j in range(1, intNumber):
        if j ==1:continue
        if intNumber % j == 0:
            return False
    return True

def separate2(string, k):
    primeHistory = []
    stringLength = len(string)
    idx_start = 0
    idx_end = 0

    if len(string) == 1:
        if isPrime(string, k):
            return 1
        else: return 0

    for idx_end in range(1, stringLength):
        if not idx_end >= idx_start: continue
        if idx_end == stringLength - 1: # no next
            tmpSubStr = string[idx_start:idx_end + 1]
            if isPrime(tmpSubStr, k):
                primeHistory.append(tmpSubStr)
                break
        else:
            if string[idx_end+1] == '0':
                tmpSubStr = string[idx_start:idx_end+1]
                if isPrime(tmpSubStr, k):
                    primeHistory.append(tmpSubStr)
                    # idx_start = idx_end + 2
                else:
                    pass
                idx_start = idx_end + 1
                while string[idx_start] == '0':
                    idx_start += 1
            else:
                continue

    return primeHistory


def solution(n, k):


    converted = convert_to_k(n, k)
    print(f'converted : {converted}')


    partition = separate2(converted, k)
    print(f'partition : {partition}')

    return len(partition)


def convert_to_k(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]

if __name__ == '__main__':
    n = 10
    k = 10
    solution(n, k)