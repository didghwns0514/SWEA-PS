
VERTICAL = {
	'1-up':0,
	'2-up':1,
	'3-up':2,
	'1-down':3,
	'2-down':4,
	'3-down':5
}
HORIZONTAL = {
	'1-right':6,
	'2-right':7,
	'3-right':8,
	'1-left':9,
	'2-left':10,
	'3-left':11
}

NEXT = [
	[
		[],
		[],
		[],
		[],
		[],
		[]
	],


]

def yprint(string, isEnabled=True):
	if isEnabled:
		print(string)


def wrapper(i):

	for j in range(i):
		init()
		solution(j)


def init():
	pass


def solution(testIter):
	pass


if __name__ == '__main__':
	import sys
	sys.stdin = open('sample_input.txt', 'r')

	wrapper(1)