import sys
import copy

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)


def wrapper(i):
	for j in range(i):
		yprint('\n'*2)
		yprint(f'#'*30)
		N, M, xi, yi, K, dataMap, dataOrder, dice = init()
		solution(i, N, M, xi, yi, K, dataMap, dataOrder, dice)

class Dice:

	def __init__(self, posY, posX):
		self.faceNow = 1
		self.posX = posX
		self.posY = posY
		self.diceFlipMap = self.makeDiceFlipMap()
		self.diceFaceMap = self.makeDiceFaceMap()

	def makeDiceFaceMap(self):

		dataDict = {
			0 : 0,
			1 : 0,
			2 : 0,
			3 : 0,
			4 : 0,
			5 : 0
		}

		return dataDict

	def makeDiceFlipMap(self):

		direction = [
			(1, 5, 2, 0, 4, 3), # right
			(3, 0, 2, 5, 4, 1), # left
			(4, 1, 0, 3, 5, 2), # down
			(2, 1, 5, 3, 0, 4) # up
		]

		return direction

	def update(self, directionMap):

		tmpDict = copy.deepcopy(self.diceFaceMap)

		for idx, value in enumerate(directionMap):
			tmpDict[idx] = self.diceFaceMap[value]

		self.diceFaceMap = copy.deepcopy(tmpDict)

	def roll(self, direction, dataMap, yPos, xPos):

		dirInt= 0
		if direction == 3 : # up
			dirInt = 2
		elif direction == 4: # down
			dirInt = 3
		elif direction == 2 : # left
			dirInt = 1
		elif direction == 1 : # right
			dirInt = 0

		# update dice
		directionMap = self.diceFlipMap[dirInt]
		self.update(directionMap)

		if dataMap[yPos][xPos] == 0:
			dataMap[yPos][xPos] = self.diceFaceMap[5]
		else:
			self.diceFaceMap[5] = dataMap[yPos][xPos]
			dataMap[yPos][xPos] = 0

		# update x, y pos
		self.posX = xPos
		self.posY = yPos

	def getCurrPos(self):
		return self.posY, self.posX

	def getDiceFaceNum(self):
		#yprint(f'self.diceFaceMap : {self.diceFaceMap}')
		#yprint(f'self.faceNow : {self.faceNow}')
		return self.diceFaceMap[0]


def init():
	N, M, xi, yi, K = list(map(int, input().split(' ')))
	dataMap = [ [data for data in list(map(int, input().split(' ')))] for _ in range(N)]
	dataOrder = list(map(int, input().split(' ')))

	yprint(f'N, M, xi, yi, K : {N, M, xi, yi, K}')
	yprint(f'dataMap : {dataMap}')
	yprint(f'dataOrder : {dataOrder}')

	return N, M, xi, yi, K, dataMap, dataOrder, Dice(xi, yi)

def checkMoveable(dataMap, dice, direction):

	currPosY, currPosX = dice.getCurrPos()
	dx = [1, -1, 0, 0]
	dy = [0, 0, -1, 1]
	ind = 0
	if direction == 1: # right
		ind = 0
	elif direction == 2: # left
		ind = 1
	elif direction == 3: # up
		ind = 2
	elif direction == 4: # down
		ind = 3

	nextPosY, nextPosX = currPosY + dy[ind], currPosX + dx[ind]

	if not( 0 <= nextPosY <= len(dataMap)-1 and 0 <= nextPosX <= len(dataMap[0])-1 ):
		return False, nextPosY, nextPosX
	else: return True, nextPosY, nextPosX

def solution(testIndex, N, M, xi, yi, K, dataMap, dataOrder, dice):

	for order in dataOrder:
		isMoveable, nextPosY, nextPosX = checkMoveable(dataMap, dice, direction=order)
		if isMoveable:
			dice.roll(direction=order, dataMap=dataMap, yPos=nextPosY, xPos=nextPosX)
			yprint(f'current face : {dice.getDiceFaceNum()}')
			print(dice.getDiceFaceNum())


if __name__ == '__main__':
	sys.stdin = open("sample_input.txt", "r")
	wrapper(4)