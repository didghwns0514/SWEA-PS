
import copy

def wrapper(i):
    for _ in range(i):
        dataMap, sentMap, dirMap, K, M, N = init()
        returnValue = solution(dataMap, sentMap, dirMap, K, M, N)
        print(f'returnValue : {returnValue}')

def init():
    N, M, K = list(map(int, input().split(' ')))

    dataMap = []
    sentMap = {}
    dirMap = {}

    # 맵 N개의 줄
    for j in range(N):
        tmpInput = []
        tmpList = list(map(int, input().split(' ')))
        for k in range(len(tmpList)):
            if tmpList[k] == 0:
                tmpInput.append([])
            else:
                tmpInput.append([[tmpList[k], None]])
                sentMap[(j, k)] = [tmpList[k], K] # shark
        dataMap.append(tmpInput)

    # 각 상어 방향 기록
    tmpDir = list(map(int, input().split(' ')))
    for m in range(1, M+1):
        for idx1, val1 in enumerate(dataMap):
            for idx2, val2 in enumerate(val1):
                if val2:
                    if val2[0][0] == m:
                        dataMap[idx1][idx2][0][1] = tmpDir[m-1]

    # 1, 2, 3, 4, -> 위, 아래, 왼쪽, 오른쪽
    for q in range(M):
        dirMap[q+1] = {} # 상어 num
        for p in range(4):
            dirMap[q+1][p+1] = list(map(int, input().split(' ')))

    return dataMap, sentMap, dirMap, K, M, N

def solution(dataMap, sentMap, dirMap, K, M, N):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for time in range(1000):



        # 상어 이동
        for sharkNum in range(1, M+1):
            sharkResult = findShark(sharkNum, dataMap)
            if sharkResult == None: continue

            X, Y = sharkResult[0], sharkResult[1]
            sharkDir = dataMap[sharkResult[0]][sharkResult[1]][sharkResult[2]][1]
            dirshark = dirMap[sharkNum][sharkDir]


            emptySpot = []
            for direction in dirshark:
                nX, nY = X + dx[direction - 1], Y + dy[direction - 1]
                if not((0 <= nX <= N-1) and (0 <= nY <= N-1)):
                    continue
                else:
                    #if not dataMap[nX][nY]: # 빈자리일 경우
                    if (nX, nY) not in sentMap:
                        emptySpot.append((nX, nY, direction))
            if emptySpot:
                # 1, 2, 3, 4, -> 위, 아래, 왼쪽, 오른쪽
                # 빈자리 있을시
                for spot in emptySpot:
                    dataMap[sharkResult[0]][sharkResult[1]][sharkResult[2]][1] = spot[2]  # direction update
                    dataMap[spot[0]][spot[1]].append(
                        dataMap[sharkResult[0]][sharkResult[1]].pop(sharkResult[2])
                    )
                    break

            else:
                # 빈자리 없을 시
                # 1, 2, 3, 4, -> 위, 아래, 왼쪽, 오른쪽
                for direction in dirshark:
                    nX, nY = X + dx[direction-1], Y + dy[direction-1]
                    if not((0 <= nX <= N-1) and (0 <= nY <= N-1)):
                        continue
                    if (nX, nY) in sentMap:
                        if sentMap[(nX, nY)][0] == sharkNum: # 자기 냄새
                            dataMap[sharkResult[0]][sharkResult[1]][sharkResult[2]][1] = direction # direction update
                            dataMap[nX][nY].append(
                                dataMap[sharkResult[0]][sharkResult[1]].pop(sharkResult[2])
                            )
                            break
                        elif sentMap[(nX, nY)][0] != sharkNum: # 자기 냄새
                            continue
                    else:
                        dataMap[sharkResult[0]][sharkResult[1]][sharkResult[2]][1] = direction  # direction update
                        dataMap[nX][nY].append(
                            dataMap[sharkResult[0]][sharkResult[1]].pop(sharkResult[2])
                        )
                        break

        # 상어 쫒아내기
        for idx1, val1 in enumerate(dataMap):
            for idx2, val2 in enumerate(val1):
                if val2: # 상어 있음
                    if len(val2) >= 2:
                        selectValue = min(val2, key=lambda x : x[0])
                        dataMap[idx1][idx2] = copy.deepcopy([selectValue])

        # 냄새 차감
        # 주인, 냄새 cnt
        removeKeys = []
        for key, val in sentMap.items():
            sentMap[key][1] -= 1
            if sentMap[key][1] == 0:
                removeKeys.append(key)
        for _Key in removeKeys: # 제거
            sentMap.pop(_Key)

        # 현재 위치 냄새 업데이트
        for idx1, val1 in enumerate(dataMap):
            for idx2, val2 in enumerate(val1):
                if val2: # 상어 있음
                    sentMap[(idx1, idx2)] = [val2[0][0], K]

        # 상어 중복되는거 확인
        totalCount = 0
        location = None
        for idx1, val1 in enumerate(dataMap):
            for idx2, val2 in enumerate(val1):
                if val2: # 상어 있음
                    totalCount += 1
                    location = (idx1, idx2)
        if totalCount == 1:
            return time + 1

    return -1


def findShark(sharkNum, dataMap):

    for idx1, val1 in enumerate(dataMap):
        for idx2, val2 in enumerate(val1):
            if val2:
                for idx3, subShark in enumerate(val2):
                    if subShark:
                        if subShark[0] == sharkNum:
                            return (idx1, idx2, idx3)

    return None

if __name__ == '__main__':

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 4
    wrapper(4)