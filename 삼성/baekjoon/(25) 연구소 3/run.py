
def tWrapper():

	def test1():
		startpoint = [ (4,3), (4,2) ]
		dataMap = [ [2, 2, 2, 1, 1],
					[2, 1, 1, 1, 1],
					[2, 1, 1, 1, 1],
					[2, 1, 1, 1, 1],
					[2, 2, 2, 2, 0],
					]
		tmpResult = dfs(dataMap, startpoint)
		print(f'tmpResult : {tmpResult}')

	test1()

def wrapper(i):

	for j in range(i):
		N, M, dataMap = init()
		result = solution(j, N, M, dataMap)
		print(f'#{j+1} {result}')

def init():
	N, M = map(int, input().split())
	dataMap = [ list( map(int, input().split())) for _ in range(N) ]

	return N, M, dataMap

def checkFinished(dataMap):

	for idxRow, valRow in enumerate(dataMap):
		for idxCol, valCol in enumerate(valRow):
			if valCol == 0 :
				return False

	return True



def dfs(dataMap, startPoints:list):

	MaxX = len(dataMap[0])
	MaxY = len(dataMap)
	timeCount = 0
	dy = [1, 0, -1,  0]
	dx = [0, 1,  0, -1]
	visited = []

	q = deque()
	q.extend(list(startPoints))
	tmpQ = deque()

	while q or tmpQ:

		currPos = q.popleft()
		if currPos not in visited:
			visited.append(currPos)
			dataMap[currPos[0]][currPos[1]] = '*'

			for k in range(4):
				nY = currPos[0] + dy[k]
				nX = currPos[1] + dx[k]
				if 0 <= nY <= MaxY -1 and 0 <= nX <= MaxX - 1  \
					and (nY, nX) not in visited and (nY, nX) not in tmpQ:
					if dataMap[nY][nX] == 0:
						tmpQ.append((nY, nX))
					elif dataMap[nY][nX] == 2:
						tmpQ.append((nY, nX))
						# tmpNumProcess += 1
					# elif dataMap[nY][nX] == 2:
					# 	tmpResult = activateVirus(dataMap, [], (nY, nX))
					# 	q.extend(tmpResult)
					# 	tmpNumProcess += len(tmpResult)

		if checkFinished(dataMap):
			return True, timeCount

		if not q:
			q = copy.deepcopy(tmpQ)
			tmpQ.clear()
			tmpNumProcess = len(q)
			timeCount += 1




	# if checkFinished(dataMap):
	# 	return True, timeCount
	# else:
	# 	return False, -1
	return False, -1

def solution(testIter,  N, M, dataMap):

	filteredMSpots = [ (idxRow, idxCol) for idxRow, valRow in enumerate(dataMap)
					   for idxCol, valCol in enumerate(valRow)
					   if valCol == 2 ]
	selected = list( itertools.combinations(filteredMSpots, M) )

	minSec = -1
	for select in selected:
		tmpDataMap = [ x[:] for x in dataMap ]
		resultBool, resultTime = dfs(tmpDataMap, select)
		if resultBool:
			if minSec >= 0:
				minSec = min(minSec, resultTime)
			else:
				minSec = resultTime

	return minSec

if __name__=="__main__":
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	import itertools
	from collections import deque
	import copy

	#tWrapper()

	#T = int(input())
	T = 6
	wrapper(T)
