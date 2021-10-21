
def wrapper(i):

	for j in range(i):
		r, c, k, dataMap = init()
		returned = solution(j,  r, c, k, dataMap)
		print(returned)

def init():
	r, c, k = map(int, input().split())
	dataMap = [ list(map(int, input().split())) for _ in range(3)]

	return r, c, k, dataMap

def solution(testIter,  r, c, k, dataMap):
	"""
	1)_연산
	R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
	C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.

	각각의 수가 몇 번 나왔는지 알아야 한다.
	그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
	그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는,
	수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.

	"""

	for sec in range(101):
		# R연산 : 배열 A의 모든 행에 대해서 정렬을 수행한다.
		# 행의 개수 ≥ 열의 개수인 경우에 적용

		try:
			if dataMap[r-1][c-1] == k:
				return sec
		except:pass

		if len(dataMap) >= len(dataMap[0]):
			maxRowLength = 0
			for idxRow, valRow in enumerate(dataMap):
				resultDict = collections.Counter(valRow)


				tmpRow = sorted(
					[ (key, val) for key, val in  resultDict.items() if key!=0 ]
				, key=lambda x: (x[1], x[0]))

				resultRow = []
				for data in tmpRow:
					resultRow.append(data[0])
					resultRow.append(data[1])

				maxRowLength = max(maxRowLength, len(resultRow))
				dataMap[idxRow] = resultRow[:]

			for idxRow, valRow in enumerate(dataMap):
				dataMap[idxRow].extend(
					abs(len(valRow) - maxRowLength)*[0]
				)

			pass


		# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다.
		# 행의 개수 < 열의 개수인 경우에 적용
		else:
			maxColLength = 0
			tmpDataMap = [[0]*len(dataMap) for _ in range(len(dataMap[0]))]
			for i in range(len(dataMap)):
				for j in range(len(dataMap[0])):
					tmpDataMap[j][i] = dataMap[i][j]

			for idxRow, valRow in enumerate(tmpDataMap):
				resultDict = collections.Counter(valRow)

				tmpRow = sorted(
					[ (key, val) for key, val in  resultDict.items() if key!=0 ]
					, key=lambda x: (x[1], x[0]))

				resultRow = []
				for data in tmpRow:
					resultRow.append(data[0])
					resultRow.append(data[1])
				maxColLength = max(maxColLength, len(resultRow))
				tmpDataMap[idxRow] = resultRow[:]

			for idxRow, valRow in enumerate(tmpDataMap):
				tmpDataMap[idxRow].extend(
					abs(len(valRow) - maxColLength)*[0]
				)

			dataMap = [[0]*len(tmpDataMap) for _ in range(len(tmpDataMap[0]))]
			for i in range(len(tmpDataMap)):
				for j in range(len(tmpDataMap[0])):
					dataMap[j][i] = tmpDataMap[i][j]

			pass

		# 100개 미만으로 자르기!
		if len(dataMap) > 100:
			dataMap = dataMap[:100]
		if len(dataMap[0]) > 100:
			for idxRow, valRow in enumerate(dataMap):
				dataMap[idxRow] = valRow[:100]



	return -1




	pass

if __name__ == '__main__':
	import collections
	import sys
	import copy
	sys.stdin = open('sample_input.txt', 'r')

	wrapper(6)