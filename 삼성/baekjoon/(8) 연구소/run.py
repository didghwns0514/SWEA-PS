import itertools
import sys
import copy

virusZoneCnt = 99999999

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		N, M, dataMap = init()
		solution(j, N, M, dataMap)


def init():

	N, M = list(map(int, input().split(' ')))
	dataMap = [ list(map(int, input().split(' '))) for _ in range(N)]

	yprint(f'N, M : {N, M}')
	yprint(f'dataMap : {dataMap}')

	return N, M, dataMap

def dfs(dataMap, visited, idxY, idxX):
	global virusZoneCnt


	# tmpVZCnt = getVirusZoneNumber(dataMap)
	# if tmpVZCnt > virusZoneCnt:
	# 	return False

	#yprint(f'visited : {visited}')
	if (idxY, idxX) in visited:
		return False

	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	maxY = len(dataMap)
	maxX = len(dataMap[0])

	if dataMap[idxY][idxX] == 1:
		return False

	visited.add((idxY, idxX))
	yprint(f'idxY, idxX : {idxY, idxX }')
	dataMap[idxY][idxX] = 2

	for i in range(4):
		nextY = idxY + dy[i]
		nextX = idxX + dx[i]
		if 0 <= nextY <= maxY - 1 and 0 <= nextX <= maxX - 1:
			dfs(dataMap, visited, nextY, nextX)

	return True

def dfsWrapper(dataMap, selection):


	# add 3 walls
	yprint(f'selection :{selection}')
	yprint(f'dataMap original : {dataMap}')
	for pos in selection:
		if dataMap[pos[0]][pos[1]] in [1, 2]:
			return False
		dataMap[pos[0]][pos[1]] = 1

	yprint(f'dataMap before : {dataMap}')

	interestPoint =  []
	visited = set()
	for idxY, valueY in enumerate(dataMap):
		for idxX, valueX in enumerate(valueY):
			if valueX == 2:
				interestPoint.append((idxY, idxX))
	for pos in interestPoint:
		dfs(dataMap, visited, pos[0], pos[1])

	yprint(f'dataMap after : {dataMap}')
	return True

def getSafeZoneNumber(dataMap):

	cnt = 0
	for idxY, valY in enumerate(dataMap):
		for idxX, valX in enumerate(valY):
			if  valX == 0:
				cnt += 1

	return cnt

def getVirusZoneNumber(dataMap):

	cnt = 0
	for idxY, valY in enumerate(dataMap):
		for idxX, valX in enumerate(valY):
			if  valX == 2:
				cnt += 1

	return cnt

def solution(testIter, N, M, _dataMap): # N :col, M:row
	global virusZoneCnt

	# make datapoint
	dataPoint = []
	for col in range(N):
		for row in range(M):
			dataPoint.append((col, row))
	yprint(f'dataPoint ; {dataPoint}')
	# Select 3
	selectedIter = list(itertools.combinations(dataPoint, 3))
	# selectForce = []
	# for i1, val1 in enumerate(dataPoint):
	# 	for i2, val2 in enumerate(dataPoint[i1+1:]):
	# 		if dataPoint[i1+i2+1:]:
	# 			for i3, val3 in enumerate(dataPoint[i1+i2+1:]):
	# 				selectForce.append((val1, val2, val3))
	# yprint(f'selectedIter : {selectedIter}')
	# yprint(f'selectForce : {selectForce}')

	#yprint(f'len - selectForce : {len(selectForce)}')
	yprint(f'len - selectedIter : {len(selectedIter)}')
	yprint(f'selectedIter  : {selectedIter[:10]}')

	resultList = []
	for selection in selectedIter:
		yprint('\n')
		yprint(f'-'*20)

		dataMap = copy.deepcopy(_dataMap)
		tmpBoolean = dfsWrapper(dataMap, selection)
		if tmpBoolean:
			resultCnt = getSafeZoneNumber(dataMap)
			#virusZoneCnt = getVirusZoneNumber(dataMap)
			yprint(f'resultCnt : {resultCnt}')
			resultList.append(resultCnt)

	resultMax = max(resultList)
	yprint(f'resultMax : {resultMax}')
	print(resultMax)



if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(3)