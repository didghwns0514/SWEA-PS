import copy
from collections import deque
import sys
GLOBAL_RECURSION = 300000
sys.setrecursionlimit(GLOBAL_RECURSION)

CONST_MAX = 987654321
MIN_VALUE = 987654321

def solution(queue1, queue2):

    global CONST_MAX, MIN_VALUE

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    try:
        subSolution(queue1, queue2, 0)
    except:
        return -1
    if MIN_VALUE == CONST_MAX:
        return -1

    else:
        return MIN_VALUE


def subSolution(q1, q2, counter):
    global CONST_MAX, MIN_VALUE, GLOBAL_RECURSION

    if counter > MIN_VALUE:
        return None

    if counter > GLOBAL_RECURSION:
        return None

    s1 = sum(q1)
    s2 = sum(q2)
    if s1 == s2:
        MIN_VALUE = min(MIN_VALUE, counter)
        return None

    # for i in range(2):
    #     if i == 0:
    #         if not q1: continue
    #         qq1 = copy.deepcopy(q1)
    #         qq2 = copy.deepcopy(q2)
    #         qq2.append(qq1.popleft())
    #         subSolution(qq1, qq2, counter+1)
    #
    #     elif i == 1:
    #         if not q2: continue
    #         qq1 = copy.deepcopy(q1)
    #         qq2 = copy.deepcopy(q2)
    #         qq1.append(qq2.popleft())
    #         subSolution(qq1, qq2, counter + 1)

    if s1 > s2:
        #if not q1: continue
        qq1 = copy.deepcopy(q1)
        qq2 = copy.deepcopy(q2)
        qq2.append(qq1.popleft())
        subSolution(qq1, qq2, counter+1)
    else:
        #if not q2: continue
        qq1 = copy.deepcopy(q1)
        qq2 = copy.deepcopy(q2)
        qq1.append(qq2.popleft())
        subSolution(qq1, qq2, counter + 1)


if __name__ == "__main__":

    switch = 3

    if switch == 1:
        q1 = [3, 2, 7, 2]
        q2 = [4, 6, 5, 1]
        answer = solution(q1, q2)
        print(f'found answer : {answer}')
        assert(answer == 2)

    elif switch == 2:
        q1 = [1, 2, 1, 2]
        q2 = [1, 10, 1, 2]
        answer = solution(q1, q2)
        print(f'found answer : {answer}')
        assert(answer == 7)

    elif switch == 3:
        q1 = [1, 1]
        q2 = [1, 5]
        answer = solution(q1, q2)
        print(f'found answer : {answer}')
        assert(answer == -1)