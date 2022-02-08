

import copy


def Wrapper(T):
    for _ in range(T):
        N, K, dataFireball = init()
        returnValue = solution(N, K, dataFireball)

        print(f'returnValue  : {returnValue}')

def init():
    N, M, K = list(map(int, input().split(' ')))

    dataFireball = {}
    for n1 in range(N):
        for n2 in range(N):
            dataFireball[(n1, n2)] = []

    for _ in range(M):
        r, c, m, s, d = list(map(int, input().split(' ')))
        r, c = r -1, c -1

        if (r, c) not in dataFireball: # 행, 열 -> y, x
            dataFireball[(r, c)] = []
        dataFireball[(r, c)].append([m, d, s, False])  # 질량, 방향, 속도, move되었음


    return N, K, dataFireball # 정사각격자 크기, 수행 횟수, 데이터

def solution(N, K, dataFireball):

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    for _ in range(K):

        """1. 모든 파이어볼이 자신의 방향 d로 속력 s만큼 이동"""
        """ 방향
            0 위, 1, 2 오른, 3, 4 아래, 5, 6 왼쪽, 7
        """
        for loc_key, loc_value in dataFireball.items():
            index_keep_record = []

            for fire_index, fireball in enumerate(loc_value):
                if fireball[3] == False:
                    returnValue = getNextPos(currPos=loc_key, speed=fireball[2], direction=fireball[1], dx=dx, dy=dy, N=N)

                    # 파이어볼 이동
                    if returnValue not in dataFireball:
                        dataFireball[returnValue] = []
                    dataFireball[returnValue].append([fireball[0], fireball[1], fireball[2], True])

                else: index_keep_record.append(fire_index)

            # 기록
            tmpKeptRecord = []
            for _idx in index_keep_record:
                tmpKeptRecord.append(loc_value[_idx])
            dataFireball[loc_key] = copy.deepcopy(tmpKeptRecord)


        """2. 이동이 끝난 후 2개이상의 파이어볼이 있음"""
        tmpRecordDict = {}
        for loc_key, loc_value in dataFireball.items():
            if len(loc_value) >= 2: # loc_value -> # 질량, 방향, 속도, move되었음
                tot_mass = sum( [ data[0] for data in loc_value ] )
                tot_speed = sum( [ data[2] for data in loc_value ] )

                if tot_mass / 5 < 1: # 0 밑으로 소멸
                    dataFireball[loc_key] = copy.deepcopy([])
                else:
                    decided_direction = [0, 2, 4, 6] if (all([ data[1] % 2 ==0 for data in loc_value ]) or all([data[1] % 2 ==1 for data in loc_value]) ) else [1, 3, 5, 7]

                    for _dir in decided_direction:
                        if loc_key not in tmpRecordDict:
                            tmpRecordDict[loc_key] = []
                        tmpRecordDict[loc_key].append([ int(tot_mass//5), _dir, int(tot_speed//len(loc_value)), False ])

                dataFireball[loc_key] = copy.deepcopy([])

        for key, value in tmpRecordDict.items():
            if key not in dataFireball:
                dataFireball[key] = []

            dataFireball[key].extend(value)


        """ 마지막, 이동상태 모두 false로 전환"""
        for key, value in dataFireball.items():
            for _idx, fireball in enumerate(value):
                value[_idx][3] = False

    """질량 합산"""
    _total = 0
    for key, value in dataFireball.items():
        for _idx, fireball in enumerate(value):
            _total += fireball[0]

    return _total

def getNextPos(currPos, speed, direction, dx, dy, N):
    cy, cx = currPos
    for _ in range(speed):
        cy += dy[direction]
        cx += dx[direction]

        cy = N-1 if cy < 0 else ( 0 if cy > N - 1 else cy )
        cx = N-1 if cx < 0 else ( 0 if cx > N - 1 else cx )


    return (cy, cx)

if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 4
    Wrapper(T)