
dirY = [-1, 0, 1, 0]
dirX = [0, 1, 0, -1]
tempValueCountDict = {}
tmpNumber = 1
tmpMap = []
setCheck = set()

def clockNextDirection(directionGiven, clockwise):
    if clockwise:
        if directionGiven == 3:
            return 0
        else:
            return directionGiven + 1
    else:
        if directionGiven == 0:
            return 3
        else:
            return directionGiven - 1

def genDirections(clockwise):

    if clockwise:
        return [1, 2, 3, 0]
    else:
        return [2, 3, 0, 1]

def solution(n, clockwise):
    global dirY, dirX, tmpMap, setCheck, tempValueCountDict, tmpNumber

    for v in range(n):
        tmpRow = [0] * n
        tmpMap.append(tmpRow)


    setCheck.update([(n-1, 0), (n-1, n-1), (0, n-1), (0 ,0) ])
    listPoint = [(0 ,0), (0, n-1), (n-1, n-1), (n-1, 0)]
    listDirection = genDirections(clockwise)
    initialPoint = [(n-1, 0), (n-1, n-1), (0, n-1), (0 ,0) ]


    while not( len(setCheck) == n**2 ):

        tmpNumber += 1

        for indexK, point in enumerate(listPoint):
            currY = point[0]
            currX = point[1]
            nextY =  currY + dirY[listDirection[indexK]]
            nextX =  currX + dirX[listDirection[indexK]]
            
            # check set existing
            if (nextY, nextX) not in setCheck:
                setCheck.add((nextY, nextX))
                tempValueCountDict[(nextY, nextX)], listPoint[indexK] = tmpNumber, (nextY, nextX)

            else:
                nextDir = clockNextDirection(listDirection[indexK], clockwise)
                listDirection[indexK] = nextDir
                nnextY = currY + dirY[nextDir]
                nnextX = currX + dirX[nextDir]

                # not needed -> already exists and visited
                if (nnextY, nnextX) in setCheck:
                    break
                else:
                    setCheck.add((nnextY, nnextX))
                    listPoint[indexK] = (nnextY, nnextX)
                    tempValueCountDict[(nnextY, nnextX)] = tmpNumber


    for points in initialPoint:
        tmpMap[points[0]][points[1]] = 1

    for key, value in tempValueCountDict.items():
        tmpMap[key[0]][key[1]] = value

    return tmpMap





if __name__=='__main__':
    n = 5
    clockwise = True
    returnValue = solution(n, clockwise)
    print(f'returnValue : {returnValue}')