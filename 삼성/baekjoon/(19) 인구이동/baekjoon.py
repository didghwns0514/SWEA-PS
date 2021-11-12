def wrapper(i):

	for j in range(i):
		N, L, R, dataMap = init()
		solution(j, N, L, R, dataMap)

def findParent(dataCountry, country):
	if dataCountry[country] == country:
		return country
	else:
		return findParent(dataCountry, dataCountry[country])

def unionFind(dataCountry, country1, country2):
	parent1 = findParent(dataCountry, country1)
	parent2 = findParent(dataCountry, country2)

	if parent1 != parent2: # avoid cycle
		dataCountry[parent1] = parent2

def init():
	N, L, R = map(int, input().split())
	dataMap = [ list(map(int, input().split())) for _ in range(N) ]

	return N, L, R, dataMap

def solution(testIter, N, L, R, dataMap):
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]
	yMax, xMax = N-1, N-1
	count = 0
	while True:

		dataCountry = {(rowIdx, colIdx):(rowIdx, colIdx) for rowIdx, rowVal in enumerate(dataMap) \
					   for colIdx, colVal in enumerate(rowVal)}

		for rowIdx, rowVal in enumerate(dataMap):
			for colIdx, colVal in enumerate(rowVal):
				for direction in range(4):
					nextY = rowIdx + dy[direction]
					nextX = colIdx + dx[direction]
					if 0 <= nextY <= yMax and 0 <= nextX <= xMax:
						targetCountryVal = dataMap[nextY][nextX]
						if L <= abs(targetCountryVal - colVal) <= R:
							unionFind(dataCountry, country1=(rowIdx, colIdx), country2=(nextY,nextX))

		dataCountry = {key : findParent(dataCountry, key) for key, value in dataCountry.items()}

		unitedSet = set([ value for key, value in dataCountry.items() ])

		for union in unitedSet:
			tmp = []
			for key, val in dataCountry.items():
				if  val == union:
					tmp.append(key)


		if len(unitedSet) == N**2:
			break
		else:
			count += 1

		for parentCountry in unitedSet:
			sumNum = 0
			countNum = 0
			record = []
			for key, value in dataCountry.items():
				if value == parentCountry:
					record.append(key)
					countNum += 1
					sumNum += dataMap[key[0]][key[1]]
			targetVal = sumNum // countNum
			for country in record:
				dataMap[country[0]][country[1]] = targetVal

	print(count)

if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(5)