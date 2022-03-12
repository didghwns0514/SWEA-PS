
ans = 0
unitList = [1,5,10,50,100,500]

def solution(money, costs):
    global ans, unitList
    
    moneyList = [(cost, unitList[i]) for i, cost in enumerate(costs)]
    moneyList.sort( key=lambda x: x[0] / x[1])

    remainder_money = money
    idx = 0
    
    while idx < 6 and remainder_money > 0 :

        # moeny 카운트
        moneyCount = remainder_money // moneyList[idx][1]

        # 나머지 계산
        remainder_money = remainder_money % moneyList[idx][1]

        ans += moneyList[idx][0] * moneyCount

        # 인덱스 증가
        idx += 1

    return ans

if __name__=='__main__':
    money = 4578
    costs = [1, 4, 99, 35, 50, 1000]
    returnValue = solution(money, costs)
    print(f'returnValue : {returnValue}')