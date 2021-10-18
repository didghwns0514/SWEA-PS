# 5
import math
import pprint

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)


def wrapper(i):

	for j in range(i):
		yprint('\n'*2)
		yprint('#'*30)
		N, L, R, dataMap = init()
		solution(j, N, L, R, dataMap)

def findParent(dataCountry, country):
	# if dataCountry[country] == country:
	# 	return country
	# else:
	# 	return findParent(dataCountry, dataCountry[country])
	targetCountry = dataCountry[country]
	while( True ):
		if targetCountry == country:
			return targetCountry
		else:
			country = targetCountry
			targetCountry = dataCountry[country]


def unionFind(dataCountry, country1, country2):
	parent1 = findParent(dataCountry, country1)
	parent2 = findParent(dataCountry, country2)

	# if counter1 >= counter2:
	# 	dataCountry[parent2] = parent1
	# else:
	# 	dataCountry[parent1] = parent2
	if parent1 != parent2: # avoid cycle
		dataCountry[parent1] = parent2

def init():
	N, L, R = map(int, input().split())
	dataMap = [ list(map(int, input().split())) for _ in range(N) ]

	yprint(f'N, L, R  : {N, L, R }')
	yprint(f'dataMap  : {dataMap}')

	return N, L, R, dataMap

def solution(testIter, N, L, R, dataMap):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	yMax, xMax = N-1, N-1
	count = 0
	while True:
		yprint('')
		yprint('-'*20)
		dataCountry = {(rowIdx, colIdx):(rowIdx, colIdx) for rowIdx, rowVal in enumerate(dataMap) \
					   for colIdx, colVal in enumerate(rowVal)}
		yprint(f'  - count : {count}')
		yprint(f'dataCountry init : {dataCountry}')

		for rowIdx, rowVal in enumerate(dataMap):
			for colIdx, colVal in enumerate(rowVal):
				for direction in range(4):
					nextY = rowIdx + dy[direction]
					nextX = colIdx + dx[direction]
					if 0 <= nextY <= yMax and 0 <= nextX <= xMax:
						targetCountryVal = dataMap[nextY][nextX]
						if L <= abs(targetCountryVal - colVal) <= R:
							unionFind(dataCountry, country1=(rowIdx, colIdx), country2=(nextY,nextX))
							# parentBaseNode = unionFind(dataCountry, (rowIdx, colIdx))
							# parentTargetNode = unionFind(dataCountry, (nextY, nextX))
							# if parentTargetNode != parentBaseNode:
							# 	dataCountry[(nextY, nextX)] = parentBaseNode
							#dataCountry[(nextY, nextX)] = unionFind(dataCountry, (rowIdx, colIdx))

		yprint(f'dataCountry after : {dataCountry}')

		unitedSet = set([ findParent(dataCountry, key) for key, value in dataCountry.items() ])
		yprint(f'unitedSet : {unitedSet}')
		yprint('********')
		for union in unitedSet:
			tmp = []
			for key, val in dataCountry.items():
				if findParent(dataCountry,key) == union:
					tmp.append(key)
			yprint(f'union : {union} -> list : {sorted(tmp)}')
		yprint('********')

		if len(unitedSet) == N**2:
			break
		else:
			count += 1

		for parentCountry in unitedSet:
			sumNum = 0
			countNum = 0
			record = []
			for key, value in dataCountry.items():
				if findParent(dataCountry,key) == parentCountry:
					record.append(key)
					countNum += 1
					sumNum += dataMap[key[0]][key[1]]

			yprint(f'record : {record}')
			yprint(f'sumNum, countNum : {sumNum, countNum}')
			targetVal = sumNum // countNum
			yprint(f'targetVal : {targetVal}')
			for country in record:
				dataMap[country[0]][country[1]] = targetVal

			yprint(f'  >  dataMap middle : ')
			#pprint.pprint(dataMap, )

	yprint(f'dataMap final : {dataMap}')
	print(count)

if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(5)