def solution(info, edges):
    answer = 0
    return answer



if __name__ == "__main__":

    switch = 1

    if switch == 1:
        info = [0,0,1,1,1,0,1,0,1,0,1,1]
        edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
        assert(solution(info, edges) == 5)

    elif switch == 2:
        info = [0,1,0,1,1,0,1,0,0,1,0]
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
        assert(solution(info, edges) == 5)
