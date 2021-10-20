
def wrapper(i):

	for j in range(i):
		R, C, M, dataSharkDict = init()
		solution(j, R, C, M, dataSharkDict)


def init():
	R, C, M = map(int, input().split())
	dataMap = [ [ [] for _ in range(C)]  for _ in range(R) ]
	dataSharkInfo = [list(map(int, input().split())) for _ in range(M)]
	# . 상어의 정보는 다섯 정수 r, c, s, d,
	# 다. (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
	dataSharkDict = {(valRow[0]-1, valRow[1]-1) : (valRow[2], valRow[3], valRow[4]) for idxRow, valRow in enumerate(dataSharkInfo) }


	return R, C, M, dataSharkDict

# s, d, z = shark #  s는 속력, d는 이동 방향, z는 크기
#  d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
def sharkNextDir(R, C,  s, _d, z, yCurPos, xCurPos):
	_s = s
	d = _d - 1
	dx = [0, 0, 1, -1]
	dy = [-1, 1, 0, 0]
	nY, nX = yCurPos, xCurPos
	while s > 0:

		s -= 1

		if nY == R - 1 and d == 2 - 1 :
			d = 1 - 1
		elif nY == 0 and d == 1 -1 :
			d = 2 - 1
		if nX == C - 1 and d == 3 - 1 :
			d = 4 - 1
		elif nX == 0 and d == 4 -1 :
			d = 3 - 1

		nY += dy[d]
		nX += dx[d]

		# if s > 0:
		# 	if nX < 0:
		# 		d = 3 - 1
		# 		nX = 1
		# 	elif nX > C - 1:
		# 		d = 4 - 3
		# 		nX = C - 2
		# 	elif nY < 0:
		# 		d = 2 - 1
		# 		nY = 1
		# 	elif nY > R - 1:
		# 		d = 1 - 1
		# 		nY = R - 2


	return _s, d + 1, z, nY, nX

def solution(testIter, R, C, M, dataSharkDict):

	fisherColPos = -1
	catchCount = 0

	while fisherColPos < C :

		# 1) 낚시왕이 오른쪽으로 한 칸 이동한다.
		fisherColPos += 1

		# 2) 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
		# 격자에 1마리만 존재
		rmPos = None
		for rowPos in range(R):
			if (rowPos, fisherColPos) in dataSharkDict:
				rmPos = (rowPos, fisherColPos)
				break
		if rmPos != None:
			shark = dataSharkDict.pop(rmPos)
			catchCount += shark[2]

		# 3) move shark
		nextSharkPosInfo = {}
		for keyPos, valShark in dataSharkDict.items():
			# # s, d, z = shark #  s는 속력, d는 이동 방향, z는 크기
			s, d, z = valShark[0], valShark[1], valShark[2]

			ns, nd, nz, nY, nX = sharkNextDir(R, C,  s, d, z, yCurPos=keyPos[0], xCurPos=keyPos[1])
			if (nY, nX) not in nextSharkPosInfo:
				nextSharkPosInfo[(nY, nX)] = (ns, nd, nz)
			else:
				_s, _d, _z = nextSharkPosInfo[(nY, nX)]
				if nz > _z:
					nextSharkPosInfo[(nY, nX)] = (ns, nd, nz)
			pass

		dataSharkDict = nextSharkPosInfo

		pass

	print(catchCount)




if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(4)