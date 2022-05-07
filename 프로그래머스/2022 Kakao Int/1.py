
dataCharacter = {
    "R" : 0,
    "T" : 0,
    "C" : 0,
    "F" : 0,
    "J" : 0,
    "M" : 0,
    "A" : 0,
    "N" : 0
}

dataCharToNum = {

    "A" : 0,
    "C" : 1,
    "F" : 2,
    "J" : 3,
    "M" : 4,
    "N" : 5,
    "R" : 6,
    "T" : 7

}
def solution(survey, choices):
    global dataCharacter, dataCharToNum

    for surv, choice in zip(survey, choices):
        surveyAnswer(surv, choice)

    answer = ''
    for i in range(4):
        answer += filterAnswer(i+1)

    return answer

def filterAnswer(index):


    if index == 1:
        return characterCompare("RT")
    elif index == 2:
        return characterCompare("CF")
    elif index == 3:
        return characterCompare("JM")
    elif index == 4:
        return characterCompare("AN")

def characterCompare(characters):
    global dataCharacter

    first, second = list(characters)
    if dataCharacter[first] > dataCharacter[second]:
        return first
    elif dataCharacter[first] < dataCharacter[second]:
        return second
    else:
        return sorted(list(characters))[0]


def surveyAnswer( text, choice):
    global dataCharacter

    """
    
    1	매우 비동의
    2	비동의
    3	약간 비동의
    4	모르겠음
    5	약간 동의
    6	동의
    7	매우 동의

    """
    firstText, secondText = text

    if choice == 4:
        pass
    else:
        if choice == 1:
            dataCharacter[firstText] += 3
        elif choice == 2:
            dataCharacter[firstText] += 2
        elif choice == 3:
            dataCharacter[firstText] += 1
        elif choice == 5:
            dataCharacter[secondText] += 1
        elif choice == 6:
            dataCharacter[secondText] += 2
        elif choice == 7:
            dataCharacter[secondText] += 3






if __name__ == "__main__":

    switch = 2

    if switch == 1:
        survey = ["AN", "CF", "MJ", "RT", "NA"]
        choices = [5, 3, 2, 7, 5]
        answer = solution(survey, choices)
        print(f'found answer : {answer}')
        assert(answer == "TCMA")

    elif switch == 2:
        survey = ["TR", "RT", "TR"]
        choices = [7, 1, 3]
        answer = solution(survey, choices)
        print(f'found answer : {answer}')
        assert(answer == "RCJA")
