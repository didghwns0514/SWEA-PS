

def tWrapper():
	pass

def wrapper(i):

	for j in range(i):
		dataDice, mapData = init()
		returnValue = solution(j, dataDice, mapData)

def makePoint(score, red=None, blue=None):
	return {'score':score, 'red':red, 'blue':blue}

def init():

	mapData = {
		'start' : makePoint(0, '2-1'),
		'2-1' : makePoint(2, '4-1'),
		'4-1' : makePoint(4, '6-1'),
		'6-1' : makePoint(6, '8-1'),
		'8-1' : makePoint(8, '10'),
		'10': makePoint(10, '12-2', '13-3'),
		'12-2': makePoint(12, '14-2'),
		'14-2': makePoint(14, '16-2'),
		'16-2': makePoint(16, '18-2'),
		'18-2': makePoint(18, '20'),
		'13-3': makePoint(13, '16-3'),
		'16-3': makePoint(16, '19-3'),
		'19-3': makePoint(19, '25'),
		'20': makePoint(20,  '22-6', '22-4'),
		'22-4': makePoint(22, '24-4'),
		'24-4': makePoint(24, '25'),
		'25' : makePoint(25, '30-5'),
		'30-5': makePoint(30, '35-5'),
		'35-5': makePoint(35, '40'),
		'22-6': makePoint(22, '24-6'),
		'24-6': makePoint(24, '26-6'),
		'26-6': makePoint(26, '28-6'),
		'28-6': makePoint(28, '30'),
		'30' : makePoint(30, '32-8', '28-7'),
		'28-7': makePoint(28, '27-7'),
		'27-7': makePoint(27, '26-7'),
		'26-7': makePoint(26, '25'),
		'32-8': makePoint(32, '34-8'),
		'34-8': makePoint(34, '36-8'),
		'36-8': makePoint(36, '38-8'),
		'38-8': makePoint(38, '40'),
		'40' : makePoint(40, 'end')

	}

	dataDice = list(map(int, input().split()))

	return dataDice, mapData

def solution(testIter, dataDice, mapData):




if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')

	import itertools

	# T = int(input())
	T = 4
	wrapper(T)