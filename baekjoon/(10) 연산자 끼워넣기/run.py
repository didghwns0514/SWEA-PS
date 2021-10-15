import sys
import itertools

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):
	print(11*10*9*8*7*6*5*4*3*2)
	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		N, dataNumber, dataOperation = init()
		solution(j,  N, dataNumber, dataOperation)


def init():
	N = int(input())
	dataNumber = list(map(int, input().split(' ')))
	dataOperation = list(map(int, input().split(' ')))

	yprint(f'N :{N}')
	yprint(f'dataNumber :{dataNumber}')
	yprint(f'dataOperation :{dataOperation}')
	opsIdx = ['+', '-', 'x', '/']
	filterDataOperation = []
	for idx, num in enumerate(dataOperation):
		filterDataOperation.extend([opsIdx[idx]]*num)
	yprint(f'filterDataOperation : {filterDataOperation}')

	return N, dataNumber, filterDataOperation

def solution(testIter,  N, dataNumber, dataOperation):

	dataPermu = list(itertools.permutations(dataOperation, r=len(dataOperation)))

	yprint(f'dataPermu : {dataPermu}')

	record = []
	for operation in dataPermu:
		yprint(f'operation : {operation}')
		answer = dataNumber[0]
		for idxNum, valueNum in enumerate(dataNumber):
			yprint(f'idxNum, valueNum : {idxNum, valueNum}')
			try:
				if idxNum == 0 : continue
				if operation[idxNum-1] == '+':
					answer = answer + valueNum
				elif operation[idxNum-1] == '-':
					answer = answer - valueNum
				elif operation[idxNum-1] == 'x':
					answer = answer * valueNum
				elif operation[idxNum-1] == '/':
					answer = -(abs(answer)//valueNum) if answer < 0 else answer//valueNum
			except:pass

		record.append(answer)

	print(max(record))
	print(min(record))

if __name__=="__main__":
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(3)