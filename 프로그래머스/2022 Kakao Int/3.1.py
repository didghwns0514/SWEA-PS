import sys
sys.setrecursionlimit(30000)

TIME_ELAPSED = 987654321
IS_FOUND = False

def solution(alp, cop, problems):
    answer = 0

    #subSolution(alp, cop, problems, 0, 0)
    returnValue = subSolution(alp, cop, problems, 0)


    return returnValue


def subSolution(alp, cop, problems, elapsed_time):

    totalLength = len(problems)
    tmpDataCheck = [ alp >= problem[0] and cop >= problem[1] for problem in problems]
    while not all([ alp >= problem[0] and cop >= problem[1] for problem in problems]):

        solveableProblems = [
            problem for problem in problems if alp >= problem[0] and cop >= problem[1]
        ]

        if not solveableProblems: # 풀 수 있는 문제가 없으므로 자습해야 함

            # decide which fiedl to study
            filteredData = [
                ( max(problem[0] - alp, 0) + max(problem[1] - cop, 0), _idx) for _idx, problem in enumerate(problems) \
                if problem[0] - alp > 0 or problem[1] - cop > 0
            ]
            filteredFilteredData = sorted(filteredData, key=lambda x: x[0])
            selectedProblemIdx = filteredFilteredData[0][1]
            alp = problems[selectedProblemIdx][0]
            cop = problems[selectedProblemIdx][1]
            elapsed_time += filteredFilteredData[0][0]

        else: # 풀 수 있는 문제가 있음
            pass
            # 가성비 따져서 자습이 나은지 확인
            selectedProblemIdx2, targetType = getTargetProblem(alp, cop, problems)
            runStudy, selectedProblemIdx = getStudyProblem(alp, cop, problems, targetType, selectedProblemIdx2)


            if runStudy : # 문제풀기가 낫다
                cnt = 0

                while alp < problems[selectedProblemIdx2][0] and cop < problems[selectedProblemIdx2][1]:

                    alp += problems[selectedProblemIdx][2]
                    cop += problems[selectedProblemIdx][3]

                    cnt += problems[selectedProblemIdx][4]
                elapsed_time += cnt
            else: # 자습이 낫다
                if targetType == 0: #alp
                    delta = problems[selectedProblemIdx2][0] - alp
                    alp += delta

                elif targetType == 1: #cop
                    delta = problems[selectedProblemIdx2][1] - cop
                    cop += delta

                elapsed_time += delta


        # next while loop
        #tmpDataCheck = [ alp >= problem[0] and cop >= problem[1] for problem in problems]


    return elapsed_time

def getStudyProblem(alp, cop, problems, targetPType, targetIDX):

    studyFilter = None
    if targetPType == 0 : # alp
        studyFilter = [ (_idx, problem[2] / problem[4]) for _idx, problem in enumerate(problems) if problem[0] <= alp and problem[1] <= cop ]
    elif targetPType == 1 : # cops
        studyFilter = [ (_idx, problem[3] / problem[4]) for _idx, problem in enumerate(problems) if problem[0] <= alp and problem[1] <= cop ]

    studyFilterFiltered = sorted(studyFilter, key=lambda x:x[1], reverse=True)
    studyFilterIDX = studyFilterFiltered[0][0]
    studyEffValue = studyFilterFiltered[0][1]

    if studyEffValue >= 1:
        return True, studyFilterIDX
    else:
        return False, studyFilterIDX


def getTargetProblem(alp, cop, problems): # index, 0/1 [0:alps, 1:cops]
    alpsFilter = [ (_idx, problem[0] - alp) for _idx, problem in enumerate(problems) if problem[0] - alp > 0 ]
    copsFilter = [ (_idx, problem[1] - cop) for _idx, problem in enumerate(problems) if problem[1] - cop > 0 ]

    if alpsFilter and copsFilter:
        alpsFiltered = sorted(alpsFilter, key= lambda x: x[1])[0]
        copsFiltered = sorted(copsFilter, key= lambda x: x[1])[0]

        if alpsFiltered[0] == copsFiltered[0]:
            return copsFiltered[0], 1
        else:
            if alpsFiltered[0] >= copsFiltered[0]:
                return copsFiltered[0], 1
            else:
                return alpsFiltered[0], 0
    elif alpsFilter and not copsFilter:
        alpsFiltered = sorted(alpsFilter, key=lambda x: x[1])[0]
        return alpsFiltered[0], 0
    elif not alpsFilter and copsFilter:
        copsFiltered = sorted(copsFilter, key=lambda x: x[1])[0]
        return copsFiltered[0], 1

if __name__ == "__main__":

    switch = 1

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

