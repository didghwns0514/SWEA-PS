import copy

def twrapper():
	pass

def wrapper(i):

	for j in range(i):
		fishData = init()
		returnValue = solution(j, fishData)
		print(f'returnValue : {returnValue}')

def init():

	fishData = {}
	for j in range(4):
		fish_input = list(map(int, input().split(' ')))
		#print(f'fish_input: {fish_input}')
		for i in range(4):
			fishData[fish_input[2*i]] = {
				'direction' : fish_input[2*i + 1],
				'location' : (j, i), # 행, 열,
				'type' : 'fish'
			}
	#print(f'fishData : {fishData}')
	return fishData

topAnswer = 0

def solution(testIter, fishData):
	global topAnswer
	topAnswer= 0

	sharkAteFish = 0
	fishGame((0,0), fishData, sharkAteFish)

	return topAnswer



def fishGame(movePose, fishData, sharkAteFish):
	global topAnswer

	dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 헹
	dy = [0, -1, -1, -1, 0, 1, 1, 1] # 열

	# 청소년 상어 투입
	foundFish = None
	for fishKey, fishVal in fishData.items():
		if fishKey == 0: continue
		if fishVal['location'] == movePose:
			sharkAteFish += fishKey
			foundFish = fishKey
			fishData[0] = {
				'direction' : fishVal['direction'],
				'location' : fishVal['location'],
				'type' : 'shrak'
			}
			break
	fishData.pop(foundFish)

	# 물고기 회전
	for idx, fishKey in enumerate(sorted(list(fishData.keys()))):
		if fishKey == 0: continue # shark

		currFishDir = fishData[fishKey]['direction']
		X, Y = fishData[fishKey]['location']


		for q in range(9):
			nextX, nextY = dx[currFishDir - 1], dy[currFishDir - 1]

			if not ((0 <= X + nextX < 4) or (0 <= Y + nextY < 4)):
				currFishDir = FishRoatate(currentDir=currFishDir)
				fishData[fishKey]['direction'] = currFishDir
			elif fishData[0]['location'] == (X + nextX, Y + nextY):
				currFishDir = FishRoatate(currentDir=currFishDir)
				fishData[fishKey]['direction'] = currFishDir

			else: # moveable
				# fish exists
				foundFish = None
				for fishKey2 in sorted(list(fishData.keys())):
					if fishKey2 in [0, fishKey]: continue
					else:
						if fishData[fishKey2]['location'][0] == X + nextX and  \
						   fishData[fishKey2]['location'][1] ==	Y + nextY:
							foundFish = fishKey2
							break
						else: continue
				if foundFish:
					loc1 = fishData[fishKey]['location']
					fishData[fishKey]['location'] = fishData[foundFish]['location']
					fishData[foundFish]['location'] = loc1
				else:
					fishData[fishKey]['location'] = (X + nextX, Y + nextY)
				break

	# 상어 움직이기
	dirShark = fishData[0]['direction']
	locSharkX, locSharkY = fishData[0]['location']
	moveableLoc = []
	for _ in range(4):
		nextX, nextY = dx[dirShark - 1], dy[dirShark - 1]
		if not ((0 <= locSharkX + nextX < 4) or (0 <= locSharkY + nextY < 4)):
			continue

		tmploc = (locSharkX + dx[dirShark-1], locSharkY + dy[dirShark-1])
		for fishKey, fishVal in fishData.items():
			if fishVal['location'] == tmploc:
				moveableLoc.append(tmploc)
				locSharkX, locSharkY = locSharkX + nextX, locSharkY + nextY
				break

	if not moveableLoc:
		topAnswer = max(topAnswer, sharkAteFish)
		return
	else:
		tmpFishData = copy.deepcopy(fishData)
		for k in range(len(moveableLoc)):
			fishGame(moveableLoc[k], tmpFishData, sharkAteFish)


def FishRoatate(currentDir):
	if currentDir >= 8 :
		return 0
	else:
		return currentDir + 1


if __name__ == "__main__":

	import sys
	sys.stdin = open('sample_input.txt', 'r')

	# T = int(input())
	T = 4
	wrapper(T)
