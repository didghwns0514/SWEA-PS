import copy
import pprint

YEAR = ['spring', 'summer', 'fall', 'winter']
dx = [1,  1,  0,  -1,  -1, -1,  0,   1]
dy = [0,  1,  1,   1,   0, -1, -1,  -1]

def yprint(string, isEnabled=True):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		dataFertil, dataTreeInfo,dataMap, K, N = init()
		solution(j, dataFertil, dataTreeInfo, dataMap, K, N)

def init():
	N, M, K = map(int, input().split())
	dataFertil = [list(map(int, input().split())) for _ in range(N)]
	dataTreeInfo = [list(map(int, input().split())) for _ in range(M)]
	dataMap = [[5]*N for _ in range(N)]
	yprint(f'N, M, K : {N, M, K}')
	yprint(f'dataFertil : {dataFertil}')
	yprint(f'dataTreeInfo : {dataTreeInfo}')
	yprint(f'dataMap : {dataMap}')

	return dataFertil, dataTreeInfo, dataMap, K, N


def genTree(y,x, age=0):
	class Tree:
		def __init__(self, y,x,age):
			self.age = age
			self.isDead = False
			self.isFertilized = False
			self.x = x
			self.y = y

		def getPos(self):
			return (self.y, self.x)

		def isAlive(self):
			return not(self.isDead)

		def growOld(self):
			self.age += 1

		def getAge(self):
			return self.age

		def playDead(self):
			self.isDead = True

		def beFertilizer(self):
			self.isFertilized = True

		def isTreeFertilized(self):
			return self.isFertilized

	return Tree(y,x, age)

def solution(testIter,dataFertil, dataTreeInfo, dataMap, K, N ):
	"""

	dataMap : 땅, 양분 5로 초기화 N*N, (r,c)로 표기
	dataTreeInfo : 심은 나무의 정보 (x,y,z) : (x,y)위치의 z 나이의 나무를 심는다(맨처음)
	dataFertil : 겨울 로봇이 A[r][c] 만큼 양분 추가

	1) 봄
	나무 나이 모두 1씩 추가
	나무가 자신의 나이만큼 양분 흡수
	나이 증가
	여러 나무가 있다면, 나이가 어린 나무부터 양분 흡수 -> 없으면 죽음
	2) 여름
	죽은 나무가 양분으로 변함
	죽은 나무의 나이 //2 가 양분으로 그 위치에 추가
	3) 가을
	나무 번식 if 나무나이 % 5 == 0
	인접한 8칸에 나무 추가
	4)겨울
	각 칸에 A[r][c] 만큼 양분 추가

	K년 이후 살아있는 나무의 개수

	"""

	dataTree = { (idxRow, idxCol):set() for idxRow, valRow in enumerate(dataMap) \
					for idxCol, valCol in enumerate(valRow)
			}
	yprint(f'dataTree init : {dataTree}')
	diction = {}

	for info in dataTreeInfo:
		x, y, z = info
		dataTree[(y-1,x-1)].add(genTree(y-1,x-1,z))
	yprint(f'dataTree after : {dataTree}')

	for kk in range(K):
		yprint(f'')
		yprint(f'-'*20)
		yprint(f'kth gen : {kk}')

		for idxYear, year in enumerate(YEAR):
			if year == 'spring':
				for treeKey, treeVal in dataTree.items():
					_treeVal = sorted(list(treeVal), key=lambda x:x.age)
					for tree in _treeVal:
						yprint(f'>> tree in treeVal ::: {tree in treeVal}')
						if tree.isAlive():
							tmpTreeAge = tree.getAge()
							tmpTreePos = tree.getPos()

							mapFertil = dataMap[tmpTreePos[0]][tmpTreePos[1]]
							if mapFertil >= tmpTreeAge:
								yprint(f'spring - 1')
								dataMap[tmpTreePos[0]][tmpTreePos[1]] -= tmpTreeAge
								tree.growOld()
							else:
								yprint(f'spring - 2')
								tree.playDead()

			elif year == 'summer':
				for treeKey, treeVal in dataTree.items():
					tmpRemove = []
					for tree in treeVal:
						if not tree.isAlive() and not tree.isTreeFertilized():
							tmpTreePos = tree.getPos()
							dataMap[tmpTreePos[0]][tmpTreePos[1]] += (tree.getAge() // 2)
							tmpRemove.append(tree)

					for subTree in tmpRemove:
						treeVal.discard(subTree)


			elif year == 'fall':
				for treeKey, treeVal in dataTree.items():
					for tree in treeVal:
						if tree.getAge() % 5 == 0 and tree.isAlive():
							tmpTreePos = tree.getPos()
							cY, cX = tmpTreePos
							for ndir in range(8):
								nY = cY + dy[ndir]
								nX = cX + dx[ndir]

								if 0 <= nY <= N-1 and 0 <= nX <= N - 1:
									dataTree[(nY, nX)].add(genTree(nY,nX,1))

			elif year == 'winter':
				for idxRow, valRow in enumerate(dataFertil):
					for idxCol, valCol in enumerate(valRow):
						dataMap[idxRow][idxCol] +=valCol

			else:
				raise ValueError('Error!')
		yprint(f'---Pprint')
		pprint.pprint(dataMap)
		yprint(f'dataTree mid : {dataTree}')
		yprint(f'---Pprint')

	yprint(f'dataTree final : {dataTree}')
	yprint(f'dataMap final : {dataMap}')

	yprint(f'^'*13)
	counter = 0
	for key, val in dataTree.items():
		for tree in val:
			if tree.isAlive():
				counter += 1
	yprint(f'counter : {counter}')
	print(counter)


if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(8)