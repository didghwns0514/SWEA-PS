import sys
import itertools

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)


def wrapper(i):

	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		N, dataCounsel = init()
		solution(i, N, dataCounsel)


def init():
	N = int(input())
	dataCounsel = [ list(map(int, input().split(' '))) for  _ in range(N)]
	dataCounsel = [ [ data[0], data[1], idx ] for idx, data in enumerate(dataCounsel) ]

	yprint(f'N : {N}')
	yprint(f'dataCounsel : {dataCounsel}')

	return N, dataCounsel


def solution(testIndex, N, dataCounsel):

	answer = 0

	for pickNum in range(1, N + 1):
		yprint(f'\n')
		yprint(f'-'*20)
		yprint(f'pickNum : {pickNum}')
		pickedDays = list(itertools.combinations(dataCounsel, pickNum))
		#pickedDays = list(map(lambda x : x[0], pickedDays))
		yprint(f'pickedDays : {pickedDays}')

		for selecedDay in pickedDays:
			filteredDays = list(filter(lambda x: N - x[2] >= x[0],  selecedDay ))
			yprint(f'filteredDays : {filteredDays}')

			for tIdx, task in enumerate(filteredDays):
				try:
					if task[0] + task[2] - 1 >= filteredDays[tIdx + 1][2]:
						break
				except:
					tmpSum = sum(map(lambda x : x[1], filteredDays))
					yprint(f'tmpSum1 : {tmpSum}')
					answer = max(answer, tmpSum)
			else:
				tmpSum = sum(map(lambda x : x[1], filteredDays))
				yprint(f'tmpSum2 : {tmpSum}')
				answer = max(answer, tmpSum)


	yprint(f'answer : {answer}')
	print(answer)

if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	wrapper(4)