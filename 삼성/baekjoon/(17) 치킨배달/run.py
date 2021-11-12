
def yprint(string, isEnabled = True):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		dataMap, M = init()
		solution(j, dataMap, M)

def init():
	N, M = list(map(int, input().split(' ')))
	dataMap = [ list(map(int, input().split())) for _ in range(N)]

	return dataMap, M

def getShortestDistance(dataChicken, housePosY, housePosX):

	sums = 1e9
	for data in dataChicken:
		tmp = abs(data[0]-housePosY) + abs(data[1] - housePosX)
		sums = min(sums, tmp)
	return sums

def solution(testIter, dataMap, M):
	chickenPlace =[ (idxRow, idxCol) for idxRow, data in enumerate(dataMap) for idxCol, val in enumerate(data) if val == 2]
	yprint(f'chickenPlace : {chickenPlace}')

	dataHouse = []
	for idxCol, valCol in enumerate(dataMap):
		for idxRow, valRow in enumerate(valCol):
			if valRow == 1:
				dataHouse.append((idxCol, idxRow))

	tmpChosen = list(itertools.combinations(chickenPlace, M))
	yprint(f'tmpChosen : {tmpChosen}')
	yprint(f'dataHouse : {dataHouse}')

	finalAnswer = 1e9
	for chosen in tmpChosen:
		yprint('')
		yprint(f'-'*20)
		yprint(f'chosen : {chosen}')
		tmpAnswer = 0

		for house in dataHouse:
			shortestDistance = getShortestDistance(chosen, house[0], house[1])
			tmpAnswer += shortestDistance
		finalAnswer = min(finalAnswer, tmpAnswer)

	yprint(f'finalAnswer : {finalAnswer}')

if __name__ == '__main__':
	import sys
	import itertools
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(4)