

def solution(rc, operations):
    rs = len(rc)
    cs = len(rc[0])

    for op in operations:
        if op == "Rotate":
            rotate(rc, rs, cs)
        elif op == "ShiftRow":
            shiftRow(rc)

    return rc

def shiftRow(dataMap):
    poped = dataMap.pop(-1)
    dataMap.insert(0,poped)

def rotate(dataMap, rowSize, colSize):

    currPos = (0, 0)
    endBuffer = dataMap[1][0]
    tempBuffer = None
    currBuffer = None

    for j in range(  ((rowSize + colSize) * 2) - 4 ):
        currBuffer = dataMap[currPos[0]][currPos[1]]
        if tempBuffer != None:
            dataMap[currPos[0]][currPos[1]] = tempBuffer
        currPos = getNextPos(currPos, rowSize, colSize)
        tempBuffer = currBuffer

    dataMap[0][0] = endBuffer

def getNextPos(currPos, rowSize, colSize):
    if currPos[0] == 0 and currPos[1] < colSize - 1:
        return (currPos[0], currPos[1] + 1)
    elif currPos[0] == 0 and currPos[1] == colSize - 1:
        return (currPos[0] + 1, currPos[1])

    elif currPos[0] < rowSize - 1 and currPos[1] == colSize - 1:
        return (currPos[0] + 1, currPos[1])
    elif currPos[0] == rowSize - 1 and currPos[1] == colSize - 1:
        return (currPos[0], currPos[1]-1)

    elif currPos[0] == rowSize - 1 and 0 < currPos[1]:
        return (currPos[0], currPos[1]-1)
    elif currPos[0] == rowSize - 1 and 0 == currPos[1]:
        return (currPos[0] - 1, currPos[1])

    elif currPos[0] > 0 and currPos[1] == 0:
        return (currPos[0] - 1, currPos[1])


if __name__ == "__main__":

    switch = 1

    if switch == 1:
        rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        operations = ["Rotate", "ShiftRow"]
        #shiftRow(rc)
        answer = solution(rc, operations)
        print(f'found answer : {answer}')
        assert(answer == [[8, 9, 6], [4, 1, 2], [7, 5, 3]])

    elif switch == 2:
        rc = [[8, 6, 3], [3, 3, 7], [8, 4, 9]]
        operations = ["Rotate", "ShiftRow", "ShiftRow"]
        answer = solution(rc, operations)
        print(f'found answer : {answer}')
        assert(answer == [[8, 3, 3], [4, 9, 7], [3, 8, 6]])

    elif switch == 3:
        rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
        #rotate(rc, len(rc), len(rc[0]))
        answer = solution(rc, operations)
        print(f'found answer : {answer}')
        assert(answer == [[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]])
