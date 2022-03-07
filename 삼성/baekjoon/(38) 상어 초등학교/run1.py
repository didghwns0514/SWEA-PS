
import copy
from collections import deque

def Wrapper(T):

    for _ in range(T):
        N, dataMap, Q, dataL = init()
        returnResult, _maxHist = solution(N, dataMap, Q, dataL)
        #print(f'returnResult, _maxHist : {returnResult, _maxHist}')
        print(returnResult)
        print(_maxHist)


def init():
    N, Q = list(map(int, input().split(' ')))  # N**2 만큼 / Q 번 수행

    # 데이터 생성
    dataMap = []
    for _ in range(2**N):
        tmpInput = list(map(int, input().split(' ')))
        dataMap.append(tmpInput)

    dataL = list(map(int, input().split(' ')))

    # print(f'len(dataMap) : {len(dataMap)}')
    # print(f'dataMap : {dataMap}')
    # print(f'Q, dataL : { Q, dataL}')

    return N, dataMap, Q, dataL


def solution(N, dataMap, Q, dataL):

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    nMax = 2**N

    for L in dataL: # 총 Q 번 시행
        tmpDataMap = copy.deepcopy(dataMap)
        tmpWholeBlock = splitForLsize(N, L)
        # print(f'\n')
        # print(f'-'*20)
        # print(f'L :{L}')
        # print(f'tmpWholeBlock : {tmpWholeBlock}')
        # print(f'dataMap before : {dataMap}')

        # rotate blocks
        for singleBlock in tmpWholeBlock:
            # print(f'singleBlock : {singleBlock}')
            rotatedBlock = rotateClockwise90(L, singleBlock)
            # print(f'rotatedBlock : {rotatedBlock}')

            for idxRow, valRow in enumerate(singleBlock):
                for idxCol, valCol in enumerate(valRow):
                    # tmpBuff = dataMap[ singleBlock[idxRow][idxCol][0] ][ singleBlock[idxRow][idxCol][1] ]
                    # dataMap[singleBlock[idxRow][idxCol][0]][singleBlock[idxRow][idxCol][1]] = copy.deepcopy(dataMap[ rotatedBlock[idxRow][idxCol][0] ][ rotatedBlock[idxRow][idxCol][1] ])
                    # dataMap[rotatedBlock[idxRow][idxCol][0]][rotatedBlock[idxRow][idxCol][1]] = tmpBuff
                    dataMap[ singleBlock[idxRow][idxCol][0] ][ singleBlock[idxRow][idxCol][1] ] = tmpDataMap[ rotatedBlock[idxRow][idxCol][0] ][ rotatedBlock[idxRow][idxCol][1] ]

        # ice melt
        tmpMeltHist = []
        for oi1, v1 in enumerate(dataMap):
            for oi2, v2 in enumerate(v1):
                tmpCount = 0
                if dataMap[oi1][oi2] == 0 : continue

                for _i in range(4):
                    nX, nY = dx[_i] + oi2, dy[_i] + oi1
                    if ( 0 <= nX < nMax  and 0 <= nY < nMax):
                        if dataMap[nY][nX] > 0 :
                            tmpCount += 1

                if tmpCount < 3 :
                    tmpMeltHist.append( (oi1, oi2) )

        for meltPos in tmpMeltHist:
            dataMap[meltPos[0]][meltPos[1]] -= 1


        # print(f'dataMap after : {dataMap}')
            # tmpBuffer = dataMap[tBRow]
            # dataMap[tBRow] = dataMap[oBRow]
            # dataMap[oBRow] = tmpBuffer

    # 합 구하기
    _sum = 0
    for row in dataMap:
        _sum += sum(row)


    _maxHist = calculateIce(dataMap)

    return _sum, _maxHist


countIce = 0
visited = set()
def calculateIce(dataMap):

    global countIce, visited
    visited = set()
    countIce = 0
    maxHist = 0
    nMax = len(dataMap)

    for oi1, val1 in enumerate(dataMap):
        for oi2, val2 in enumerate(val1):
            countIce = 0

            bfs((oi1, oi2), dataMap, nMax)
            maxHist = max(maxHist, countIce)

    return maxHist

def bfs(start, dataMap, nMax):
    global countIce, visited

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    q = deque()
    q.append(start)

    if start in visited:
        return None

    while q:
        tmpPop = q.popleft()

        if tmpPop in visited:
            continue

        if dataMap[tmpPop[0]][tmpPop[1]] == 0:
            continue

        visited.add(tmpPop)
        countIce += 1

        for _i in range(4):
            nX, nY = dx[_i] + tmpPop[1], dy[_i] + tmpPop[0]
            if (0 <= nX < nMax and 0 <= nY < nMax):
                q.append((nY, nX))


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
                    tmpRowBlock.append((i1*tmpLlength + j1, i2*tmpLlength + j2))
                tmpBlock.append( tmpRowBlock )

            tmpWholeBlock.append(tmpBlock)

    return tmpWholeBlock


if __name__ == "__main__":
    import sys
    sys.stdin = open('sample_input.txt', 'r')


    T = 6
    Wrapper(T)