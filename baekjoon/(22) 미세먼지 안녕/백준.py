import sys, copy
from collections import deque

input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

m, n, t = map(int, input().split())
q = deque()

a = []
for i in range(m):
	row = list(map(int, input().split()))
	a.append(row)
	for j in range(n):
		if a[i][j] > 0:
			q.append([i, j])
		if a[i][j] == -1:
			sx = i

for _ in range(t):
	temp1 = copy.deepcopy(a)
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < m and 0 <= ny < n:
				if a[nx][ny] >= 0:
					temp1[nx][ny] += a[x][y] // 5
					temp1[x][y] -= a[x][y] // 5

	temp2 = copy.deepcopy(temp1)
	x, y, flag, turn = sx - 1, 1, 1, 1
	while True:
		if turn == 1:
			temp2[x][y+1] = temp1[x][y]
			y += 1
			if y + 1 == n:
				turn = 2
		elif turn == 2:
			if flag == 1:
				temp2[x-1][y] = temp1[x][y]
				x -= 1
				if x - 1 == -1:
					turn = 3
			if flag == 2:
				temp2[x+1][y] = temp1[x][y]
				x += 1
				if x + 1 == m:
					turn = 3
		elif turn == 3:
			temp2[x][y-1] = temp1[x][y]
			y -= 1
			if y - 1 == -1:
				turn = 4
		elif turn == 4:
			if flag == 1:
				if x + 1 == sx - 1:
					x, y, flag, turn = sx, 1, 2, 1
					continue
				temp2[x+1][y] = temp1[x][y]
				x += 1
			if flag == 2:
				if x - 1 == sx:
					break
				temp2[x-1][y] = temp1[x][y]
				x -= 1

	temp2[sx-1][1], temp2[sx][1] = 0, 0
	a = temp2

	for i in range(m):
		for j in range(n):
			if a[i][j] > 0:
				q.append([i, j])

ans = 0
for i in a:
	ans += sum(i)
print(ans+2)