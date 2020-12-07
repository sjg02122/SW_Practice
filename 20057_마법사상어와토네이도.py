#import numpy as np

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
out_sand =0

def Push_Sand(d,sand,x,y):
    global maps,out_sand,n
    #print(sand,x,y)
    first_sand = sand
    move_left =[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),
              (-1,-1,0.1),(1,-1,0.1),(0,-2,0.05)]
    move_right=[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),
              (-1,1,0.1),(1,1,0.1),(0,2,0.05)]
    move_up = [(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),
               (-2,0,0.05),(0,-2,0.02),(0,2,0.02)]
    move_down = [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),
                 (1,-1,0.1),(1,1,0.1),(2,0,0.05)]
    move_list = [move_up,move_down,move_right,move_left]
    last_move = [(-1,0,1),(1,0,1),(0,1,1),(0,-1,1)]
    for i in move_list[d]:
        temp_x = x+ i[0]
        temp_y = y+ i[1]
        temp_sand = int(first_sand*i[2])
        sand -= temp_sand
        #print(temp_sand,sand,i[2])
        if(temp_x<0 or temp_x >=n or temp_y<0 or temp_y >=n):
            out_sand+= temp_sand
            continue
        maps[temp_x][temp_y] += temp_sand

    last_x = x+last_move[d][0]
    last_y = y+last_move[d][1]
    if(last_x>=n or last_x<0 or last_y >=n or last_y<0):
        out_sand+= sand
    else:
        maps[last_x][last_y] += sand

    #show_maps()


def show_maps():
    global maps
    #print(np.array(maps))
    #print()

#init
finger = [n//2,n//2]
#up,down,right,left
direction = [(-1,0),(1,0),(0,1),(0,-1)]

#move_finger
for idx in range(n-1):
    if(idx%2==0):
        #left,down
        for _ in range(idx+1):
            finger[0] = finger[0]+direction[3][0]
            finger[1] = finger[1]+direction[3][1]

            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]]=0
            Push_Sand(3,temp,finger[0],finger[1])

        for _ in range(idx+1):
            finger[0] = finger[0]+direction[1][0]
            finger[1] = finger[1]+direction[1][1]

            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]]=0
            Push_Sand(1,temp,finger[0],finger[1])

    else:
        #right,up
        for _ in range(idx + 1):
            finger[0] = finger[0]+direction[2][0]
            finger[1] = finger[1]+direction[2][1]

            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]] = 0
            Push_Sand(2, temp, finger[0], finger[1])


        for _ in range(idx + 1):
            finger[0] = finger[0]+direction[0][0]
            finger[1] = finger[1]+direction[0][1]
            temp = maps[finger[0]][finger[1]]
            maps[finger[0]][finger[1]] = 0
            Push_Sand(0, temp, finger[0], finger[1])


for _ in range(n):
    finger[0] = finger[0] + direction[3][0]
    finger[1] = finger[1] + direction[3][1]
    temp = maps[finger[0]][finger[1]]
    maps[finger[0]][finger[1]]=0
    Push_Sand(3,temp,finger[0],finger[1])

print(out_sand)