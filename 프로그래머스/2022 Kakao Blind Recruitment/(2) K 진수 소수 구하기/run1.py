import re

def isPrime(stingNum, k):
    if stingNum == '': return False
    intNum = int(stingNum)

    if intNum == 2 or intNum == 3: return True  # 2 or 3 은 소수
    if intNum % 2 == 0 or intNum < 2: return False  # 2의 배수이거나 2보다 작은 값인 경우 소수가 아님

    for i in range(3, int(intNum ** 0.5) + 1, 2):
        if intNum % i == 0:
            return False
    return True

def separate(string, k):
    #print(f'initial string : {string}')
    totalPrimeCount = 0
    reObj = re.compile('0([1-9]*)|([1-9]*)0|0([1-9]*)0|([1-9]*)')

    while string:
        rePattern = reObj.match(string).group()
        #print(f'v : {rePattern}')

        rePatternReal = rePattern.replace('0','')

        if isPrime(rePatternReal, k):
            totalPrimeCount += 1

        string = string[len(rePattern):]

    return totalPrimeCount


def solution(n, k):


    converted = convert_to_k(n, k)
    #print(f'converted : {converted}')


    length = separate(converted, k)
    #print(f'length : {length}')

    return length


def convert_to_k(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]


if __name__ == '__main__':
    n = 437674
    k = 3
    solution(n, k)