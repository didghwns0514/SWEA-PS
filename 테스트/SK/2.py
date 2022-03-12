def solution(n, clockwise):
    tmpMap = []

    globalVisitedSet = set()

    for k1 in range(n):
        tmpRow = [0]*n
        tmpMap.append(tmpRow)

    globalVisitedSet.update([(n-1, 0), (n-1, n-1), (0, n-1), (0 ,0) ])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # four points
    p1, p2, p3, p4 = (0 ,0), (0, n-1), (n-1, n-1), (n-1, 0)
    listPoint = [p1, p2, p3, p4]
    # 위, + 시계방향 : 0, 1, 2, 3
    if clockwise:
        d1, d2, d3, d4 = 1, 2, 3, 0
    else:
        d1, d2, d3, d4 = 2, 3, 0, 1
    listDirection = [d1, d2, d3, d4]

    tmpHist = {}
    tmpNumber = 1

    while not( len(globalVisitedSet) == n**2 ):
        tmpNumber += 1

        for idx, point in enumerate(listPoint):
            cy, cx = point
            ny, nx = cy + dy[listDirection[idx]], cx + dx[listDirection[idx]]
            if (ny, nx) not in globalVisitedSet:
                globalVisitedSet.add((ny, nx))
                listPoint[idx] = (ny, nx)
                tmpHist[(ny, nx)] = tmpNumber
            else: # 방문
                nextDir = getClockwise(listDirection[idx], clockwise)
                listDirection[idx] = nextDir
                nny, nnx = cy + dy[nextDir], cx + dx[nextDir]
                if (nny, nnx) in globalVisitedSet:
                    break
                else:
                    globalVisitedSet.add((nny, nnx))
                    listPoint[idx] = (nny, nnx)
                    tmpHist[(nny, nnx)] = tmpNumber


    for tmpPoint in [(n-1, 0), (n-1, n-1), (0, n-1), (0 ,0) ]:
        tmpMap[tmpPoint[0]][tmpPoint[1]] = 1

    for key, value in tmpHist.items():
        tmpMap[key[0]][key[1]] = value

    return tmpMap

def getClockwise(currentDir, clockwise):
    if clockwise:
        if currentDir == 3:
            return 0
        else:
            return currentDir + 1
    else:
        if currentDir == 0:
            return 3
        else:
            return currentDir - 1



if __name__=='__main__':
    n = 5
    clockwise = True
    returnValue = solution(n, clockwise)
    print(f'returnValue : {returnValue}')