from collections import deque
import copy

def Wrapper(it):

    for _ in range(it):
        q, K, N = init()
        returnValue = solution(q, K, N)
        print(f'returnValue : {returnValue}')

def init():

    N, K = list(map(int, input().split(' ')))

    q = deque() # deque 쓸 예정

    tmpInput = list(map(int, input().split(' ')))
    for k in range(len(tmpInput)):
        q.append({
            '내구도' : tmpInput[k],
            '로봇' : None
        })

    return q, K, N


def solution(q, K, N):

    robotHist = []
    robotCnt = 0
    stepCount = 0

    while not(len([ data for data in q if data['내구도'] <= 0 ]) >= K):

        # step
        stepCount += 1

        # 밸트가 한칸 회전
        q.rotate(1)

        # 로봇 내리기
        if q[N-1]['로봇'] != None:
            tmpRobotNum = q[N - 1]['로봇']
            q[N - 1]['로봇'] = None
            if tmpRobotNum in robotHist:
                robotHist.remove(tmpRobotNum)
            q[N - 1]['내구도'] -= 1


        # 로봇 이동
        if robotHist: # 있으면
            for robot in robotHist: # 로봇 순서대로 작업
                tmpReturnValue = findRobotIdx(q, robot)
                if tmpReturnValue == None: # not found
                    continue
                else: # found
                    nextRobotIdx = tmpReturnValue + 1 if tmpReturnValue < len(q) - 1 else 0
                    if q[nextRobotIdx]['내구도'] >= 1 and q[nextRobotIdx]['로봇'] == None:
                        q[nextRobotIdx]['로봇'] = copy.deepcopy(q[tmpReturnValue]['로봇'])
                        q[nextRobotIdx]['내구도'] -= 1
                        q[tmpReturnValue]['로봇'] = None
                        continue
                    else:continue

        # 로봇 내리기
        if q[N-1]['로봇'] != None:
            tmpRobotNum = q[N - 1]['로봇']
            q[N - 1]['로봇'] = None
            if tmpRobotNum in robotHist:
                robotHist.remove(tmpRobotNum)
            q[N - 1]['내구도'] -= 1

        # 로봇 올리기
        if q[0]['로봇'] == None and q[0]['내구도'] != 0:
            q[0]['로봇'] = robotCnt
            robotHist.append(robotCnt)
            robotCnt += 1
            q[0]['내구도'] -= 1


    return stepCount

def findRobotIdx(q, robotIdx):
    for k in range(len(q)):
        if q[k]['로봇'] == robotIdx:
            return k
    else:
        return None

if __name__ == '__main__':

    import sys
    sys.stdin = open('sample_input.txt','r')


    T = 4
    Wrapper(T)