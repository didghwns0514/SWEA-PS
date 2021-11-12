

import sys

def yprint(string, isEnabled=False):
	if isEnabled:
		print(string)

def wrapper(i):
	for j in range(i):
		yprint(f'\n'*2)
		yprint(f'#'*30)
		N, testRoom, nB, nC = init()
		solution(j, N, testRoom, nB, nC)



def init():
	N = int(input())
	testRoom = list(map(int, input().split(' ')))
	nB, nC = list(map(int, input().split(' ')))

	yprint(f'N : {N}')
	yprint(f'testRoom : {testRoom}')
	yprint(f'nB, nC : {nB}, {nC}')

	return N, testRoom, nB, nC

def getMinSups(peopleNumber, nB, nC):

	nBMax = (peopleNumber // nB) + 1
	nCMax = (peopleNumber // nC) + 1
	yprint(f'nBMax : {nBMax}, nCMax : {nCMax}')
	record = []

	for i_nB in range(1, 1 + 1):
		for i_nC in range(nCMax + 1):

			#yprint(f'i_nC : {i_nC}, i_nB : {i_nB}')
			#yprint(f'(i_nB * nB) + (i_nC * nC) : {(i_nB * nB) + (i_nC * nC)}')
			if ((i_nB * nB) + (i_nC * nC) ) >= peopleNumber :
				record.append([i_nB, i_nC])
				break

	yprint(f'record : {record}')

	return sum(min(record, key=lambda x : sum(x)))

def solution(testIndex, N, testRoom, nB, nC):

	nSupMain = 0
	nSupSub = 0

	# 총감독관
	#nSupMain += len(testRoom)
	#testRoom = [0 if data - nB < 0 else data - nB for data in testRoom]
	yprint(f'testRoom : {testRoom}')

	# iter
	cnt = 0
	for number in testRoom:
		cnt += getMinSups(peopleNumber=number, nB=nB, nC=nC)

	yprint(f'cnt + nSupMain : {cnt + nSupMain}')
	print(cnt)

if __name__ == '__main__':
	sys.stdin = open("sample_input.txt", "r")
	wrapper(5)