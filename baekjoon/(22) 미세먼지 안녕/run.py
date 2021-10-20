
from collections import deque
import copy


def wrapper(i):

	for j in range(i):
		R, C, T, dataMap = init()
		solution(j, R, C, T, dataMap)


def init():
	R, C, T = map(int, input().split())
	dataMap = [ list(map(int, input().split())) for _ in range(R)]

	return R, C, T, dataMap

def genCirculation(dataMap, airCleanPos, R, C):

	windDir = [
		[[0,1],[-1,0],[0,-1],[1,0]],
		[[0,1],[1,0],[0,-1],[-1,0]]
	]

	upperPos = airCleanPos[0]
	lowerPos = airCleanPos[1]
	q1, q2 = deque(), deque()

	for _type in range(len(windDir)):
		k = 0
		if _type == 0: # upper
			sY, sX = upperPos
		else:
			sY, sX = lowerPos
		while True:
			if k == 4:
				break
			sY += windDir[_type][k][0]
			sX += windDir[_type][k][1]

			if sY >= R:
				sY -= 1
				k += 1
			elif sY < 0:
				sY += 1
				k += 1
			elif sX >= C:
				sX -= 1
				k += 1
			elif sX < 0:
				sX += 1
				k += 1
			else:

				if _type == 0:
					q1.append((sY, sX, dataMap[sY][sX]))
				else:
					q2.append((sY, sX, dataMap[sY][sX]))

				if (sY, sX) in airCleanPos:
					break

			if sY >= R:
				sY -= 1
				k += 1
			elif sY < 0:
				sY += 1
				k += 1
			elif sX >= C:
				sX -= 1
				k += 1
			elif sX < 0:
				sX += 1
				k += 1


	return q1, q2

def solution(testIter, R, C, T, dataMap):

	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	airCleanPos = [ (idxRow, idxCol) for idxRow, valRow in enumerate(dataMap)
					for idxCol, valCol in enumerate(valRow) if valCol == -1 ]

	for sec in range(T):
		# y, x, 먼지양 -> 공청기 제외
		dustLoc = { (idxRow, idxCol): valCol for idxRow, valRow in enumerate(dataMap)
					 for idxCol, valCol in enumerate(valRow)
					if (idxRow, idxCol) not in airCleanPos
					if dataMap[idxRow][idxCol] > 0}

		# 먼지 분배, 동시에 동작
		dustAlterMapDict = {}
		for keyDust, valDust in dustLoc.items():
			idxRow, idxCol = keyDust

			dustDiffused = 0
			currDust = valDust

			dirInfo = []
			for _dir in range(4):
				nY = idxRow + dy[_dir]
				nX = idxCol + dx[_dir]
				if (0 <= nY < R and 0 <= nX < C) and (nY, nX) not in airCleanPos:
					dirInfo.append((nY,nX))

			dustDiffused = dataMap[idxRow][idxCol] // 5
			if (idxRow, idxCol) not in dustAlterMapDict:
				dustAlterMapDict[(idxRow, idxCol)] = []
			dustAlterMapDict[(idxRow, idxCol)].append(-dustDiffused*len(dirInfo))

			for idxInfo, valInfo in enumerate(dirInfo):
				y, x = valInfo
				if (y, x) not in dustAlterMapDict:
					dustAlterMapDict[(y, x)] = []
				dustAlterMapDict[(y, x)].append(dustDiffused)

		for keyDir, valDir in dustAlterMapDict.items():
			y, x = keyDir
			dataMap[y][x] += (sum(valDir))


		# 공기청정기 동작
		q1, q2 = genCirculation(dataMap, airCleanPos, R, C)
		q1From, q2From = copy.deepcopy(q1), copy.deepcopy(q2)
		q1From.rotate(1)
		q2From.rotate(1)

		for _type in range(2):
			obj = None
			if _type == 0 : objOri, objRotate = q1, q1From
			else :     objOri, objRotate = q2, q2From
			for idxDest, valDest in enumerate(objRotate):
				oriY, oriX, oriDustNum = objOri[idxDest]

				if (valDest[0], valDest[1]) in airCleanPos: # 더 탐색 필요 없음
					dataMap[oriY][oriX] = 0
					continue
				else:
					if ((oriY, oriX) in airCleanPos):
						continue
					else:
						dataMap[oriY][oriX] = valDest[2]



	#print(f'sum : {sum([ sum(data) for data in dataMap ]) + 2}')
	print(sum([ sum(data) for data in dataMap ]) + 2)

if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(8)