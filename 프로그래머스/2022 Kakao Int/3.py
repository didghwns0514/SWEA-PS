import sys
sys.setrecursionlimit(30000)

TIME_ELAPSED = 987654321
IS_FOUND = False

def solution(alp, cop, problems):
    answer = 0

    subSolution(alp, cop, problems, 0, 0)

    return TIME_ELAPSED

def subSolution(alp, cop, problems, elapsed_time, depth):
    global TIME_ELAPSED, IS_FOUND

    solveableFilter = [ alp >= problem[0] and cop >= problem[1] for problem in problems]

    #if IS_FOUND: return

    if depth > 990:
        return None

    if elapsed_time >= TIME_ELAPSED: return None

    if all(solveableFilter):
        TIME_ELAPSED = min(TIME_ELAPSED, elapsed_time)
        IS_FOUND = True
        return

    # for i in range(3):
    #
    #     if i == 0: # 알고력 높이기
    #         subSolution(alp + 1, cop, problems, elapsed_time + 1)
    #     elif i == 1: # 코딩력 높이기
    #         subSolution(alp, cop + 1, problems, elapsed_time + 1)
    #     elif i == 2: #풀 수 있는 문제 풀어 높이기
    #         solveableProblems = [
    #             problem for problem in problems if alp >= problem[0] and cop >= problem[1]
    #         ]
    #         for prob in solveableProblems:
    #             alp_req, cop_req, alp_rwd, cop_rwd, cost = prob
    #             subSolution(alp + alp_rwd, cop + cop_rwd, problems, elapsed_time + cost)

    solveableProblems = [
        problem for problem in problems if alp >= problem[0] and cop >= problem[1]
    ]
    if solveableProblems:
        for prob in solveableProblems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = prob
            subSolution(alp + alp_rwd, cop + cop_rwd, problems, elapsed_time + cost, depth+1)
    else:
        subSolution(alp + 1, cop, problems, elapsed_time + 1, depth+1)
        subSolution(alp, cop + 1, problems, elapsed_time + 1, depth+1)

if __name__ == "__main__":

    switch = 2

    if switch == 1:
        alp = 10
        cop = 10
        problems = [[10,15,2,1,2],[20,20,3,3,4]]
        answer = solution(alp, cop, problems)
        print(f'found answer : {answer}')
        assert(answer == 15)

    elif switch == 2:
        alp = 0
        cop = 0
        problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
        answer = solution(alp, cop, problems)
        print(f'found answer : {answer}')
        assert(answer == 13)

