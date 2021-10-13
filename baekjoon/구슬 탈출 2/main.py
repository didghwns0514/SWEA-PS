
# red를 구멍으로 빼내고, 파란색은 건드리지 말것


import copy
import sys
import pprint

sys.setrecursionlimit(10000000)

def createMap(N, M): #세로, 가로
	map = []
	for _ in range(N):
		map.append(list(input('createMap')))

	return map

def isRollingFinished(map):

	for rowIndex, rowValue in enumerate(map):
		for colIndex, colValue in enumerate(rowValue):
			if colValue == 'R':
				return False
	return True


def tilt(_map, direction):
	# dir 0 : right
	# dir 1 : down
	# dir 2 : left
	# dir 3 : up
	dx = [1, 0, -1, 0]
	dy = [0, -1, 0, 1]
	map = copy.deepcopy(_map)

	for rowIndex, rowValue in enumerate(map):
		for colIndex, colValue in enumerate(rowValue):

			if colValue in ['R', 'B']:
				if map[colIndex+dy[direction]][rowIndex+dx[direction]] == '.':
					tmpOriginal = map[colIndex][rowIndex]
					map[colIndex][rowIndex] = '.'
					map[colIndex+dy[direction]][rowIndex+dx[direction]] = tmpOriginal

				elif map[colIndex+dy[direction]][rowIndex+dx[direction]] in ['R', 'B', '#']:
					pass

				elif map[colIndex+dy[direction]][rowIndex+dx[direction]] == 'O':
					if colValue == 'R':
						map[colIndex][rowIndex] = '.'
					elif colValue == 'B':
						return '', False
	return map, True

def search(record, map, cnt, depth):
	print(f'depth : {depth}')
	print(f'map : ')
	pprint.pprint(map)
	print(f'cnt : {cnt}-')
	print(f'record :{record}')
	if cnt > 10:
		record.append(-1)
		return

	if isRollingFinished(map):
		record.append(cnt)
		return


	for j in range(4):
		tmpMap, tmpBool = tilt(map, j)
		if tmpBool:
			search(record, tmpMap, cnt+1, depth+1)



def solution():
	print('sss')
	#map = createMap(N,M)
	map = [['#', '#', '#', '#', '#'], ['#', '.', '.', 'B', '#'], ['#', '.', '#', '.', '#'], ['#', 'R', 'O', '.', '#'], ['#', '#', '#', '#', '#']]
	print(f'map : {map}')

	record = []
	search(record, map, 0, 1)
	print(f'record : {record}')

if __name__ == '__main__':
	# N, M = list(map(int, input('N, M : ').split(' ')))
	# print('ff')
	print(f'solution : {solution()}')