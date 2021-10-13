# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import sys
from collections import deque
import pprint

sys.stdin = open("sample_input.txt", "r")
answer = 0

def wrapper(i):
	global answer

	for k in range(i):
		T = int(input())
		dataMap = [ [ data for data in list(map(int, input().split(' '))) ] for  _ in range(T) ]
		count, answer, q = 0, 0, deque()
		print(f'dataMap : {dataMap}')
		print(f'k th iteration : {k+1} out of total {i}')
		solution(dataMap, count, q, T)

		print(f'final answer : {answer}')

def get(dataMap, q, i, j):
	if dataMap[i][j]: # 0이 아닌 값이라면
		q.append(dataMap[i][j]) # queue에 board의 값을 넣는다. -> FIFO
		dataMap[i][j] = 0 # 처리가 된 빈 자리는 0으로 값 업데이트

def merge(dataMap, q, i, j, di, dj): # row index, column index, y방향, x방향
	print(f'q : {q}')
	while q:
		x = q.popleft() # 움직이려는 블록 값을 가져온다. FIFO
		if not dataMap[i][j]: # 0이라면 그대로 놓는다.
			dataMap[i][j] = x
		elif dataMap[i][j] == x: # 값이 일치한다면
			dataMap[i][j] = x*2 # 합쳐지므로 2배로 증가
			i, j = i+di, j+dj
		else: # 값이 일치하지 않으면 or 0 이라면
			i, j = i+di, j+dj
			dataMap[i][j] = x

def move(dataMap, q, T, k):
	# board[i][j]
	print(f'move direction : {k}')
	if k == 0: # 위로 이동, 블락들이 위로 모두 이동하면 row index는 0
		for j in range(T): # col
			for i in range(T): # row
				get(dataMap, q, i, j)
			merge(dataMap, q, 0, j, 1, 0) # row index 1씩 증가하면서 아래쪽 블락들을 합쳐감
	elif k == 1: # 아래로 이동, 블락들이 아래로 모두 이동하면 row index는 n-1
		for j in range(T):
			for i in range(T-1, -1, -1):
				get(dataMap,q, i, j)
			merge(dataMap, q, T-1, j, -1, 0) # row 인덱스 1씩 감소하면서 위쪽들을 합쳐감
	elif k == 2: # 오른쪽으로 이동, column index는 0
		for i in range(T):
			for j in range(T):
				get(dataMap, q, i, j)
			merge(dataMap, q, i, 0, 0, 1) # column 인덱스 증가 오른쪽으로 이동
	else: # 왼쪽으로 이동, column index는 n-1
		for i in range(T):
			for j in range(T-1, -1, -1):
				get(dataMap, q, i, j)
			merge(dataMap, q, i, T-1, 0, -1) # column 인덱스 감소 왼쪽으로 이동


def solution(dataMap, count, q, T):
	global answer
	print('#'*30)
	if count == 5: # 최대 5번까지 움직였다면
		for i in range(T):
			answer = max(answer, max(dataMap[i])) # 가장 큰 값이 answer
		print(f'answer : {answer}')
		return

	print(f'count : {count}')
	print(f'dataMap before :')
	pprint.pprint(dataMap)

	b = [x[:] for x in dataMap] # 방향을 바꾸기 전에 원래의 보드를 기억해야 한다.
	for k in range(4): # 4방향으로 움직인다.
		print('-'*20)
		print(f'dataMap before - solution:')
		pprint.pprint(dataMap)
		move(dataMap, q, T, k) # 움직인다.
		solution(dataMap, count+1, q, T) # 재귀적으로 호출 -> DFS 처럼 동작, 한쪽 먼저 팜
		print(f'dataMap after - solution:')
		pprint.pprint(dataMap)
		dataMap = [x[:] for x in b]


	print(f'dataMap after :')
	pprint.pprint(dataMap)
	print('#'*30)
	print(f'')


if __name__ == '__main__':
	wrapper(1)