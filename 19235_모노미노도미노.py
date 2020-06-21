from collections import deque

transform_right = {
    (0,0):(0,3),(0,1):(1,3),(0,2):(2,3),(0,3):(3,3),
    (1,0):(0,2),(1,1):(1,2),(1,2):(2,2),(1,3):(3,2),
    (2,0):(0,1),(2,1):(1,1),(2,2):(2,1),(2,3):(3,1),
    (3,0):(0,0),(3,1):(1,0),(3,2):(2,0),(3,3):(3,0)
}


def go_blocks(block,temp_maps,idx):
    block_type,cur_x,cur_y = block
    if(block_type==1):
        ny = cur_y
        nx = 0
        while(True):
            if(temp_maps[nx][ny]):
                nx-=1
                break
            if(nx>=5):
                break
            nx+=1
        temp_maps[nx][ny]=idx
    elif(block_type==2):
        ny1 = cur_y
        ny2 = ny1+1
        nx = 0
        while(True):
            if(temp_maps[nx][ny1] or temp_maps[nx][ny2]):
                nx-=1
                break
            if(nx>=5):
                break
            nx+=1
        temp_maps[nx][ny1]=idx
        temp_maps[nx][ny2]=idx

    elif(block_type==3):
        nx2=1
        ny = cur_y
        while(True):
            if(temp_maps[nx2][ny]):
                nx2-=1
                break
            if(nx2>=5):
                break
            nx2+=1
        nx1 = nx2 - 1
        temp_maps[nx2][ny]=idx
        temp_maps[nx1][ny]=idx

    return temp_maps

def get_scores(maps,s):

    while(True):
        condition2 = 1
        while(True):
            condition1 = 1
            for i in range(5, -1, -1):
                if (0 not in maps[i]):
                    s += 1
                    condition1 = 0
                    condition2 =0
                    del maps[i]
                    maps.appendleft([0, 0, 0, 0])
            if(condition1):
                break

        for j in range(4):
            candidate = []
            for i in range(6):
                if (maps[i][j] != 0):
                    candidate.append((i, j, maps[i][j]))
            while (candidate):
                cur_x, cur_y, value = candidate.pop()

                if (cur_y + 1 <= 3 and maps[cur_x][cur_y + 1] == value):
                    ny1, ny2 = cur_y, cur_y + 1
                    nx = cur_x + 1
                    maps[cur_x][ny1] = 0
                    maps[cur_x][ny2] = 0
                    while (True):
                        if (nx >= 6 or maps[nx][ny1] or maps[nx][ny2]):
                            maps[nx - 1][ny1] = value
                            maps[nx - 1][ny2] = value
                            break
                        nx += 1

                elif (cur_y - 1 >= 0 and maps[cur_x][cur_y - 1] == value):
                    ny1, ny2 = cur_y - 1, cur_y
                    nx = cur_x + 1
                    maps[cur_x][ny1] = 0
                    maps[cur_x][ny2] = 0
                    while (True):
                        if (nx >= 6 or maps[nx][ny1] or maps[nx][ny2]):
                            maps[nx - 1][ny1] = value
                            maps[nx - 1][ny2] = value
                            break
                        nx += 1
                else:
                    maps[cur_x][cur_y] = 0
                    nx = cur_x + 1
                    while (True):
                        if (nx >= 6 or maps[nx][cur_y]):
                            maps[nx - 1][cur_y] = value
                            break
                        nx += 1
        if(condition1 and condition2):
            break
    return maps,s

def check_up(maps):

    for _ in range(2):
        for i in range(4):
            if(maps[0][i] or maps[1][i]):
                maps.pop()
                maps.appendleft([0,0,0,0])
    return maps

def transform_block(block):
    b_type,b_x,b_y =block
    nx, ny = b_x, b_y
    if(b_type==3):
        b_type=2
        nx+=1
    elif(b_type==2):
        b_type=3
    nx, ny = transform_right[(nx, ny)]
    nblock = (b_type, nx, ny)
    return nblock

n = int(input())
blocks = [list(map(int,input().split())) for _ in range(n)]

green_score, green_blocks = 0,0
blue_score, blue_blocks = 0,0

green_board = deque([[0,0,0,0]for _ in range(6)])
blue_board = deque([[0,0,0,0]for _ in range(6)])
idx=0
for i in blocks:
    idx+=1
    '''
    green_board = go_blocks(i,green_board,idx)
    #show_maps(green_board)
    green_board,green_score=get_scores(green_board,green_score)
    #show_maps(green_board)
    green_board = check_up(green_board)
    #show_maps(green_board)

    blue_block = transform_block(i)
    blue_board = go_blocks(blue_block,blue_board,idx)
    show_maps(blue_board)
    blue_board,blue_score = get_scores(blue_board,blue_score)
    show_maps(blue_board)
    blue_board = check_up(blue_board)
    show_maps(blue_board)
    '''
    green_board = go_blocks(i,green_board,idx)
    blue_block = transform_block(i)
    blue_board = go_blocks(blue_block,blue_board,idx)

    green_board,green_score=get_scores(green_board,green_score)
    blue_board,blue_score = get_scores(blue_board,blue_score)

    green_board = check_up(green_board)
    blue_board = check_up(blue_board)


def maps_show():
    global green_board,blue_board
    for i in range(6):
        print(green_board[i],end=' ')
        print(blue_board[i])
    print()

ans_s = blue_score+green_score
ans_b=0
for i in range(6):
    for j in range(4):
        if(blue_board[i][j]!=0):
           ans_b+=1
        if(green_board[i][j]!=0):
            ans_b+=1

print(ans_s)
print(ans_b)


