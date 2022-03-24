from collections import deque
import copy

def solution(arr, processes):
    time = 0
    """
    endtime : deque([])
    (r/w, end time, value C)
    """
    returnResult = []
    processQ = deque()
    waitQ = deque()
    # idle : 0, read : 1, write : 2
    arrayStatus = 0

    while process or processQ or waitQ:

        # 확인절차
        if processes:
            tempProcessPeek = copy.deepcopy(processes[0])

            action, t1, t2, A, B_ = tempProcessPeek.split(' ', 4)
            B, writeC = None, None
            if action == 'read':
                B = B_
            elif action == 'write':
                B, writeC = B_.split(' ')
                writeC = int(writeC)
            t1, t2, A, B = int(t1), int(t2), int(A), int(B)

            # 대기큐에 넣기
            # 시간이 되는건지 확인
            if t1 == time:
                if action == 'read':
                    waitQ.append([1, t1, t2, (A, B, None), time])
                elif action == 'write':
                    waitQ.append([1, t1, t2, (A, B, writeC), time])
                processes.pop(0)


        # 완료작업 제거
        for i in range(len(processQ)):
            tmpStatus = getStatus(processQ)
            tmpPop = processQ.popleft()
            if tmpPop[0] == tmpStatus:
                if abs(time - tmpPop[1] >= tmpPop[2]):
                    if tmpPop[0] == 1:  # read
                        returnResult.append(
                            ''.join(arr[tmpPop[3][0]:tmpPop[3][1] + 1])
                        )
                    elif tmpPop[1] == 2:  # write:
                        for k in range(tmpPop[3][0], tmpPop[3][1] + 1):
                            arr[k] = str(tmpPop[3][2])
                        arr
                else:
                    #tmpPop[4] = time
                    processQ.append( copy.deepcopy(tmpPop) )



        # 대기 큐에서 빼서 작업큐에 넣기
        # waitQ.append([1, t1, t2, (A, B, writeC), None])
        if waitQ:
            if getStatus(processQ) == 0:
                writeJobFilter = [work[0] == 2 for work in waitQ]
                if writeJobFilter and any(writeJobFilter):
                    selectedWriteJob = sorted( [ (work, _idx) for _idx, work in enumerate(waitQ) if work[0] == 2], key=lambda x: x[0][1])[0]
                    # selectedWriteJob[0][4] = time + 1
                    processQ.append( copy.deepcopy(selectedWriteJob[0]) )
                    waitQ.remove(selectedWriteJob[1])
                else:
                    processQ.append( copy.deepcopy(waitQ.popleft()) )

            # 한 번에 여러 프로세스가 배열에서 동시에 읽기 작업을 수행할 수 있습니다.
            elif getStatus(processQ) == 1:  # idle, read

                # 하나 이상의 쓰기 작업이 대기 중인 경우, 새로운 읽기 요청 또한 대기해야 합니다.
                if any([work[0] == 2 for work in waitQ]):
                    pass
                else:
                    for j in range(len(waitQ)):
                        tmpPop = waitQ.popleft()
                        if tmpPop[0] == 1:
                            # tmpPop[4] = time + 1
                            processQ.append( copy.deepcopy(tmpPop) )
                        else:
                            waitQ.append( copy.deepcopy(tmpPop) )
            elif getStatus(processQ) == 2:  # write, 한 번에 하나의 프로세스만 배열에서 쓰기 작업
                pass

        # 작업큐 작업 진행
        # - 시간 지나면 되는 것
        # if arrayStatus == 0:  # idle
        #     if processQ:
        #         arrayStatus = processQ[0][0]



        # status 설정
        # if not processQ:
        #     arrayStatus = 0

        # increase time
        time += 1

    returnResult.append(str(time))

    return returnResult


def getStatus(workQ):
    if not workQ : return 0 # idle
    if any([work[0] == 2 for work in workQ]):
        return 2 # write
    else:
        return 1 # read


if __name__ == '__main__':
    arr = ["1","2","4","3","3","4","1","5"]
    process = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]

    returnValue = solution(arr, process)
    print(f'returnValue : {returnValue}')