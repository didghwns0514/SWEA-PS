import sys
from collections import deque
import pprint

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):
	for _ in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		N, K, appleData, L, dirData, mapData, sec, q, direction = init()
		solution(i, N, K, appleData, L, dirData, mapData, sec, q, direction )

def createMap(_N, appleData):

	#
	N = _N + 2
	tmpRtn = [ [ (2 if(i2==0 or i2==N-1 or i1 ==0 or i1 == N-1) else 0) for i2, val2 in enumerate(range(N)) ] for i1, _ in enumerate(range(N)) ]

	# apple data
	for value in appleData:
		tmpRtn[value[0]][value[1]] = 1

	#yprint(f'tmpRtn : {pprint.pprint(tmpRtn)}')
	return tmpRtn

def init():
	sec = 0
	direction = 1
	q = deque([[1,1]])
	N = int(input())
	K = int(input())
	yprint(f'N :{N}, K : {K}')
	appleData = [ [data for data in  list(map(int, input().split(' ')))] for _ in range(K)]
	appleData = [ [data[0], data[1]] for data in appleData ]
	L = int(input())
	dirData = [ [ data for data in  list(input().split(' '))] for _ in range(L)]
	#dirData = [ [ [int(data[0]), data[1]] for data in  list(input().split(' '))] for _ in range(L)]
	dirData = list( map(lambda x : [int(x[0]), x[1]], dirData ))
	#yprint(f'appleData : {pprint.pprint(appleData)}')
	#yprint(f'dirData : {pprint.pprint(dirData)}')

	return N, K, appleData, L, dirData, createMap(N, appleData), sec, q, direction

def move(q, mapData, direction, xPos, yPos):

	dx = [0, 1, 0, -1]
	dy = [-1, 0, 1, 0]
	i = 0
	if direction == 0 : # up
		i = 0
	elif direction == 1 : # right
		i = 1
	elif direction == 2 : # down
		i = 2
	elif direction == 3 : # left
		i = 3

	xNext = xPos + dx[i]
	yNext = yPos + dy[i]
	yprint(f'yNext ; {yNext}, xNext : {xNext}')

	# Check
	isPass = True
	if mapData[yNext][xNext] == 2 or  [yNext, xNext] in q: # wall or body
		isPass = False
		yprint(f'false1')

	elif mapData[yNext][xNext] == 1 : # apple
		q.appendleft([yNext, xNext])
		mapData[yNext][xNext] = 0 # remove apple
		yprint(f'true1')

	else: # move to the direction
		q.pop()
		q.appendleft([yNext, xNext])
		yprint(f'true2')


	return isPass

def nextDir(direction, letter):
	if letter == 'D':
		direction += 1
	elif letter == 'L':
		direction -= 1

	if direction == 4:
		direction = 0
	elif direction == -1:
		direction = 3

	return direction

def solution(testIter, N, K, appleData, L, dirData, mapData, sec, q, direction ):


	isLive = True
	qHead = None
	while isLive:
		yprint(f'-'*20)

		if dirData:
			if dirData[0][0] == sec:
				yprint(f'^^^')
				yprint(f'direction before : {direction}')
				yprint(f'dirData[0][0] : {dirData[0][0]}')
				yprint(f'dirData before : {dirData}')
				data = dirData.pop(0)
				direction = nextDir(direction, data[1])
				yprint(f'dirData after : {dirData}')
				yprint(f'direction after : {direction}')
				yprint(f'^^^')
		qHead = q[0]
		yprint(f'qHead : {qHead}')
		yprint(f'q : {q}')
		yprint(f'sec : {sec}')
		yprint(f'direction : {direction}')
		isLive = move(q, mapData, direction, xPos=qHead[1], yPos=qHead[0])
		sec += 1

		tmpMapScan = [data[:] for data in mapData]
		for qIndex, pos in enumerate(q):
			if qIndex == 0:
				tmpMapScan[pos[0]][pos[1]] = 'H'
			else:
				tmpMapScan[pos[0]][pos[1]] = 'S'
		#yprint(f'tmpMapScan : {pprint.pprint(tmpMapScan)}')




	yprint(f'final sec : {sec}')
	print(sec)

if __name__ == '__main__':
	sys.stdin = open("sample_input.txt", "r")
	wrapper(1)
