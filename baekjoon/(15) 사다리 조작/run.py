import copy

answer = 1e9
def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint('\n'*2)
		yprint(f'#'*30)
		N, M, H, dataMap = init()
		solution(j, N, M, H, dataMap)

def init():
	global answer

	answer = 1e9

	get =  list(map(int, input().split(' ')))
	yprint(f'get : {list(get)}')
	N, M, H = get
	dataMap = None
	if M >0 :
		dataMap = [ list(map(int, input().split(' '))) for _ in range(M) ]
	else:
		dataMap = []

	yprint(f'N, M, H : {N, M, H}')
	yprint(f'dataMap : {dataMap}')

	return N, M, H, dataMap

def getLadderResult(N, M, H, dataConnect):

	resultDict = {nPos:None for nPos in range(N)}
	# yprint(f'resultDict initial : {resultDict}')

	for _nPos in range(N):
		visitedSet = set()
		mPos = 0
		nPos = _nPos
		visitedSet.add((mPos, nPos))
		#yprint(f'_nPos : {_nPos}')
		while True:
			# yprint(f'nPos before : {nPos}')
			# yprint(f'mPos before : {mPos}')

			if mPos > H-1:
				resultDict[_nPos] = nPos
				break
			if (mPos, nPos) not in dataConnect:
				mPos += 1
			else:
				if dataConnect[(mPos, nPos)] in visitedSet:
					mPos += 1
				else:
					nPos = dataConnect[(mPos, nPos)][1]

			visitedSet.add((mPos, nPos))
			# yprint(f'nPos after : {nPos}')
			# yprint(f'mPos after : {mPos}')

	yprint(f'resultDict after : {resultDict}')

	if all([ key==value for key, value in resultDict.items() ]): return True
	else: return False

def solution(testIter, N, M, H, dataMap):
	global answer


	dataConnect = {}
	for data in dataMap:
		a, b = data
		a, b = a-1, b-1
		dataConnect[(a, b)] = (a, b+1)
		dataConnect[(a, b+1)] = (a, b)
	yprint(f'dataConnect : {dataConnect}')
	result = subSolution( 0, N, M, H, dataConnect)
	yprint(f'result : {result}')


	if answer > 3:
		yprint(f'answer : {-1}')
		print(-1)
	else:
		yprint(f'answer : {answer}')
		print(answer)

def subSolution( counter, N, M, H, dataConnect ):
	global answer

	if counter > answer:
		return

	if counter > 3:
		return

	if getLadderResult(N, M, H, dataConnect):
		answer = min(answer, counter)
		yprint(f'dataConnect after : {dataConnect}')
		return

	for idxN in range(N):
		if idxN == N-1:
			continue
		for idxH in range(H):
			if (idxH, idxN) not in dataConnect and (idxH, idxN+1) not in dataConnect:
				tmpCopyDC = copy.deepcopy(dataConnect)
				tmpCopyDC[ (idxH, idxN) ] = (idxH, idxN+1)
				tmpCopyDC[ (idxH, idxN+1) ] = (idxH, idxN)
				subSolution(counter+1, N, M, H, tmpCopyDC )


if __name__ == "__main__":

	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(7)