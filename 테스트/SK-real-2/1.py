

def solution(goods):


    huboData = { good : set() for good in goods }
    for good in goods:
        huboData[good].update(genConsequtiveString(good))

    selectedData = {
        good : set() for good in goods
    }

    resultData = {
        good: [] for good in goods
    }

    # 다른 부분에 있는지 확인
    for key1, value1 in huboData.items():
        for subString in value1:

            isAbleToAdd = True
            for key2, value2 in huboData.items():
                if key2 == key1: continue
                if subString in value2: isAbleToAdd = False
            if isAbleToAdd:
                selectedData[key1].add(subString)

    selectedData


    # 가장 짧은 길이로만 다시 바꾸기
    for key1, value1 in selectedData.items():
        if not value1:
            resultData[key1].append("None")
            continue

        leastLength = min([  len(subString) for subString in value1  ])

        for subString in value1:
            if len(subString) == leastLength:
                resultData[key1].append(subString)
        resultData[key1].sort()

    resultData

    returnList = []
    for good in goods:
        tmpString = ""
        for _idx, string in enumerate(resultData[good]):
            tmpString += string
            if _idx != len(resultData[good])-1:
                tmpString += " "
        returnList.append(tmpString)

    return returnList


def genConsequtiveString(originString):
    """연속문자 구하기"""
    returnSet = set()

    for k in range(1, len(originString)):
        for i in range(0, len(originString) - k + 1):
            subString = originString[i:i+k]
            returnSet.add(subString)
    returnSet.add(originString)
    return returnSet



if __name__ == '__main__':
    #goods = ["pencil","cilicon","contrabase","picturelist"]
    goods = ["abcdeabcd","cdabe","abce","bcdeab"]
    returnValue = solution(goods)
    print(f'returnValue ; {returnValue}')