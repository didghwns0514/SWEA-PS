


def wrapper(i):
	for j in range(i):
		qStep1, qStep2, dataStep1Time, dataStep2Time, customerArrivalInfo, N, M, K, A, B = init()

		# finalAnswer = None
		# for _ in range(5):
		# 	finalAnswer = solution(j, qStep1, qStep2, dataStep1Time, dataStep2Time, customerArrivalInfo, N, M, K, A, B)
		#
		# 	print(f'#{j+1} {finalAnswer}')
		for _ in range(4):
			solution(j, qStep1, qStep2, dataStep1Time, dataStep2Time, customerArrivalInfo, N, M, K, A, B)
		finalAnswer = solution(j, qStep1, qStep2, dataStep1Time, dataStep2Time, customerArrivalInfo, N, M, K, A, B)
		print(f'#{j+1} {finalAnswer}')

def init():
	"""
	N : 접수 창구 i에서 고객 한 명의 고장을 접수하는 데 걸리는 처리 시간은 ai이다. (1 ≤ i ≤ N)
	M : 정비 창구 j에서 고객 한 명의 차량을 정비하는 데 걸리는 처리 시간은 bj이다. (1 ≤ j ≤ M)
	K : 지금까지 차량 정비소를 방문한 고객은 K명이다, 도착하는대로 번호 1번부터 부여
	    고객번호 k의 고객이 차량 정비소에 도착하는 시간은 tk이다. (1 ≤ k ≤ K)
	:return:
	"""
	N, M, K, A, B = map(int, input().split())
	qStep1 = [[] for _ in range(N)]
	qStep2 = [[] for _ in range(M)]
	dataStep1Time = list(map(int, input().split()))
	dataStep2Time = list(map(int, input().split()))
	customerArrivalInfo = list(map(int, input().split()))

	return qStep1, qStep2, dataStep1Time, dataStep2Time, customerArrivalInfo, N, M, K, A, B



def solution(testIter, _qStep1, _qStep2, _dataStep1Time, _dataStep2Time, _customerArrivalInfo, N, M, K, A, B):

	qStep1, qStep2, dataStep1Time, dataStep2Time, customerArrivalInfo = copy.deepcopy(_qStep1), \
																			 copy.deepcopy(_qStep2), \
																			 copy.deepcopy(_dataStep1Time), \
																			 copy.deepcopy(_dataStep2Time), \
																			 copy.deepcopy(_customerArrivalInfo)

	# customer : [arrivedCustormerCnt + 1 ,None, 0, None, 0] # 1, 2 창구
	globalTime = 0
	hqStep1 = []
	hqStep2 = []
	arrivedCustormerCnt = 0
	finishedCustomerCnt = 0
	answerSum = 0

	#while arrivedCustormerCnt < K and not(hqStep1) and not(hqStep2) and finishedCustomerCnt < k:
	while  finishedCustomerCnt < K:

		# add customer
		while True:
			if customerArrivalInfo:
				if customerArrivalInfo[0] == globalTime:
					customerTime = customerArrivalInfo.pop(0)
					heapq.heappush(hqStep1, [arrivedCustormerCnt + 1 ,None, 0, None, 0])
					arrivedCustormerCnt += 1
				else:
					break
			else:
				break

		# 고객 완료 빼기
		for idx, val in enumerate(qStep1):
			if val: # 창구번호 참
				tmpCustomer = val[0]
				if tmpCustomer[2] >= dataStep1Time[idx]: # 완료시점
					#heapq.heappush(hqStep2, val.pop(0))
					hqStep2.append(val.pop(0))

		for idx, val in enumerate(qStep2):
			if val: # 창구번호 참
				tmpCustomer = val[0]
				if tmpCustomer[4] >= dataStep2Time[idx]: # 완료시점
					customerNumber, St1Index, _, St2Index, _ = val.pop(0)
					finishedCustomerCnt += 1
					if St1Index == A and St2Index == B:
						answerSum += customerNumber


		# 고객 투입
		for idx, val in enumerate(qStep1): #  [[] for _ in range(N+1)]
			if not(val): # empty
				if hqStep1:
					customer = heapq.heappop(hqStep1)
					customer[1] = idx + 1 # 창구번호 기록
					qStep1[idx].append(customer)

		for idx, val in enumerate(qStep2): #  [[] for _ in range(N+1)]
			if not(val): # empty
				if hqStep2:


					targetIdx = min([ (idx, val[1]) for idx, val in enumerate(hqStep2)],
									key=lambda x:(x[0], x[1]))[0]

					customer = hqStep2.pop(targetIdx)

					customer[3] = idx + 1 # 창구번호 기록
					qStep2[idx].append(customer)

		# 고객 진행
		for idx, val in enumerate(qStep1):
			if val: # 창구번호 참
				tmpCustomer = val[0]
				tmpCustomer[2] += 1
		for idx, val in enumerate(qStep2):
			if val: # 창구번호 참
				tmpCustomer = val[0]
				tmpCustomer[4] += 1


		globalTime += 1

	finalNum = -1 if answerSum == 0 else answerSum

	return finalNum



if __name__ == '__main__':
	import sys
	import heapq
	import copy
	sys.stdin = open('sample_input.txt', 'r')
	T = int(input())
	wrapper(T)
