

def Wrapper(i):

    for _ in range(i):
        dataDict = init()
        returnValue = solution(dataDict)
        print(f'returnValue : {returnValue}')

def init():
    n = int(input().strip())
    dataDict = {}
    for _ in range(n**2):
        s, l1, l2, l3, l4 = list(map(int, input().split(' ')))
        dataDict[s] = [l1, l2, l3, l4]

    return dataDict

def solution(dataDict):
    pass



def returnCloseAbs(pos1, pos2): # y, x

    return abs(pos1[0]-pos2[0]), abs(pos1[1]-pos2[1])

if __name__ == '__main__':

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 2
    Wrapper(T)