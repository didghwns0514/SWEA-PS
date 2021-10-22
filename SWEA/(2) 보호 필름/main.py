
answer = 1e9

def wrapper(i):
	for j in range(i):
		D, W, K, dataFilm = init()
		returnValue = solution(j, D, W, K, dataFilm)
		if K == 1:

			print(f'#{j+1} {0}')
		else:
			print(f'#{j+1} {returnValue}')

def init():
	global answer
	answer = 1e9
	D, W, K = map(int, input().split())
	dataFilm = [ list(map(int, input().split())) for _ in range(D) ]

	return D, W, K, dataFilm

def checkTestPass3(dataFilm, K, D):

	dataResult = []
	for idxCol in range(len(dataFilm[0])):
		filmList = [ dataFilm[idxRow][idxCol] for idxRow in range(len(dataFilm)) ]
		filteredTemp = [ len(set(filmList[idxData:idxData+K])) == 1  for idxData, valData in enumerate(filmList)
						 if idxData <= D-1-K + 1 ]
		if any(filteredTemp):
			dataResult.append(True)
		else:
			dataResult.append(False)

	if all(dataResult):
		return True
	else:
		return False

def checkTestPass2(a, k, d):

	d,w = len(a),len(a[0])
	for i in range(w):
		tmp = [a[0][i],1]
		for j in range(1,d):
			if tmp[0] == a[j][i]:
				tmp[1]+=1
				if tmp[1]>=k:
					break
			else:
				tmp[0],tmp[1] = a[j][i],1
		else:
			return False
	return True

def checkTestPass(dataFilm, K, D):

	for idxCol in range(len(dataFilm[0])):
		isPass = False
		isSubPass = False

		for idxRow in range(0, len(dataFilm)-K+1):
			prevVal = dataFilm[idxRow][idxCol]
			for i in range(K):
				if not dataFilm[idxRow+i][idxCol] == prevVal:
					break
			else:
				isPass = True
				isSubPass = True

			if isSubPass:
				break

		if not isPass:
			return False
	return True

def dfs(dataFilm, D, K, W, depthIdx, counter=0):
	global answer

	if depthIdx == D:
		if checkTestPass(dataFilm, K, D) :
			if answer > counter:
				answer = counter
	else:
		dfs(dataFilm, D, K, W, depthIdx=depthIdx+1, counter=counter)
		if counter <= K:
			tmpDataLayer = [ x for x in dataFilm[depthIdx]]

			for idx in range(W):
				dataFilm[depthIdx][idx] = 0
			dfs(dataFilm, D, K, W, depthIdx=depthIdx+1, counter=counter+1)

			for idx in range(W):
				dataFilm[depthIdx][idx] = 1
			dfs(dataFilm, D, K, W, depthIdx=depthIdx+1, counter=counter+1)

			for idx, value in enumerate(tmpDataLayer):
				dataFilm[depthIdx][idx] = value



def solution(testIter, D, W, K, dataFilm):
	global answer

	dfs(dataFilm, D, K, W, depthIdx=0, counter=0)

	return answer

if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')


	T = int(input())
	wrapper(T)