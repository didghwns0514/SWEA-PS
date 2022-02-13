import re

globalPrimeSet = set()
globalNotPrimeSet = set()

def isPrime(stingNum, k):
    global globalPrimeSet, globalNotPrimeSet
    if stingNum in globalPrimeSet:
        return True
    if stingNum in globalNotPrimeSet:
        return False

    #intNumber = int(stingNum, k)
    intNumber = int(stingNum)
    if stingNum == '1' or '0' in stingNum:
        globalNotPrimeSet.add(stingNum)
        return False

    for j in range(1, intNumber):
        if j ==1:continue
        if intNumber % j == 0:
            globalNotPrimeSet.add(stingNum)
            return False

    globalPrimeSet.add(stingNum)
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

    for idx_end in range(0, stringLength):
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

    return len(primeHistory)


def solution(n, k):


    converted = convert_to_k(n, k)
    print(f'converted : {converted}')


    length = separate2(converted, k)
    print(f'length : {length}')

    return length


def convert_to_k(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]

if __name__ == '__main__':
    n = 110011
    k = 10
    solution(n, k)