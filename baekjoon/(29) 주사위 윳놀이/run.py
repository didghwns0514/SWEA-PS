
answer = 0

def tWrapper():
	pass

def wrapper(i):

	for j in range(i):
		dataDice, mapData = init()
		returnValue = solution(j, dataDice, mapData)
		print(returnValue)

def makePoint(score, red=None, blue=None):
	return {'score':score, 'red':red, 'blue':blue}

def init():
	global answer
	answer = 0

	mapData = {
		'start' : makePoint(0, '2-1'),
		'2-1' : makePoint(2, '4-1'),
		'4-1' : makePoint(4, '6-1'),
		'6-1' : makePoint(6, '8-1'),
		'8-1' : makePoint(8, '10'),
		'10': makePoint(10, '12-2', '13-3'),
		'12-2': makePoint(12, '14-2'),
		'14-2': makePoint(14, '16-2'),
		'16-2': makePoint(16, '18-2'),
		'18-2': makePoint(18, '20'),
		'13-3': makePoint(13, '16-3'),
		'16-3': makePoint(16, '19-3'),
		'19-3': makePoint(19, '25'),
		'20': makePoint(20,  '22-6', '22-4'),
		'22-4': makePoint(22, '24-4'),
		'24-4': makePoint(24, '25'),
		'25' : makePoint(25, '30-5'),
		'30-5': makePoint(30, '35-5'),
		'35-5': makePoint(35, '40'),
		'22-6': makePoint(22, '24-6'),
		'24-6': makePoint(24, '26-6'),
		'26-6': makePoint(26, '28-6'),
		'28-6': makePoint(28, '30'),
		'30' : makePoint(30, '32-8', '28-7'),
		'28-7': makePoint(28, '27-7'),
		'27-7': makePoint(27, '26-7'),
		'26-7': makePoint(26, '25'),
		'32-8': makePoint(32, '34-8'),
		'34-8': makePoint(34, '36-8'),
		'36-8': makePoint(36, '38-8'),
		'38-8': makePoint(38, '40'),
		'40' : makePoint(40, 'end'),
		'end': makePoint(0)

	}

	dataDice = list(map(int, input().split()))

	return dataDice, mapData


def dfs(mapData, dataDice, position, index=0, count=10, score=0):
	global answer

	if count == 0:
		answer = max(answer, score)
	else:
		tmpPosition = [ data for data in position ]
		currPos = tmpPosition[index]
		fixStartPos = tmpPosition[index]
		tmpScore = 0
		tmpNumberIter = dataDice[10 - count]


		for _ in range(tmpNumberIter):
			# {'score':score, 'red':red, 'blue':blue}
			nextPositionDict = mapData[currPos]

			#tmpScore += nextPositionDict['score']

			if fixStartPos in ['10', '20',  '30'] and fixStartPos == currPos:
				currPos = nextPositionDict['blue']
			else:
				currPos = nextPositionDict['red']
			tmpScore = mapData[currPos]['score']

			# 끝에 도달
			if nextPositionDict['red'] == 'end' or nextPositionDict['blue'] == 'end':
				tmpScore = 0
				break


		if currPos in position and currPos != 'end' and currPos != 'start': # 다른 말이 이미 존재, 도착 아님
			return
		else:
			tmpPosition[index] = currPos
			score += tmpScore
			if tmpPosition[0] != 'end':
				tmpTmpPosition = [ data for data in tmpPosition ]
				dfs(mapData, dataDice, tmpTmpPosition, index=0, count=count-1, score=score)
			if tmpPosition[1] != 'end':
				tmpTmpPosition = [ data for data in tmpPosition ]
				dfs(mapData, dataDice, tmpTmpPosition, index=1, count=count-1, score=score)
			if tmpPosition[2] != 'end':
				tmpTmpPosition = [ data for data in tmpPosition ]
				dfs(mapData, dataDice, tmpTmpPosition, index=2, count=count-1, score=score)
			if tmpPosition[3] != 'end':
				tmpTmpPosition = [ data for data in tmpPosition ]
				dfs(mapData, dataDice, tmpTmpPosition, index=3, count=count-1, score=score)


def solution(testIter, dataDice, mapData):
	global answer

	horse = ['start' for _ in range(4)]
	dfs(mapData, dataDice, horse, index=0, count=10, score=0)
	horse = ['start' for _ in range(4)]
	dfs(mapData, dataDice, horse, index=1, count=10, score=0)
	horse = ['start' for _ in range(4)]
	dfs(mapData, dataDice, horse, index=2, count=10, score=0)
	horse = ['start' for _ in range(4)]
	dfs(mapData, dataDice, horse, index=3, count=10, score=0)

	return answer


if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')

	import itertools

	# T = int(input())
	T = 4
	wrapper(T)