

def Wrapper(T):

    for _ in range(T):
        N, dataMap = init()
        returnValue = solution(N, dataMap)
        print(f'returnValue : {returnValue}')


def init():
    N = int(input().strip()) # 격자, 홀수
    dataMap = []
    for _ in range(N):
        tmpLine = list(map(int, input().split(' ')))
        dataMap.append(tmpLine)

    return N, dataMap


def solution(N, dataMap):

    returnValue = getNextPosList(N)
    curPos = (N // 2, N // 2)  # Y, X

    initialSand = 0
    for data in dataMap:
        initialSand += sum(data)

    blown = 0

    for nextPos in returnValue:
        tmpY, tmpX = nextPos[0] - curPos[0], nextPos[1] - curPos[1]

        windBlowData, outWindBlowData  = getBlownPosition(tmpY, tmpX, nextPos[0], nextPos[1], N)
        saveSandInCurpos = dataMap[nextPos[0]][nextPos[1]]
        sandInCurpos = saveSandInCurpos
        dataMap[nextPos[0]][nextPos[1]] = 0


        for positionInfo in outWindBlowData: # [yyPosY, yyPosX-2, 0.05]
            if positionInfo[2] == 'whatsleft':
                pass
            else:
                sandInCurpos -= int(saveSandInCurpos * positionInfo[2])
                blown += int(saveSandInCurpos * positionInfo[2])


        for positionInfo in windBlowData: # [yyPosY, yyPosX-2, 0.05]
            if positionInfo[2] == 'whatsleft':
                pass
            else:
                dataMap[positionInfo[0]][positionInfo[1]] += int(saveSandInCurpos * positionInfo[2])
                sandInCurpos -= int(saveSandInCurpos * positionInfo[2])


        # a 더하기
        if windBlowData[-1][2] == 'whatsleft':
            dataMap[windBlowData[-1][0]][windBlowData[-1][1]] += sandInCurpos
        elif outWindBlowData[-1][2] == 'whatsleft':
            blown += sandInCurpos
        else:
            raise ValueError('Wrong-2!')


        # update curpos
        curPos = nextPos


    # nowSand = 0
    # for data in dataMap:
    #     nowSand += sum(data)


    return blown

def getBlownPosition(tmpY, tmpX, yyPosY, yyPosX, N):
    # calc for relative YY position
    posData = []

    if tmpX == -1:
        posData.append( [yyPosY, yyPosX-2, 0.05] )
        posData.append( [yyPosY-1, yyPosX-1, 0.1] )
        posData.append( [yyPosY+1, yyPosX-1, 0.1] )
        posData.append( [yyPosY-1, yyPosX, 0.07] )
        posData.append( [yyPosY+1, yyPosX, 0.07] )
        posData.append( [yyPosY-2, yyPosX, 0.02] )
        posData.append( [yyPosY+2, yyPosX, 0.02] )
        posData.append( [yyPosY-1, yyPosX+1, 0.01] )
        posData.append( [yyPosY+1, yyPosX+1, 0.01] )
        posData.append([yyPosY, yyPosX - 1, 'whatsleft'])
    elif tmpX == 1:
        posData.append( [yyPosY, yyPosX+2, 0.05] )
        posData.append( [yyPosY-1, yyPosX+1, 0.1] )
        posData.append( [yyPosY+1, yyPosX+1, 0.1] )
        posData.append( [yyPosY-1, yyPosX, 0.07] )
        posData.append( [yyPosY+1, yyPosX, 0.07] )
        posData.append( [yyPosY-2, yyPosX, 0.02] )
        posData.append( [yyPosY+2, yyPosX, 0.02] )
        posData.append( [yyPosY-1, yyPosX-1, 0.01] )
        posData.append( [yyPosY+1, yyPosX-1, 0.01] )
        posData.append([yyPosY, yyPosX + 1, 'whatsleft'])
    elif tmpY == -1:
        posData.append( [yyPosY-2, yyPosX, 0.05] )
        posData.append( [yyPosY-1, yyPosX+1, 0.1] )
        posData.append( [yyPosY-1, yyPosX-1, 0.1] )
        posData.append( [yyPosY, yyPosX-1, 0.07] )
        posData.append( [yyPosY, yyPosX+1, 0.07] )
        posData.append( [yyPosY, yyPosX-2, 0.02] )
        posData.append( [yyPosY, yyPosX+2, 0.02] )
        posData.append( [yyPosY+1, yyPosX-1, 0.01] )
        posData.append( [yyPosY+1, yyPosX+1, 0.01] )
        posData.append([yyPosY-1, yyPosX, 'whatsleft'])
    elif tmpY == 1:
        posData.append( [yyPosY+2, yyPosX, 0.05] )
        posData.append( [yyPosY+1, yyPosX+1, 0.1] )
        posData.append( [yyPosY+1, yyPosX-1, 0.1] )
        posData.append( [yyPosY, yyPosX-1, 0.07] )
        posData.append( [yyPosY, yyPosX+1, 0.07] )
        posData.append( [yyPosY, yyPosX-2, 0.02] )
        posData.append( [yyPosY, yyPosX+2, 0.02] )
        posData.append( [yyPosY-1, yyPosX-1, 0.01] )
        posData.append( [yyPosY-1, yyPosX+1, 0.01] )
        posData.append([yyPosY+1, yyPosX, 'whatsleft'])
    else:
        raise ValueError('Wrong-1!')

    # filter out of box

    return [ data for data in posData if (0 <= data[0] <= N-1  and 0 <= data[1] <= N-1) ], [ data for data in posData if not (0 <= data[0] <= N-1  and 0 <= data[1] <= N-1) ]

def getNextPosList(N):
    # if N = 7 -> startpos :
    curPos = (N//2, N//2) # Y, X
    startPos = curPos
    direction = 0 # 0 : 왼, 1 : 아래, 2 : 오른, 3 : 위
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    movePos = []
    movePos.append(curPos)
    realPos = []

    while curPos != (0, 0):

        nY, nX = curPos[0] + dy[direction], curPos[1] + dx[direction]
        movePos.append((nY, nX))
        # realPos.append((nY, nX, direction))

        saveDirection = direction
        direction = (direction + 1) % 4

        nnY, nnX = nY + dy[direction],  nX + dx[direction]
        if (nnY, nnX) not in movePos:
            pass

        else:
            direction = saveDirection

        curPos = (nY, nX)

    return movePos[1:]


if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 6
    Wrapper(T)