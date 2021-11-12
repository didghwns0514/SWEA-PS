
from collections import  deque
POS1 = 6
POS2 = 2
POS_12 = 0

def yprint(string, isEnabled=True):
	if isEnabled:
		print(string)


def wrapper(i):

	for j in range(i):
		yprint('\n'*2)
		yprint('#'*20)
		dataDisk, dataOrder = init()
		solution(i, dataDisk, dataOrder)


def init():
	dataDisk = [ deque(list(map(int, list(input())) )) for _ in range(4) ]
	tmpN = int(input())
	dataOrder = [ list(map(int, input().split(' '))) for _ in range(tmpN)]
	dataOrder = [ [data[0]-1, data[1]] for data in dataOrder]

	yprint(f'dataDisk : {dataDisk}')
	yprint(f'tmpN : {tmpN}')
	yprint(f'dataOrder : {dataOrder}')

	return dataDisk, dataOrder

def rotateDisks(dataDisk, rotation):

	for idxDisk, value in enumerate(rotation):
		if value == 2:
			continue

		# if value == 1: # 시계방향
		# 	dataDisk[idxDisk].appendleft(dataDisk[idxDisk].popleft())
		# else:
		# 	dataDisk[idxDisk].append(dataDisk[idxDisk].pop())

		if value == 1: # 시계방향
			dataDisk[idxDisk].rotate(1)
		else:
			dataDisk[idxDisk].rotate(-1)

def calculateScore(dataDisk):

	score = 0
	for idx in range(4):
		if dataDisk[idx][POS_12] == 1:
			if idx == 0:
				score += 1
			elif idx == 1:
				score += 2
			elif idx == 2:
				score += 4
			elif idx == 3:
				score += 8

	return score


def solution(testIteration, dataDisk, dataOrder):

	for order in dataOrder:

		rotation = [0]*4
		rotation[order[0]] = order[1]
		subSolution(dataDisk, order, rotation, 1 )
		yprint(f'rotation - result : {rotation}')
		rotateDisks(dataDisk, rotation)
		yprint(f'dataDisk - middle ; {dataDisk}')

	yprint(f'dataDisk - final ; {dataDisk}')
	answer = calculateScore(dataDisk)
	yprint(f'answer : {answer}')
	print(answer)

def subSolution(dataDisk, order, rotation, counter):
	# rotation 1: 시계 -1 : 반시계 2: 멈춤, 0 : nor decided

	if counter == 4:
		pass
		return
	yprint(f'*'*13)
	yprint(f'counter - before ; {counter}')
	yprint(f'rotation - before: {rotation}')
	for idxDisk, value in enumerate(rotation):
		if value != 0: pass
		else:
			if idxDisk == 0:
				if rotation[1] != 0:
					if rotation[1] == 2:
						rotation[0] = 2
						counter += 1
					else:
						tmpRot = -rotation[1] if dataDisk[0][POS2] != dataDisk[1][POS1] else 2
						rotation[0] = tmpRot
						counter += 1
			if idxDisk == 1:
				if rotation[0] != 0:
					if rotation[0] == 2:
						rotation[1] = 2
						counter += 1
					else:
						tmpRot = -rotation[0] if dataDisk[0][POS2] != dataDisk[1][POS1] else 2
						rotation[1] = tmpRot
						counter += 1
				elif rotation[2] != 0:
					if rotation[2] == 2:
						rotation[1] = 2
						counter += 1
					else:
						tmpRot = -rotation[2] if dataDisk[1][POS2] != dataDisk[2][POS1] else 2
						rotation[1] = tmpRot
						counter += 1
			if idxDisk == 2:
				if rotation[1] != 0:
					if rotation[1] == 2:
						yprint('2-1')
						rotation[2] = 2
						counter += 1
					else:
						yprint('2-2')
						yprint(f'dataDisk[1][POS2] : {dataDisk[1][POS2]}')
						yprint(f'dataDisk[2][POS1] : {dataDisk[2][POS1]}')
						tmpRot = -rotation[1] if dataDisk[1][POS2] != dataDisk[2][POS1] else 2
						rotation[2] = tmpRot
						counter += 1
				elif rotation[3] != 0:
					yprint('2-3')
					if rotation[3] == 2:
						rotation[2] = 2
						counter += 1
					else:
						yprint('2-4')
						tmpRot = -rotation[3] if dataDisk[2][POS2] != dataDisk[3][POS1] else 2
						rotation[2] = tmpRot
						counter += 1
			if idxDisk == 3:
				if rotation[2] != 0:
					if rotation[2] == 2:
						rotation[3] = 2
						counter += 1
					else:
						tmpRot = -rotation[2] if dataDisk[2][POS2] != dataDisk[3][POS1] else 2
						rotation[3] = tmpRot
						counter += 1

	yprint(f'counter - after ; {counter}')
	yprint(f'rotation - after: {rotation}')
	subSolution(dataDisk, order, rotation, counter)
	return



if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(4)