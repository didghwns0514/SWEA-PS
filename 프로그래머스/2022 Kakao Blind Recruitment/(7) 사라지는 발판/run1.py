
def solution(board, aloc, bloc):
    answer = -1
    return answer

if __name__ == "__main__":

    switch = 1

    if switch == 1:
        board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
        skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
        answer = solution(board, skill)
        print(f'found answer : {answer}')
        assert(answer == 10)

    elif switch == 2:
        board = [[1,2,3],[4,5,6],[7,8,9]]
        skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
        answer = solution(board, skill)
        print(f'found answer : {answer}')
        assert(answer == 6)
