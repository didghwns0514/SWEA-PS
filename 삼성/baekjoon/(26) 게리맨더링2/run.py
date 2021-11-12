
def tWrapper():

	def test1():
		d1, d2 = 2, 2
		N = 7
		dataMap = [[0]*7 for _ in range(7)]
		tmpDistrict = draw_Boarder(d1=d1,d2=d2,dataMap=dataMap, N=N)

		for key, value in tmpDistrict.items():
			if key == (3, 1):
				for pos in value:
					dataMap[pos[0]][pos[1]] = 5

				for r in range(N):
					for c in range(N):
						dataMap[r][c] = selectDistrictNum(key[0], key[1], r, c, d1, d2, N, value)

		return

	def test2():
		d1, d2 = 3, 2
		N = 7
		dataMap = [[0]*7 for _ in range(7)]
		tmpDistrict = draw_Boarder(d1=d1,d2=d2,dataMap=dataMap, N=N)


		for key, value in tmpDistrict.items():
			if key == (4, 1):
				for pos in value:
					dataMap[pos[0]][pos[1]] = 5

				for r in range(N):
					for c in range(N):
						dataMap[r][c] \
							= selectDistrictNum(key[0], key[1], r, c, d1, d2, N, value)


				return

	def test3():
		d1, d2 = 1, 1
		N = 7
		dataMap = [[0]*7 for _ in range(7)]
		tmpDistrict = draw_Boarder(d1=d1,d2=d2,dataMap=dataMap, N=N)

		key =  (4, 1)
		value = [(4, 1), (3, 2), (4, 1), (5, 2), (3, 2), (4, 3), (5, 2), (4, 3), (4, 2)]

		for pos in value:
			dataMap[pos[0]][pos[1]] = 5

			for r in range(N):
				for c in range(N):
					dataMap[r][c] \
						= selectDistrictNum(key[0], key[1], r, c, d1, d2, N, value)

			dataMap

	def test4():
		d1, d2 = 10, 10
		N = 7
		dataMap = [[0]*7 for _ in range(7)]
		tmpDistrict = draw_Boarder(d1=d1,d2=d2,dataMap=dataMap, N=N)

		for key, value in tmpDistrict.items():
			if key == (4, 1):
				for pos in value:
					dataMap[pos[0]][pos[1]] = 5

				for r in range(N):
					for c in range(N):
						dataMap[r][c] \
							= selectDistrictNum(key[0], key[1], r, c, d1, d2, N, value)


		return

	test1()
	test2()
	test3()
	test4()

def wrapper(i):
	for j in range(i):
		N, dataMap = init()
		returnValue = solution(j, N, dataMap)
		#print(f'#{j+1} {returnValue}')
		print(returnValue)

def init():

	N = int(input())
	dataMap = [ list(map(int, input().split())) for _ in range(N) ]

	return N, dataMap

def selectDistrictNum(y, x, r, c, d1, d2, N, area5):


	if (r, c) not in area5:

		if 0 <= r <= y - 1 and 0 <= c <= x + d1:
			return 1
		elif 0 <= r <= y + d2 - d1  and c > x + d1:
			return 2
		elif r > y - 1 and 0 <= c < x + d2:
			return 3
		else: return 4
	else:
		return 5


def draw_Boarder(d1,d2,dataMap, N):

	returnList = {}
	for y in range(N):
		for x in range(N):
			if d1 >= 1 and d2 >= 1 \
				and 1 <= x+1 < x+1 + d1 + d2 <= N \
				and 1 <= y+1 - d1 < y+1 < y+1 + d2 <= N:
				if (y, x) not in returnList:
					returnList[(y, x)] = []
				# 1)
				for i in range(d1+1):
					returnList[(y, x)].append( (y-i, x+i) )
				# 2)
				for i in range(d2+1):
					returnList[(y, x)].append( (y+i, x+i) )
				# 3)
				for i in range(d2+1):
					returnList[(y, x)].append( (y-d1+i, x+d1+i) )
				# 4)
				for i in range(d1+1):
					returnList[(y, x)].append( (y+d2-i, x+d2+i) )

				tmpData1 = list(set(returnList[(y, x)]))
				tmpData = sorted(tmpData1)
				posCurr = tmpData[0]
				sweepedList = []
				for data in tmpData:
					rowNum, colNum = data[0], data[1]
					endPoint = None
					for k in range(colNum, N):
						if (rowNum, k) in tmpData:
							endPoint = (rowNum, k)
					if endPoint == data:
						continue
					else:
						sweepedList.extend( [ (rowNum, j) for j in range(colNum, endPoint[1]+1) ] )

				tmpSet = set(returnList[(y, x)])
				tmpSet.update(sweepedList)
				returnList[(y, x)] = list(tmpSet)

	return returnList


def solution(testIter, N, dataMap):

	answer = 1e9

	# 길이와 index 조심
	for d1 in range(1, N+1):
		for d2 in range(1, N+2):
			tmpDistrict = draw_Boarder(d1,d2,dataMap, N)

			for key, area5 in tmpDistrict.items():

				tmpRecord = {1:0, 2:0, 3:0, 4:0, 5:0}
				mapRecord = {1:[], 2:[], 3:[], 4:[], 5:[]}
				for r in range(N):
					for c in range(N):
						selNum = selectDistrictNum(key[0], key[1], r, c, d1, d2, N, area5)
						tmpRecord[selNum] += dataMap[r][c]
						mapRecord[selNum].append((r,c))

				tmpMax = tmpRecord[max(tmpRecord.items(), key= lambda x:x[1])[0]]
				tmpMin = tmpRecord[min(tmpRecord.items(), key= lambda x:x[1])[0]]

				tmpAnswer = abs(tmpMax - tmpMin )

				if tmpAnswer < answer:
					answer = tmpAnswer

	return answer

if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')


	#tWrapper()

	#T = int(input())
	T = 3
	wrapper(T)