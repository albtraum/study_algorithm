#더 맵게!
#https://programmers.co.kr/learn/courses/30/lessons/42626/questions
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)  
    while(1):
        if len(scoville) == 1:
            return -1
        
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)

        cnt +=1
        if  K <= scoville[0]:
            return cnt
