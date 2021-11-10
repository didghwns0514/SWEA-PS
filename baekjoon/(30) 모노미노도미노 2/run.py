
def twrapper():
	pass

def wrapper(i):

	for j in range(i):
		N, dataPlace = init()
		returnValue = solution(j, N, dataPlace)

def init():
	N = int(input())
	dataPlace = [ list(map(int, input().split())) for _ in range(N)]

	return N, dataPlace

def solution(testIter, N, dataPlace):
	pass

if __name__ == "__main__":

	import sys
	sys.stdin = open('sample_input.txt', 'r')

	# T = int(input())
	T = 7
	wrapper(T)
