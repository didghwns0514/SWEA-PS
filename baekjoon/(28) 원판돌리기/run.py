
def tWrapper():
	pass

def wrapper(i):
	for j in range(i):
		N, M, T, dataCircle, dataSpin = init()
		returnValue = solution(j, N, M, T, dataCircle, dataSpin)
		print(returnValue)

def init():
	N, M, T = map(int, input().split())
	dataCircle = [ deque(list(map(int, input().split()))) for _ in range(N) ]
	dataSpin = [list(map(int, input().split())) for _ in range(T) ]

	return N, M, T, dataCircle, dataSpin

def idxNormNext(currIdxNorm, direction, M):
	if currIdxNorm == 0:
		if direction == -1:
			return M - 1
	elif currIdxNorm == M - 1:
		if direction == 1:
			return 0
	return currIdxNorm - 1 if direction == -1 else currIdxNorm + 1

def dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNorm):

	if (idxCircle, idxNorm) in visited:
		return False
	if dataCircle[idxCircle][idxNorm] != numberCheck:
		return False
	if numberCheck == 0:
		return False

	visited.append((idxCircle, idxNorm))

	if idxCircle == 0:

		dfs(dataCircle, M, numberCheck, visited, idxCircle+1, idxNorm)
		dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNormNext(idxNorm,-1, M))
		dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNormNext(idxNorm, 1, M))

	elif 0 < idxCircle < len(dataCircle) - 1 :
		dfs(dataCircle, M, numberCheck, visited, idxCircle-1, idxNorm)
		dfs(dataCircle, M, numberCheck, visited, idxCircle+1, idxNorm)
		dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNormNext(idxNorm,-1, M))
		dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNormNext(idxNorm, 1, M))

	elif idxCircle == len(dataCircle) - 1 :
		dfs(dataCircle, M, numberCheck, visited, idxCircle-1, idxNorm)
		dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNormNext(idxNorm,-1, M))
		dfs(dataCircle, M, numberCheck, visited, idxCircle, idxNormNext(idxNorm, 1, M))
		
	else:
		return False

def solution(testIter, N, M, T, dataCircle, dataSpin):

	for spinMethod in dataSpin:

		x, d, k = spinMethod
		isReplaceFound = False
		for idx in range(N): # 배수 rotation 해주기
			tmpVal = (idx + 1)
			if tmpVal % x == 0:
				dataCircle[idx].rotate(k * (1 if d == 0 else -1))

		dataCircle

		for _idxCircle in range(N):
			for _idxNorm in range(M):
				tmpVisited = []
				number = dataCircle[_idxCircle][_idxNorm]
				dfs(dataCircle, M, numberCheck=number,
					visited=tmpVisited,
					idxCircle=_idxCircle, idxNorm=_idxNorm)

				if len(tmpVisited) >= 2 :
					isReplaceFound = True
					for pos in tmpVisited:
						circle, norm = pos
						dataCircle[circle][norm] = 0

		if not isReplaceFound: # 평균 구하고 전부 바꿔주기
			count, sums = 0, 0
			for _idxCircle in range(N):
				for _idxNorm in range(M):
					if dataCircle[_idxCircle][_idxNorm] != 0 :
						sums += dataCircle[_idxCircle][_idxNorm]
						count += 1
			avg = sums / count

			for _idxCircle in range(N):
				for _idxNorm in range(M):
					if dataCircle[_idxCircle][_idxNorm] != 0 :
						if dataCircle[_idxCircle][_idxNorm] > avg :
							dataCircle[_idxCircle][_idxNorm] -= 1
						elif dataCircle[_idxCircle][_idxNorm] < avg :
							dataCircle[_idxCircle][_idxNorm] += 1

	answer = sum([ sum(data) for data in dataCircle ])
	return answer


if __name__ == "__main__":
	import sys
	sys.setrecursionlimit(10000)
	sys.stdin = open('sample_input.txt', 'r')

	from collections import deque

	#T = int(input())
	T = 5
	wrapper(T)