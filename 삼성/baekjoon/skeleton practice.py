

def Wrapper(nums):

    for _ in range(nums):
        val1, val2 = init()
        returnValue = solution(val1, val2)

        print(returnValue)

def solution(val1, val2):
    return None

def init():

    tmpRead = input()

    val1, val2 = 0, 0
    return val1, val2

if __name__ == "__main__":

    import sys
    sys.stdin = open("open_sample.txt", 'r')

    T = 2
    Wrapper(T)