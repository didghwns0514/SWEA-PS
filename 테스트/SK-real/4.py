from collections import deque

distanceMemo = {}
dictionaryGraph2 = {}

def getInitalPoints(n):
    combinationList = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i != j and j != k and i != k):
                    combinationList.append((i, j, k))
    return combinationList


def findDistToEdge(i, j, dictionaryGraph2):
    global distanceMemo

    if (i, j) in distanceMemo:
        return distanceMemo[(i, j)]
    elif (j, i) in distanceMemo:
        return distanceMemo[(j, i)]

    valuefound1 = lookupEdgeBFS(0, i, j, dictionaryGraph2)
    distanceMemo[(i, j)], distanceMemo[(j, i)] = valuefound1, valuefound1

    return distanceMemo[(i, j)]


def lookupEdgeBFS(count, p1, p2, dictionaryGraph2):

    q = deque([(p1, count)])
    visited = []

    while q:

        pNow, countNow = q.popleft()
        if pNow == p2: return countNow

        if pNow not in visited:
            visited.append(pNow)
            for childNode in dictionaryGraph2[pNow]:
                if childNode not in visited:
                    q.append((childNode, countNow + 1))

    return visited


def solution(edges, n):
    global distanceMemo, dictionaryGraph2
    
    for e1, e2 in edges:

        if e1 not in dictionaryGraph2:dictionaryGraph2[e1] = set()
        if e2 not in dictionaryGraph2:dictionaryGraph2[e2] = set()
        dictionaryGraph2[e1].add(e2)
        dictionaryGraph2[e2].add(e1)
        
    valuePoints = getInitalPoints(n)

    counterFound = 0

    for point in valuePoints: 
        i, j, k = point
        dist_ij, dist_jk, dist_ik  = findDistToEdge(i, j, dictionaryGraph2), findDistToEdge(j, k, dictionaryGraph2), findDistToEdge(i, k, dictionaryGraph2)

        if abs(dist_ij + dist_jk) == abs(dist_ik): counterFound += 1

    return counterFound





if __name__=='__main__':
    n = 4
    edges = [[2,3],[0,1],[1,2]]
    returnValue = solution(edges, n)
    print(f'returnValue : {returnValue}')