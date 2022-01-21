from collections import deque

def wrapper(T):

    for _ in range(T):
        N, Fule, dataMap, StartPos, dataCustomer = init()
        returnValue = solution(N, Fule, dataMap, StartPos, dataCustomer)
        print(f'returnValue : {returnValue}')


def init():
    # init
    N, M, Fule = list(map(int, input().split(' ')))

    # Map
    dataMap = []
    for _ in range(N):
        tmplist = list(map(int, input().split(' ')))
        dataMap.append(tmplist)

    # startpos
    x, y = list(map(int, input().split(' ')))
    StartPos = (x-1, y-1)

    # customer
    dataCustomer = {}
    for _ in range(M):
        v1, v2, v3, v4 = list(map(int, input().split(' ')))
        dataCustomer[(v1-1, v2-1)] = (v3-1, v4-1)

    return N, Fule, dataMap, StartPos, dataCustomer


def solution(N, Fule, dataMap, StartPos, dataCustomer):


    while dataCustomer: # 연료 바닥시 fail
        returnVal = bfs(StartPos, dataMap, findList=set(dataCustomer.keys()))
        tmpFiltered = [data for data in returnVal if (data[0], data[1]) in dataCustomer]
        if not tmpFiltered:
            return -1
        selectedCustomerPos = min(tmpFiltered,
                                  key=lambda y: (y[2], y[0], y[1]))

        tmpFuleConsume = 0

        Fule -= selectedCustomerPos[2]
        #tmpFuleConsume += selectedCustomerPos[2]
        if Fule < 0:
            return -1

        StartPos = (selectedCustomerPos[0], selectedCustomerPos[1])
        destPos = dataCustomer[StartPos]
        dataCustomer.pop(StartPos)

        returnVal2 = bfs(StartPos, dataMap, findPos=destPos)
        tmpFiltered2 = [data for data in returnVal2 if (data[0], data[1]) in set(dataCustomer.values())]
        if not tmpFiltered2:
            return -1

        selectedCustomerDestPos = min([data for data in returnVal2 if (data[0], data[1]) == destPos],
                              key=lambda y: (y[2], y[0], y[1]))

        Fule -= selectedCustomerDestPos[2]
        tmpFuleConsume += selectedCustomerDestPos[2]
        if Fule < 0:
            return -1

        StartPos = (selectedCustomerDestPos[0], selectedCustomerDestPos[1])
        Fule += (tmpFuleConsume * 2)

        pass

    return Fule


def bfs(startpos, dataMap, findPos=None, findList=None):

    visited = []
    history = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    MaxX = len(dataMap)
    MaxY = len(dataMap[0])
    q = deque()
    isQuitRequest = False

    cx, cy = startpos
    q.append((cx, cy, 0))

    while q:

        tmpPos = q.popleft()  # bfs
        cx, cy, c_counter = tmpPos
        if findPos != None:
            if (cx, cy) == findPos:
                return [(cx, cy, c_counter)]

        if not (cx, cy) in visited:
            visited.append((cx, cy))
            if not (cx, cy) == startpos:
                history.append((cx, cy, c_counter))

            for i in range(4):

                nx, ny = cx + dx[i], cy + dy[i]

                if not( (0 <= nx < MaxX) and (0 <= ny < MaxY) ): continue # out of boundary
                if dataMap[nx][ny] == 1: continue # wall
                q.append((nx, ny, c_counter+1))

        if findList != None:
            if any( [ (data[0], data[1] ) in findList for data in history] ):
                isQuitRequest = True
                continue

        if isQuitRequest:
            return history

    return history


if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 3
    wrapper(T)