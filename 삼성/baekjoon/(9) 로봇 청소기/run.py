
import sys
import pprint
import copy

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):

	for j in range(i):
		yprint('\n' * 2)
		yprint(f'#' * 30)
		dataMap, robot = init()
		solution(j, dataMap, robot)

class Robot:

	def __init__(self, posY, posX, d):
		self.posY = posY
		self.posX = posX
		self.direction = d
		self.sweeeped = set()
		self.isFinished = False

	def activate(self, dataMap):
		self.sweeeped.add( (self.posY, self.posX) )
		self.move(dataMap, 1)

	def getNextDirection(self):
		# 0 : up, 1 : right, 2 : down, 3 : left

		targetDir = self.direction
		targetDir -= 1
		if targetDir == -1 :
			targetDir = 3

		return targetDir

	def rotateNextDirection(self):
		# 0 : up, 1 : right, 2 : down, 3 : left

		targetDir = self.direction
		targetDir -= 1
		if targetDir == -1 :
			targetDir = 3

		self.direction = targetDir

		return self.direction

	def getReverseDirection(self):

		if self.direction == 0:
			return 2
		elif self.direction == 1:
			return 3
		elif self.direction == 2:
			return 0
		elif self.direction == 3:
			return 1

	def move(self, dataMap, cnt):

		yprint(f'cnt :{cnt}')
		dx = [0, 1, 0, -1]
		dy = [-1, 0, 1, 0]
		drection = self.getNextDirection()

		nextY = self.posY + dy[drection]
		nextX = self.posX + dx[drection]
		maxY = len(dataMap)
		maxX = len(dataMap[0])
		nextPos = (nextY, nextX)

		# a
		if nextPos not in self.sweeeped and (0 <= nextY <= maxY-1 and 0 <= nextX <= maxX-1) \
				and dataMap[nextY][nextX] != 1: # not wall
			self.rotateNextDirection()
			self.posY = nextY
			self.posX = nextX
			return

		# b
		else:
			if cnt <= 4 :
				self.rotateNextDirection()
				return self.move(dataMap, cnt+1)
			else:
				yprint(f'direction now! - {self.posY, self.posX}')
				yprint(f'direction now2! - {self.direction}')
				reverseDirection = self.getReverseDirection()
				yprint(f'reverseDirection : {reverseDirection}')
				revY = self.posY + dy[reverseDirection]
				revX = self.posX + dx[reverseDirection]
				if dataMap[revY][revX] != 1 and (0 <= revY <= maxY-1 and 0 <= revX <= maxX-1):
					self.posY = revY
					self.posX = revX
					return
				else:
					self.isFinished = True
					return

	def checkFinished(self):
		return self.isFinished

def init():
	N, M = list(map(int, input().split(' ')))
	r, c, d = list(map(int, input().split(' ')))
	dataMap = [ list(map(int, input().split(' '))) for _ in range(N) ]
	yprint(f'N, M : {N, M}')
	yprint(f'r, c, d  : {r, c, d}')
	#pprint.pprint(dataMap)

	return dataMap, Robot(r, c, d)

def solution(testIndex, dataMap, robot):

	while not robot.checkFinished():
		yprint(f'')
		yprint(f'-' * 20)
		yprint(f'robot pos before :{robot.posY, robot.posX}')
		yprint(f'robot sweep before : {robot.sweeeped}')
		yprint(f'robot direction before : {robot.direction}')
		robot.activate(dataMap)
		tmpDataMap = copy.deepcopy(dataMap)
		for poss in robot.sweeeped:
			tmpDataMap[poss[0]][poss[1]] = 'S'
			tmpDataMap[robot.posY][robot.posX] = 'N'
		#pprint.pprint(tmpDataMap)
		yprint(f'robot pos after :{robot.posY, robot.posX}')
		yprint(f'robot sweep after : {robot.sweeeped}')
		yprint(f'robot direction after : {robot.direction}')

	yprint(f'len(set(robot.sweeeped)) : {len(set(robot.sweeeped))}')
	yprint(f'len(robot.sweeeped) : {len(robot.sweeeped)}')
	print(len(robot.sweeeped))

if __name__=='__main__':
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(2)