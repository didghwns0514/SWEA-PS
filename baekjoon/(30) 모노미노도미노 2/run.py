
def twrapper():
	pass

def wrapper(i):

	for j in range(i):
		N, dataPlace = init()
		score, tmpSum = solution(j, N, dataPlace)
		print(score)
		print(tmpSum)

def init():
	N = int(input())
	dataPlace = [ list(map(int, input().split())) for _ in range(N)]

	return N, dataPlace

def solution(testIter, N, dataPlace):

	mapBlue = [ [0]*6 for _ in range(4)]
	mapGreen = [ [0]*4 for _ in range(6) ]
	score = 0

	reverseF = lambda x: [x[1], x[0]]

	for data in dataPlace:
		t, x, y = data
		blockBlue, blockGreen = [], []
		if t == 1:
			blockBlue.append( [x, 0] )
			blockGreen.append( [0, y])
		elif t == 2:
			blockBlue.append( [x, 0] )
			blockBlue.append( [x, 1] )
			blockGreen.append( [0, y])
			blockGreen.append( [0, y+1])
		elif t ==3:
			blockBlue.append( [x, 0] )
			blockBlue.append( [x+1, 0] )
			blockGreen.append( [0, y])
			blockGreen.append( [1, y])


		# Blue
		jumpNBlue = 0
		for k in range(6):
			isFin = False
			for block in blockBlue:
				y, x = block
				if 0<=y<=3 and 0<=x+1+k<=5 and mapBlue[y][x+1+k] == 0:
					pass
				else:
					isFin = True
					break
			if isFin: break
			else:jumpNBlue += 1
		for block in blockBlue:
			y, x = block
			mapBlue[y][x+jumpNBlue] = 1

		# Green
		jumpNGreen = 0
		for k in range(6):
			isFin = False
			for block in blockGreen:
				y, x = block
				if 0<=y+1+k<=5 and 0<=x<=3 and mapGreen[y+1+k][x] == 0:
					pass
				else:
					isFin = True
					break
			if isFin:break
			else:jumpNGreen += 1
		for block in blockGreen:
			y, x = block
			mapGreen[y+jumpNGreen][x] = 1

		# Blue
		blueCnt = 0
		for blueColIdx in range(2):
			if any( [mapBlue[i][blueColIdx] == 1 for i in range(4)] ):
				blueCnt += 1
		if blueCnt:
			for k in range(5-blueCnt, -1, -1):
				for n in range(3+1):
					mapBlue[n][k+1] = mapBlue[n][k]
					mapBlue[n][k] = 0 #지우기
		# Green
		greenCnt = 0
		for greenRowIdx in range(2):
			if any( [mapGreen[greenRowIdx][i] == 1 for i in range(4)] ):
				greenCnt += 1
		if greenCnt:
			for k in range(5-greenCnt, -1, -1):
				for n in range(3+1):
					mapGreen[k+1][n] = mapGreen[k][n]
					mapGreen[k][n] = 0 #지우기



		# Blue
		for blueColIdx in range(6):
			if all([ mapBlue[i][blueColIdx] == 1 for i in range(3+1)  ]):
				score += 1
				for j in range(3+1):
					mapBlue[j][blueColIdx] = 0
				for k in range(blueColIdx-1, -1, -1):
					for n in range(3+1):
						mapBlue[n][k+1] = mapBlue[n][k]
						mapBlue[n][k] = 0 #지우기
		# Green
		for greenRowIdx in range(6):
			if all([ mapGreen[greenRowIdx][i] == 1 for i in range(3+1) ]):
				score += 1
				for j in range(3+1):
					mapGreen[greenRowIdx][j] = 0
				for k in range(greenRowIdx - 1, -1, -1):
					for n in range(3+1):
						mapGreen[k+1][n] = mapGreen[k][n]
						mapGreen[k][n] = 0


	tmpSum = 0
	tmpSum += sum([ sum(data) for data in mapBlue ])
	tmpSum += sum([ sum(data) for data in mapGreen ])

	return score, tmpSum




if __name__ == "__main__":

	import sys
	sys.stdin = open('sample_input.txt', 'r')

	# T = int(input())
	T = 1
	wrapper(T)
