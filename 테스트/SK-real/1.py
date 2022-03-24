
"""
1450


"""
def solution(money, costs):
    answer = 0

    unit = [1,5,10,50,100,500]

    order = sorted([(cost,unit[i]) for i,cost in enumerate(costs)],key = lambda x: x[0]/x[1])

    remain = money
    idx = 0
    while remain > 0 and idx < 6 :
        count = remain // order[idx][1] 
        remain = remain % order[idx][1]

        answer += (count * order[idx][0])
        idx += 1

    return answer

if __name__=='__main__':
    money = 4578
    costs = [1, 4, 99, 35, 50, 1000]
    returnValue = solution(money, costs)
    #print(f'returnValue : {returnValue}')
    print(returnValue)