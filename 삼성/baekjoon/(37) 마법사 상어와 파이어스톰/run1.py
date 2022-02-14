

def Wrapper(T):

    for _ in range(T):
        N, dataMap, Q, dataL = init()
        returnResult = solution(N, dataMap, Q, dataL)
        print(f'returnResult : {returnResult}')


def init():
    N, Q = list(map(int, input().split(' ')))  # N**2 만큼 / Q 번 수행

    # 데이터 생성
    dataMap = []
    for _ in range(2**N):
        tmpInput = list(map(int, input().split(' ')))
        dataMap.append(tmpInput)

    dataL = list(map(int, input().split(' ')))

    print(f'len(dataMap) : {len(dataMap)}')
    print(f'dataMap, Q, dataL : {dataMap, Q, dataL}')

    return N, dataMap, Q, dataL


def solution(N, dataMap, Q, dataL):
    pass


def splitForLsize(N, L):

    tmpLlength = 2**L
    tmpNLength = 2**N




if __name__ == "__main__":
    import sys
    sys.stdin = open('sample_input.txt', 'r')


    T = 6
    Wrapper(6)