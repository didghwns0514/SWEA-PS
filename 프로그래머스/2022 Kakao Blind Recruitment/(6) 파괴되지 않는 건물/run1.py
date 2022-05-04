
def solution2(board, skills):

    #########################
    # 효율성 안좋음!
    #########################

    for skill in skills:

        _type, r1, c1, r2, c2, degree = skill
        # _type=1 : 공격, _type=2 : 힐링

        for r, c in select_square(r1, c1, r2, c2):
            if _type == 1:
                board[r][c] -= degree
            elif _type == 2:
                board[r][c] += degree

    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                count += 1

    answer = 0
    return count

def solution(board, skills):

    data_board = { (r, c) : board[r][c] for r in range(len(board)) for c in range(len(board[0])) }

    for skill in skills:

        _type, r1, c1, r2, c2, degree = skill
        # _type=1 : 공격, _type=2 : 힐링

        for ri in range(r1, r2 + 1):
            for ci in range(c1, c2 + 1):

                if _type == 1 : data_board[(ri, ci)] -= degree
                elif _type == 2 : data_board[(ri, ci)] += degree

    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if data_board[(i, j)] > 0:
                count += 1

    answer = 0
    return count

def select_square(r1, c1, r2, c2):
    returnResult = []

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            returnResult.append( ( r, c ) )

    return returnResult

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
