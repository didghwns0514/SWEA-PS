
def Wrapper(T):
    for _ in range(T):
        N, K, dataFireball = init()
        returnValue = solution(N, K, dataFireball)


def init():
    N, M, K = list(map(int, input().split(' ')))

    dataFireball = {}
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
            for fireball in loc_value:
                if fireball[3] == False:




        """ 마지막, 이동상태 모두 false로 전환"""



if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 4
    Wrapper(T)