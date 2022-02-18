
import copy

def Wrapper(T):

    for _ in range(T):
        N, dataMap, Q, dataL = init()
        returnResult = solution(N, dataMap, Q, dataL)
        print(f'returnResult : {returnResult}')


def init():
    N, Q = list(map(int, input().split(' ')))  # N**2 만큼 / Q 번 수행

    # 데이터 생성
    dataMap = []
    for _ in range(2**N):
        tmpInput = list(map(int, input().split(' ')))
        dataMap.append(tmpInput)

    dataL = list(map(int, input().split(' ')))

    print(f'len(dataMap) : {len(dataMap)}')
    print(f'dataMap : {dataMap}')
    print(f'Q, dataL : { Q, dataL}')

    return N, dataMap, Q, dataL


def solution(N, dataMap, Q, dataL):

    for L in dataL: # 총 Q 번 시행

        tmpWholeBlock = splitForLsize(N, L)
        print(f'L :{L}')
        print(f'tmpWholeBlock : {tmpWholeBlock}')

        for singleBlock in tmpWholeBlock:
            print(f'singleBlock : {singleBlock}')
            rotatedBlock = rotateClockwise90(L, singleBlock)
            print(f'rotatedBlock : {rotatedBlock}')



            # tmpBuffer = dataMap[tBRow]
            # dataMap[tBRow] = dataMap[oBRow]
            # dataMap[oBRow] = tmpBuffer


def rotateClockwise90(L, singleBlock):

    tmpLlength = 2 ** L

    tmpReturnMap = [  [None for _ in range(tmpLlength)] for _ in range(tmpLlength) ]
    #print(f'tmpReturnMap : {tmpReturnMap}')

    for oi1 in range(tmpLlength):
        for oi2 in range(tmpLlength):
            ti1 = tmpLlength - oi1 - 1
            ti2 = oi2
            tmpReturnMap[ti2][ti1] = copy.deepcopy(singleBlock[oi1][oi2])


    return tmpReturnMap

def splitForLsize(N, L):

    tmpLlength = 2**L
    tmpNLength = 2**N

    tmpLeapSize = int(tmpNLength / tmpLlength)
    tmpWholeBlock = []

    for i1 in range(tmpLeapSize):
        for i2 in range(tmpLeapSize):
            tmpBlock = []
            for j1 in range(tmpLlength):
                tmpRowBlock = []
                for j2 in range(tmpLlength):
                    tmpRowBlock.append((i1 + j1, i2 + j2))
                tmpBlock.append( tmpRowBlock )

            tmpWholeBlock.append(tmpBlock)

    return tmpWholeBlock


if __name__ == "__main__":
    import sys
    sys.stdin = open('sample_input.txt', 'r')


    T = 6
    Wrapper(6)