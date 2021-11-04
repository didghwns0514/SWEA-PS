
def twrapper():
	pass

def wrapper(i):

	for j in range(i):
		init()
		returnValue = solution(j)

def init():
	pass

def solution(testIter):
	pass

if __name__ == "__main__":

	import sys
	sys.stdin = open('sample_input.txt', 'r')

	# T = int(input())
	T = 7
	wrapper(T)
