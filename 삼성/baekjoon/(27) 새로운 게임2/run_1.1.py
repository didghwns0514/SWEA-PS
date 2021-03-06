def tWrapper():
	def test1():
		list1 = []
		list1.insert(0, 1)
		list1.insert(0, 2)
		list1.insert(0, 3)

		list2 = [1,2,3]
		tmpIndex = len(list2)
		list2.insert(tmpIndex, 4)
		list2.insert(tmpIndex, 5)
		list2.insert(tmpIndex, 6)
		list1

	#test1()

def wrapper(i):

	for j in range(i):
		N, K, dataColor, dataMap, dataObject = init()
		returnValue = solution(j, N, K, dataColor, dataMap, dataObject)
		#print(f'#{j+1} {returnValue}')
		print(returnValue)

def init():
	N, K = map(int, input().split())
	dataColor = [ list(map(int, input().split())) for _ in range(N)]
	dataMap = [ list([] for _ in range(N)) for _ in range(N)  ]
	dataObject = {}
	for j in range(1, K+1):
		tmpParse = list(map(int, input().split()))
		dataObject[j] = [tmpParse[0]-1, tmpParse[1]-1, tmpParse[2]-1]

	return N, K, dataColor, dataMap, dataObject

def reverseDir(direction):
	if direction == 0:
		return 1
	elif direction == 1:
		return 0
	elif direction == 2:
		return 3
	elif direction == 3:
		return 2

def isFinished(dataMap):

	for idxRow, valRow in enumerate(dataMap):
		for idxCol, valCol in enumerate(valRow):
			if len(dataMap[idxRow][idxCol]) >= 4 :
				return True
	else:
		return False

def solution(testIter, N, K, dataColor, dataMap, dataObject):
	"""

	:param testIter:
	:param N:
	:param K:
	:param dataMap: 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색
	:param dataObject: 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향
		이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미
	:return:
	"""
	dy = [0, 0, -1, 1]
	dx = [1, -1, 0, 0]


	for objectNum in sorted(dataObject.keys()):
		y, x, d = dataObject[objectNum]
		dataMap[y][x].append(objectNum)

	for turn in range(1000):

		for objectNum in range(1, K+1):

			y, x, d = dataObject[objectNum]
			ny = y + dy[d]
			nx = x + dx[d]

			isBlueOrOut = False
			if not (0 <= ny <= N-1 and 0 <= nx <= N-1):
				isBlueOrOut = True
			elif dataColor[ny][nx] == 2:
				isBlueOrOut = True

			if isBlueOrOut:
				dataObject[objectNum][2] = reverseDir(d)
				d = reverseDir(d)
				nny = y + dy[d]
				nnx = x + dx[d]

				if not (0 <= nny <= N-1 and 0 <= nnx <= N-1):
					continue
				else:
					if dataColor[nny][nnx] == 2:
						continue
					else:
						ny, nx = nny, nnx


			if dataColor[ny][nx] == 0: # 흰색
				objIndex = dataMap[y][x].index(objectNum)
				right = dataMap[y][x][:objIndex]
				left = dataMap[y][x][objIndex:]
				dataMap[y][x] = right
				dataMap[ny][nx].extend(left)
				for number in left:
					dataObject[number][0], dataObject[number][1] = ny, nx

			elif dataColor[ny][nx] == 1: # 빨강
				objIndex = dataMap[y][x].index(objectNum)
				right = dataMap[y][x][:objIndex]
				left = dataMap[y][x][objIndex:]
				dataMap[y][x] = right
				left.reverse()
				dataMap[ny][nx].extend(left)
				for number in left:
					dataObject[number][0], dataObject[number][1] = ny, nx


			if len(dataMap[ny][nx]) >= 4:
				return turn + 1


	return -1


if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')

	tWrapper()

	#T = int(input())
	T = 5
	wrapper(T)