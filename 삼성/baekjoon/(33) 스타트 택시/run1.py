

def wrapper(T):

    for _ in range(T):
        N, Fule, dataMap, StartPos, dataCustomer = init()
        returnValue = solution(N, Fule, dataMap, StartPos, dataCustomer)


def init():
    # init
    N, M, Fule = list(map(int, input().split(' ')))

    # Map
    dataMap = []
    for _ in range(N):
        tmplist = list(map(int, input().split(' ')))
        dataMap.append(tmplist)

    # startpos
    x, y = list(map(int, input().split(' ')))
    StartPos = (x-1, y-1)

    # customer
    dataCustomer = {}
    for _ in range(M):
        v1, v2, v3, v4 = list(map(int, input().split(' ')))
        dataCustomer[(v1-1, v2-1)] = (v3-1, v4-1)

    return N, Fule, dataMap, StartPos, dataCustomer


def solution(N, Fule, dataMap, StartPos, dataCustomer):
    pass

if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 3
    wrapper(T)