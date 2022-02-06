
def Wrapper(T):
    for _ in range(T):
        data = init()
        returnValue = solution(data)


def init():
    pass

def solution(data):
    pass


if __name__ == "__main__":

    import sys
    sys.stdin = open('sample_input.txt', 'r')

    T = 4
    Wrapper(T)