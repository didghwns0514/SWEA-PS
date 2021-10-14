import sys
import time

def yprint(string, isEnabled=True):
	if isEnabled:
		print(string)

def wrapper(i):
	start = time.time()
	for j in range(i):
		N, M, dataMap = init()
		solution(j, N, M, dataMap)
		# for _ in range(17):
		# 	solution(j, N, M, dataMap)

	yprint(f'elapsed time : {time.time() - start}')

def rotate(tmpData, degreeType):
	if degreeType == 0 :
		return tmpData
	elif degreeType == 1:
		return [ [ -data[1], data[0]] for data in tmpData ]
	else:
		return rotate([ [ -data[1], data[0]] for data in tmpData ], degreeType-1)

def reflect(tmpData, mirrorType, tetroType):
	if mirrorType == 0 or tetroType in [1, 2] : # no mirror
		return tmpData
	else:
		return [ [data[1], data[0]] for data in tmpData ]

def buildTetro(dataMap, tetroType, degreeType, mirrorType, yPos, xPos):

	tmpData = []
	if tetroType == 1:
		tmpData = [[0,0], [0,1], [0,2], [0,3]]
	elif tetroType == 2:
		tmpData = [[0,0], [0,1], [1,0], [1,1]]
	elif tetroType == 3:
		tmpData = [[0,0], [0,1], [1,0], [2,0]]
	elif tetroType == 4:
		tmpData = [[0,1], [1,0], [1,1], [2,0]]
	elif tetroType == 5:
		tmpData = [[0,1], [1,0], [1,1], [1,2]]

	#print(f'tmpData1 : {tmpData}')
	tmpData = rotate(tmpData, degreeType)
	#print(f'tmpData2 : {tmpData}')
	tmpData = reflect(tmpData, mirrorType, tetroType)
	#print(f'tmpData3 : {tmpData}')

	# add startpos
	tmpData = [[ data[0]+yPos, data[1]+xPos ] for data in tmpData  ]
	#print(f'tmpData4 : {tmpData}')

	# dataMap
	yMax = len(dataMap)
	xMax = len(dataMap[0])

	if all( [ 0 <= data[0] <= yMax -1 and 0 <= data[1] <= xMax - 1 for data in tmpData ] ):
		return True, [ dataMap[data[0]][data[1]] for data in tmpData ]
	else:
		return False, tmpData



def init():
	N, M = list(map(int, input().split(' ')))
	dataMap = [ list(map(int, input().split(' '))) for _ in range(N)]
	yprint(f'N, M : {N, M}')
	yprint(f'dataMap ; {dataMap}')

	return N, M, dataMap

def solution(testIndex, N, M, dataMap):

	answer = 0
	for yIndex, yValue in enumerate(dataMap):
		for xIndex, xValue in enumerate(yValue):
			for tetroType in range(1, 5+1):
				for degreeType in range(3+1):
					for mirrorType in range(1+1):
						rtnBool, selectedData = buildTetro(dataMap, tetroType, degreeType, mirrorType, yIndex, xIndex)
						if rtnBool:
							answer = max(sum(selectedData), answer)

	print(f'answer : {answer}')


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(3)