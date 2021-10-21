
answer = 1e9

def wrapper(i):
	for j in range(i):
		D, W, K, dataFilm = init()
		returnValue = solution(j, D, W, K, dataFilm)
		print(f'#{j+1} {returnValue}')

def init():
	global answer
	answer = 1e9
	D, W, K = map(int, input().split())
	dataFilm = [ list(map(int, input().split())) for _ in range(D) ]

	return D, W, K, dataFilm

def checkTestPass(dataFilm, K, D):

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


def dfs(dataFilm, D, K, W, depthIdx=-1, counter=0):
	global answer

	if counter >= answer:
		return

	if answer == 2:
		return

	if checkTestPass(dataFilm, K, D) and counter != 1:
		answer = min(answer, counter)
		return

	if depthIdx >= D-1:
		return

	tmpDataLayer = copy.deepcopy(dataFilm[depthIdx])
	dfs(dataFilm, D, K, W, depthIdx=depthIdx+1, counter=counter)

	dataFilm[depthIdx] = [0]*W
	dfs(dataFilm, D, K, W, depthIdx=depthIdx+1, counter=counter+1)
	dataFilm[depthIdx] = copy.deepcopy(tmpDataLayer)

	dataFilm[depthIdx] = [1]*W
	dfs(dataFilm, D, K, W, depthIdx=depthIdx+1, counter=counter+1)
	dataFilm[depthIdx] = copy.deepcopy(tmpDataLayer)


def solution(testIter, D, W, K, dataFilm):
	global answer

	dfs(dataFilm, D, K, W, depthIdx=-1, counter=0)

	return answer

if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')

	import copy
	import itertools

	T = int(input())
	wrapper(T)