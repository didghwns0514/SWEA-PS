
import copy
import itertools

def solution(n, info):

    tmpArrowList = [0] * 11 # 10 -> 밖, 0 -> 정중앙 10 - index로 점수 계산

    tmpReturnValue = subSolution(tmpArrowList, n, info)


    return tmpReturnValue



def subSolution(arrow_list, n, info):

    resultCombi = list(itertools.combinations_with_replacement( list(range(0, 11)) , n))

    #print(f'resultCombi : {resultCombi}')

    tmp_max_score = -987654321
    tmp_max_list = [-1]

    for tuple_info in resultCombi:
        tmpList = genList(tuple_info)
        tmpScoreRyan, tmpScoreApachi = calcScore(tmpList, info)

        if tmpScoreApachi >= tmpScoreRyan :
            continue

        elif tmpScoreApachi < tmpScoreRyan:
            if tmp_max_score > tmpScoreRyan - tmpScoreApachi:
                continue

            elif tmp_max_score < tmpScoreRyan - tmpScoreApachi:
                tmp_max_list = copy.deepcopy(tmpList)
                tmp_max_score = tmpScoreRyan - tmpScoreApachi
            else: # tmp_max_score == tmpScoreRyan
                # 가장 낮음 점수를 더많이 맞춤 경우
                for prev, curr in zip(reversed(tmp_max_list), reversed(tmpList)):
                    if prev == curr:
                        continue
                    elif prev > curr:
                        break
                    else:
                        tmp_max_list = copy.deepcopy(tmpList)
                        # curr_max_point = tmpPointCalculation
                        break


    return tmp_max_list

def genList(tuple_info):
    tmpList = [0] * 11  # 10 -> 밖, 0 -> 정중앙 10 - index로 점수 계산
    for index_info in tuple_info:
        tmpList[index_info] += 1

    return tmpList

def calcScore(arrow_list, info): # tmpScoreRyan, tmpScoreApachi


    return sum( [ (10 - idx) for idx, val in enumerate(arrow_list) if (val > info[idx] and val > 0) ] ), \
           sum( [ (10 - idx) for idx, val in enumerate(info) if (val >= arrow_list[idx] and val > 0) ] )


if __name__ == "__main__":
    selection = 2

    if selection == 0:
        n = 5
        info = [2,1,1,1,0,0,0,0,0,0,0]

    elif selection == 1:
        n = 1
        info = [1,0,0,0,0,0,0,0,0,0,0]

    elif selection == 2:
        n = 9
        info = 	[0,0,1,2,0,1,1,1,1,1,1]

    elif selection == 3:
        n = 10
        info = 	[0,0,0,0,0,0,0,0,3,4,3]

    returnValue = solution(n, info)
    print(f'returnValue : {returnValue}')


#
# def subSolution2(arrow_list, n):
#     global curr_arrowList, curr_max_point
#
#     if sum(arrow_list) == n:
#         tmpPointCalculation = calcScore(arrow_list)
#         if tmpPointCalculation > curr_max_point:
#             curr_max_point = tmpPointCalculation
#             curr_arrowList = copy.deepcopy(arrow_list)
#         elif tmpPointCalculation == curr_max_point:
#             # 가장 낮음 점수를 더많이 맞춤 경우
#             for _index, prev, curr in enumerate(zip(reversed(curr_arrowList), reversed(arrow_list))):
#                 if prev == curr: continue
#                 elif prev > curr : break
#                 else:
#                     curr_arrowList = copy.deepcopy(arrow_list)
#                     # curr_max_point = tmpPointCalculation
#                     break
#         else: pass # 낮아서 업데이트 할 필요 없음
#         return
#
#     for k in range(len(arrow_list)):
#         tmpArrowList = copy.deepcopy(arrow_list)
#         tmpArrowList[k] += 1
#         subSolution(tmpArrowList, n)
#
#     return
