
def twrapper():
	pass

def wrapper(i):

	for j in range(i):
		dataMap = init()
		returnValue = solution(j, dataMap)


def init():

	dataMap = [ list(map(int, input().split())) for _ in range(4) ]

	return dataMap

def solution(testIter, dataMap):
	pass




if __name__ == "__main__":

	import sys
	sys.stdin = open('sample_input.txt', 'r')

	# T = int(input())
	T = 4
	wrapper(T)
