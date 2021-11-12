from collections import deque
import  math
import copy

def tWrapper():
	pass

def yprint(string, isEnabled=True):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint('\n'*2)
		yprint(f'#'*30)
		dataDragon, q = init()
		solution(j, dataDragon, q)

def init():
	N = int(input())
	dataDragon = [ list(map(int, input().split(' '))) for _ in range(N) ]
	q = deque()

	yprint(f'N, dataDragon : {N, dataDragon}')

	return dataDragon, q

def rotate90Clock(position):
	# y, x
	posy, posx = position
	return [posx, -posy]

def generageDragon(x, y, d, g):

	genCount = 0
	q = deque()
	q.append([0,0]) # 시작 -> 끝
	endPoint = [0,1]
	if d == 0 :pass
	elif d == 1 : endPoint = [-1, 0]
	elif d == 2 : endPoint = [0, -1]
	elif d == 3 : endPoint = [1, 0]
	q.append(endPoint)

	while genCount < 3:
		yprint(f'q: {q}')
		fPoint = max(q, key=lambda k : math.sqrt( (k[0])**2 + (k[1])**2 ))
		print(f'fPoint : {fPoint}')
		qNext = copy.deepcopy(q)
		qNext = list(map(lambda p: rotate90Clock([p[0]-fPoint[0], p[1]-fPoint[1]]), qNext))
		yprint(f'qNext - mid1 : {qNext}')
		# qNext = list(map(lambda p: [p[0]+fPoint[0], p[1]+fPoint[1]], qNext))
		# yprint(f'qNext - mid2 : {qNext}')
		deltaY, deltaX = fPoint[0] - qNext[-1][0], fPoint[1] - qNext[-1][1]
		yprint(f'deltaY, deltaX : {deltaY, deltaX}')
		qNext = deque(map(lambda p: [p[0]+deltaY, p[1]+deltaX], qNext))
		qNext.reverse()
		yprint(f'qNext final : {qNext}')

		for posNext in qNext:
			if posNext in q: pass
			else:q.append(posNext)
		yprint(f' > q final : {q}')
		genCount += 1

	tmpResult = deque(map(lambda k: [k[0] + y, k[1]+x], q ))
	yprint(f'tmpResult : {tmpResult}')
	return tmpResult


def solution(testIter, dataDragon, q):

	totalSet = set()
	for data in dataDragon:
		yprint('')
		yprint('-'*20)
		x, y, d, g = data
		yprint(f'x, y, d, g  :{x, y, d, g }')

		tmpResult = list(generageDragon(x, y, d, g))
		tmpResult = [ tuple(data) for data in tmpResult ]
		yprint(f'tmpResult : {tmpResult}')
		totalSet.update(tmpResult)

		# farthest
		# try:fPoint = max(points, key=lambda x : print(x, end=" dragon"))
		# except:pass
	yprint(f'totalSet : {totalSet}')
	yprint(f'len(totalSet : {len(totalSet)}')





if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(4)
