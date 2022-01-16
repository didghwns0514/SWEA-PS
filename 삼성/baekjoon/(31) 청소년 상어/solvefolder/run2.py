import copy

def wrapper(i):

    for _ in range(i):
        data = init()
        returnValue = solution(data)
        print(f'returnValue : {returnValue}')

def init():
    data = []
    for _ in range(4):
        line = list(map(int, input().split(' ')))
        tmpList = []
        for i in range(4):
            tmpList.append( [ line[2*i], line[2*i+1], 1 ] )
        data.append(tmpList)

    return data

fishAnswer = 0
def solution(data):
    global fishAnswer
    fishAnswer = 0
    subSolution(data[0][0][0], data, [0,0,0], 0)

    return fishAnswer


def subSolution(nextSharkFish, data, shark, fishSum=0):
    global fishAnswer
    dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 행
    dy = [0, -1, -1, -1, 0, 1, 1, 1] # 열

    # 상어 이동
    try:
        sharkLoc = findShark(data)
        data[sharkLoc[0]][sharkLoc[1]] = None
    except:pass

    fishLoc = findFish(nextSharkFish, data)
    fishDir = data[fishLoc[0]][fishLoc[1]][1]
    fishSum += nextSharkFish

    data[fishLoc[0]][fishLoc[1]] = copy.deepcopy(shark)
    data[fishLoc[0]][fishLoc[1]][1] = fishDir

    # 물고기 이동
    for num in range(1, 16+1):
        currFishLoc = findFish(num, data)
        if currFishLoc == None:
            continue

        currFishDir = data[currFishLoc[0]][currFishLoc[1]][1]
        for _ in range(8):
            nextX = currFishLoc[0] + dx[currFishDir-1]
            nextY = currFishLoc[1] + dy[currFishDir-1]
            if not( (0 <= nextX <= 3) and (0 <= nextY <= 3) ):
                currFishDir = getNextDir(currFishDir)
                data[currFishLoc[0]][currFishLoc[1]][1] = currFishDir
                continue


            if data[nextX][nextY] == None:
                data[nextX][nextY] = copy.deepcopy(
                    data[currFishLoc[0]][currFishLoc[1]]
                )
                data[currFishLoc[0]][currFishLoc[1]] = None
                break
            else:
                if data[nextX][nextY][2] == 0:  # shark
                    currFishDir = getNextDir(currFishDir)
                    data[currFishLoc[0]][currFishLoc[1]][1] = currFishDir
                    continue
                else:
                    tmpVal = copy.deepcopy(data[currFishLoc[0]][currFishLoc[1]])
                    data[currFishLoc[0]][currFishLoc[1]] = copy.deepcopy(data[nextX][nextY])
                    data[nextX][nextY] = copy.deepcopy(tmpVal)
                    break


    # Shark move
    sharkLoc = findShark(data)
    sharkLX, sharkLY = sharkLoc
    sharkDir = data[sharkLX][sharkLY][1]
    tmpFish = []
    for _ in range(4):
        nextX, nextY = sharkLX + dx[sharkDir-1], sharkLY + dy[sharkDir-1]
        sharkLX, sharkLY = nextX, nextY
        if not( (0 <= nextX <= 3) and (0 <= nextY <= 3)): continue
        if data[nextX][nextY] == None: continue
        tmpFish.append(data[nextX][nextY][0])

    if not tmpFish:
        fishAnswer = max(fishAnswer, fishSum)
        return
    else:
        for k in range(len(tmpFish)):
            tmpData = copy.deepcopy(data)
            subSolution(tmpFish[k], tmpData, tmpData[sharkLoc[0]][sharkLoc[1]], fishSum=fishSum)

def getNextDir(dirss):
    if dirss == 8:
        return 1
    else:
        return dirss + 1

def findShark(data):
    for idx1, val1 in enumerate(data):
        for idx2, val2 in enumerate(val1):
            if val2 != None:
                if val2[2] == 0: # shark
                    return (idx1, idx2)
    else:
        raise ValueError("not found shark")

def findFish(fishVal, data):

    for idx1, val1 in enumerate(data):
        for idx2, val2 in enumerate(val1):
            if val2 != None:
                if val2[0] == fishVal and val2[2] != 0: # not shark
                    return (idx1, idx2)
    else:
        return None


if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 4
    wrapper(T)