import copy
MAX_SHEEP = 0

def solution(info, edges):
    global MAX_SHEEP

    data_graph = gen_graph(edges)
    subSolution(info, data_graph, [], 0)

    return MAX_SHEEP

def subSolution(info, data_graph, visited, currVertex):
    global MAX_SHEEP

    if not visited and data_graph[currVertex] == 0:
        return

    visitedSave = copy.deepcopy(visited)
    visitedSave.append(currVertex)

    visitedToIndex = [ info[vertex] for vertex in visitedSave ]
    if visitedToIndex.count(0) <= visitedToIndex.count(1):
        MAX_SHEEP = max(MAX_SHEEP, visitedToIndex.count(0))
        return

    candidateVertex = set()
    for vertex in visitedSave:
        candidateVertex.update(data_graph[vertex])
    candidateVertex = candidateVertex - set(visitedSave)

    for vertex in candidateVertex:
        subSolution(info, data_graph, visitedSave, vertex)

def gen_graph(edges):

    data_graph = dict()
    for edge in edges:
        v1, v2 = edge
        if v1 not in data_graph:
            data_graph[v1] = set()
        data_graph[v1].add(v2)
        if v2 not in data_graph:
            data_graph[v2] = set()
        data_graph[v2].add(v2)

    return data_graph


if __name__ == "__main__":

    switch = 2

    if switch == 1:
        info = [0,0,1,1,1,0,1,0,1,0,1,1]
        edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
        answer = solution(info, edges)
        print(f'found answer : {answer}')
        assert(answer == 5)

    elif switch == 2:
        info = [0,1,0,1,1,0,1,0,0,1,0]
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
        answer = solution(info, edges)
        print(f'found answer : {answer}')
        assert(answer == 5)
