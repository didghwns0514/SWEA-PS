
import sys
import copy

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		dataN, dataS, N = init()
		solution(j, dataN, dataS, N)

def init():
	N  = int(input())
	dataS = [ list(map(int, input().split(' '))) for _ in range(N)]
	yprint(f'N, dataS : {N, dataS}')

	return [1 for _ in range(N)], dataS, N

def solution2(testIter, dataN, dataS, N):

	record = []
	teamLink = []
	teamStart = []

	subSolution(record, 0, teamLink, teamStart,dataS,dataN,N)

	yprint(f'record : {record}')
	#print(f'record : {record}')
	tmpMin = min(record, key=lambda x: abs(x[0]-x[1]))
	tmpMin = abs(tmpMin[0]-tmpMin[1])
	print(tmpMin)

def solution(testIter, dataN, dataS, N):

	record = []
	teamLink = []
	teamStart = []

	import itertools

	# subSolution(record, 0, teamLink, teamStart,dataS,dataN,N)
	selectedIter = list(itertools.permutations(range(N), N))
	#yprint(f'selectedIter : {selectedIter}')

	for selected in  selectedIter:
		selectedLink = selected[:int(N/2)]
		selectedStart = selected[int(N/2):]

		scoreLink = getTeamScore(dataS, selectedLink)
		scoreStart = getTeamScore(dataS, selectedStart)

		record.append([scoreLink, scoreStart])

	minRecord = min(record, key=lambda x : abs(x[0]-x[1]))
	print(abs(minRecord[0] - minRecord[1]))

def getTeamScore(dataS, selectedIdx):

	score = 0
	yprint(f'selectedIdx :{selectedIdx}')
	for i1, v1 in enumerate(selectedIdx):
		tmpSelected = selectedIdx[i1+1:]
		for i2, v2 in enumerate(tmpSelected):
			if tmpSelected:
				yprint(f'v1, v2 : {v1, v2}')
				score += (dataS[v1][v2]+dataS[v2][v1])
	return score



if __name__ == '__main__':
	sys.stdin = open('sample_input.txt','r')
	wrapper(3)



"""

def wrapper(i):

	for j in range(i):
		dataN, dataS, N = init()
		solution(j, dataN, dataS, N)

def init():
	N  = int(input())
	dataS = [ list(map(int, input().split(' '))) for _ in range(N)]

	return [1 for _ in range(N)], dataS, N


def solution(testIter, dataN, dataS, N):

	record = []
	teamLink = []
	teamStart = []

	import itertools

	# subSolution(record, 0, teamLink, teamStart,dataS,dataN,N)
	selectedIter = list(itertools.permutations(range(N), N))
	#yprint(f'selectedIter : {selectedIter}')

	for selected in  selectedIter:
		selectedLink = selected[:int(N/2)]
		selectedStart = selected[int(N/2):]

		scoreLink = getTeamScore(dataS, selectedLink)
		scoreStart = getTeamScore(dataS, selectedStart)

		record.append([scoreLink, scoreStart])

	minRecord = min(record, key=lambda x : abs(x[0]-x[1]))
	print(abs(minRecord[0] - minRecord[1]))

def getTeamScore(dataS, selectedIdx):

	score = 0
	for i1, v1 in enumerate(selectedIdx):
		tmpSelected = selectedIdx[i1+1:]
		for i2, v2 in enumerate(tmpSelected):
			if tmpSelected:
				score += (dataS[v1][v2]+dataS[v2][v1])
	return score



if __name__ == '__main__':
	#sys.stdin = open('sample_input.txt','r')
	wrapper(1)
"""