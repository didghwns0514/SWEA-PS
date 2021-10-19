
from collections import deque

def yprint(string, isEnabled=True):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint(f'\n'*2)
		yprint('#'*30)
		qFish, sharkPos, N = init()
		solution(j, qFish, sharkPos, N)


def init():

	N = int(input())
	qFish = deque()
	dataMap = [ list(map(int, input().split())) for _ in range(N) ]

	sharkPos = None
	for idxRow, valRow in enumerate(dataMap):
		for idxCol, valCol in enumerate(valRow):
			if valCol == 9:
				sharkPos = (idxRow, idxCol)
			elif 1 <= valCol <= 6:
				qFish.append((idxRow, idxCol, valCol))

	yprint(f'dataMap : {dataMap}')
	yprint(f'N, qFish : {N, qFish}')
	yprint(f'sharkPos : {N, sharkPos}')

	return qFish, sharkPos, N

dx = [0, 0, -1, 1]
dy = [-1,1,  0, 0]


def bfs(yShark, xShark, sharkSize, fishDict, N, counter=0):

	visited = set()
	record = []
	q = deque()
	q.append((yShark, xShark, 0))

	yprint(f'q - initial : {q}')

	while q:

		qPosY, qPosX, _counter = q.popleft()

		if (qPosY, qPosX) not in visited:
			visited.add((qPosY, qPosX))

			if (qPosY, qPosX) in fishDict :
				if fishDict[(qPosY, qPosX)] < sharkSize:
					record.append((qPosY, qPosX, _counter))

			for i in range(4):
				yN = qPosY + dy[i]
				xN = qPosX + dx[i]
				if 0 <= yN <= N-1 and 0 <= xN <= N-1 and (yN, xN) not in visited :
					if (yN, xN) not in fishDict:

						q.append((yN, xN, _counter + 1))
					else:
						if not fishDict[(yN, xN)] > sharkSize:

							q.append((yN, xN, _counter + 1))
	return record

def solution(testIter, qFish, sharkPos, N):

	second = 0
	sharkY, sharkX = sharkPos
	sharkSize = 2
	sharkAte = 0

	while True:
		yprint('')
		yprint(f'-'*20)
		yprint(f'sharkAte, sharkSize : {sharkAte, sharkSize}')
		yprint(f'sharkY, sharkX : {sharkY, sharkX}')
		# eatFishInfo :  (y, x, fishSize)

		fishDict = { (y,x):size for idxQ, (y, x, size) in enumerate(qFish)}
		fishList = bfs( sharkY, sharkX, sharkSize, fishDict, N, counter=0)

		yprint(f'fishList : {fishList}')
		if not fishList: # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
			break
		# elif fishCount == 1: # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
		# 	second += abs(eatFishInfo[0] - sharkY) +  abs(eatFishInfo[1] - sharkX)
		# 	sharkY, sharkX = eatFishInfo[0], eatFishInfo[1]
		# 	sharkAte += 1
		# 	break
		else:

			yprint(f'fishDict : {fishDict}')
			yprint(f'sharkAte, sharkSize : {sharkAte, sharkSize}')
			pickedFish = sorted(fishList, key=lambda x : (x[2], x[0], x[1]))[0]
			shortestCnt = pickedFish[2]
			yprint(f'shortestCnt : {shortestCnt}')

			second += shortestCnt
			sharkAte += 1

			sharkY, sharkX =  pickedFish[0], pickedFish[1]

			tmpRmoveObj = None
			for fish in qFish:
				if (fish[0], fish[1]) == (pickedFish[0], pickedFish[1]):
					tmpRmoveObj = fish
					break
			qFish.remove(tmpRmoveObj)
			yprint(f'qFish : {qFish}')

		# 크기 증가
		if sharkAte == sharkSize:
			sharkSize += 1
			sharkAte = 0


	yprint(f'second : {second}')
	print(f'second : {second}')

if __name__ == "__main__":
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(6)