#왕실의 나이트 

- 단순 구현 문제

'''python
# -*- coding: utf-8 -*-
# 입력 받기 
# ex) a1,b3 => a는 열 , 1은 행을 의미 
loc = input()

#좌표 분해
row = int(loc[1]) # 행
col = ord(loc[0])-int(ord('a'))+1 # 열
ans = 0 
#나이트의 모든 경우의수

can_move = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
for e in can_move :
    if row+e[1] >0 and col+e[0] > 0 and row+e[1]<9 and col+e[0] <9 :
        ans +=1

print(ans)
'''
