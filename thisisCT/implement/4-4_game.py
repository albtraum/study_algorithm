# -*- coding: utf-8 -*-
#n,m 입력받기 
n,m = map(int,input().split())

save = [ [0 for _ in range(n)] for  _ in range(m)]

#현위치, 방향 
x,y,look = map(int,input().split())
save[x][y] = 1 #현위치 방문처리 
ans = 1 
#게임 지도 입력4
game_map =[]
for _ in range(n):
    game_map.append(list(map(int,input().split())))

#방향 0:북 / 1:서 / 2:남 / 3:동
face = [[-1,0],[0,-1],[1,0],[0,1]]
turn_cnt = 0
#시뮬레이션 진행
while 1:
    #step 1 
    turn=(turn_cnt)%4

    temp_x = x+face[turn][0] 
    temp_y = y+face[turn][1]

    if game_map[temp_x][temp_y] == 0 and save[temp_x][temp_y] ==0:
        ans +=1
        game_map[temp_x][temp_y] = 1
        turn_cnt = 0
        x=temp_x
        y=temp_y
        continue 
    else :
        turn_cnt += 1
    #step 2 : while 을 통한 구현 

    #strp 3 
    if turn_cnt%4== 0 and turn_cnt != 0:
        #바라보는 방향 유지, 
        temp_x= x-face[turn][0]
        temp_y= y-face[turn][1]
        if game_map[temp_x][temp_y] == 0 :
            x=temp_x
            y=temp_y
    #조건에 의한 중단 
        else :
            break
        turn_cnt +=1

print(ans)
