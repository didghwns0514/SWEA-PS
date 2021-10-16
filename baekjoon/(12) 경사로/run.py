



def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint('\n'*2)
		yprint('#'*30)
		N, L, dataMap, dataRoadRow, dataRoadCol = init()
		solution(j, N, L, dataMap, dataRoadRow, dataRoadCol)

def init():
	N, L = list(map(int, input().split(' ')))
	dataMap = [ list(map(int, input().split(' '))) for _ in range(N)]
	dataRoadRow = {idx : False for idx in range(N)}
	dataRoadCol = {idx : False for idx in range(N)}

	yprint(f'N, L : {N, L }')
	yprint(f'dataMap : {dataMap }')
	yprint(f'dataRoadRow : {dataRoadRow }')
	yprint(f'dataRoadCol : {dataRoadCol }')

	return N, L, dataMap, dataRoadRow, dataRoadCol

def solution(testIndex, N, L, dataMap, dataRoadRow, dataRoadCol):

	subSolution(N, L, dataMap, dataRoadRow, dataRoadCol, select=0)
	subSolution(N, L, dataMap, dataRoadRow, dataRoadCol, select=1)

	yprint(f'dataRoadRow : {dataRoadRow}')
	yprint(f'dataRoadCol : {dataRoadCol}')

	length = len(list(filter(lambda x : dataRoadRow[x] == True, dataRoadRow))) + \
			 len(list(filter(lambda x : dataRoadCol[x] == True, dataRoadCol)))
	yprint(f'length : {length}')
	print(length)

def subSolution(N, L, dataMap, dataRoadRow, dataRoadCol, select):

	for  numKey in range(N):
		#if select == 0 : dataRoadRow
		tmpDatas = dataMap[numKey] if not select else [ dat[numKey] for dat in dataMap ]
		checkExistSet = set()
		tmpBridgeSet = set()
		yprint(f'-'*20)
		yprint(f'subSolution - tmpDatas : {tmpDatas}')
		yprint(f'selected: {select}')
		yprint(f'numKey : {numKey}')
		for idx, val in enumerate(tmpDatas):
			if idx == N-1:
				continue
			tmpExpectVal = tmpDatas[idx+1]
			if tmpExpectVal == val + 1: # 고도 상승
				tmpRange = range(idx, idx-L, -1)
				if not all([ 0 <= rng <= N - 1 for rng in tmpRange ]):
					break
				tmpDatas2 = [ tmpDatas[_idx] == val for _idx in tmpRange ]
				yprint(f'tmpRange : {tmpRange}')
				yprint(f'tmpDatas2 : {tmpDatas2}')
				if not( all( tmpDatas2 ) and all([ rng not in checkExistSet for rng in tmpRange ])):
					yprint('1')
					break
				else:
					yprint('1-1')
					checkExistSet.update(tmpRange)
			elif tmpExpectVal == val - 1: # 고도 하강
				tmpRange = range(idx+1, idx+1+L, 1)
				if not all([ 0 <= rng <= N - 1 for rng in tmpRange ]):
					break
				tmpDatas2 = [ tmpDatas[_idx] == tmpExpectVal for _idx in tmpRange ]
				yprint(f'tmpRange : {tmpRange}')
				yprint(f'tmpDatas2 : {tmpDatas2}')
				if not( all( tmpDatas2 ) and all([ rng not in checkExistSet for rng in tmpRange ])):
					yprint('2')

					break
				else:
					yprint('2-1')
					checkExistSet.update(tmpRange)
			else:
				if abs(tmpExpectVal - val) > 1:
					yprint('3-1')
					break
				else:pass


		else:
			yprint('5')
			if select == 0:
				dataRoadRow[numKey] = True
			else:
				dataRoadCol[numKey] = True
		yprint(f'checkExistSet : {checkExistSet}')


if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(4)

	# [3, 2, 2, 1, 1, 1]