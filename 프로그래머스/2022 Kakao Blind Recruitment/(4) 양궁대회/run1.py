
import copy


curr_arrowList = []
curr_max_point = 0

def solution(n, info):
    global curr_arrowList, curr_max_point

    tmpArrowList = [0] * 11 # 10 -> 밖, 0 -> 정중앙 10 - index로 점수 계산

    answer = []
    return answer


def subSolution(arrow_list):
    global curr_arrowList, curr_max_point

    if sum(arrow_list) == 10:
        tmpPointCalculation = calcScore(arrow_list)
        if tmpPointCalculation > curr_max_point:
            curr_max_point = tmpPointCalculation
            curr_arrowList = arrow_list
            return
        elif tmpPointCalculation == curr_max_point:

        else: pass # 낮아서 업데이트 할 필요 없음
        return

def calcScore(arrow_list):

    return sum( [ val*(10 - idx) for idx, val in enumerate(arrow_list) ] )


if __name__ == "__main__":
    selection = 0

    if selection == 0:
        n = 5
        info = [2,1,1,1,0,0,0,0,0,0,0]

    elif selection == 1:
        n = 1
        info = [1,0,0,0,0,0,0,0,0,0,0]

    elif selection == 2:
        n = 9
        info = 	[0,0,1,2,0,1,1,1,1,1,1]

    solution(n, info)

