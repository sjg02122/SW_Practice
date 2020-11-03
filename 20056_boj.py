from copy import deepcopy

n,m,k = map(int,input().split())
maps = [[[] for _ in range(n)] for _ in range(n)]

fire_location =set()

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


for _ in range(m):
    r,c,M,s,d = map(int,input().split())
    r-=1
    c-=1
    fire_location.add((r,c))
    maps[r][c].append((M,s,d))


def show():
    for i in range(n):
        print(maps[i])

for _ in range(k):
    #이동명령
    next_candidate =set()
    copy_maps = [[[] for _ in range(n)] for _ in range(n)]
    #show()
    while(fire_location):
        #모든 Fire 이동
        cur_x,cur_y = fire_location.pop()
        while(maps[cur_x][cur_y]):
            cur_m,cur_s,cur_d=maps[cur_x][cur_y].pop()
            if (cur_s * dx[cur_d] > 0):
                nx = cur_x + (cur_s * dx[cur_d]) % n
                if (nx >= n):
                    nx = nx - n
            else:
                nx = cur_x - abs(cur_s * dx[cur_d]) % n
                if (nx < 0):
                    nx = n - abs(nx)
            if (cur_s * dy[cur_d] > 0):
                ny = cur_y + (cur_s * dy[cur_d]) % n
                if (ny >= n):
                    ny = ny - n
            else:
                ny = cur_y - abs(cur_s * dy[cur_d]) % n
                if (ny < 0):
                    ny = n - abs(ny)
            copy_maps[nx][ny].append((cur_m, cur_s, cur_d))
            next_candidate.add((nx, ny))
    #print()
    #이동이 끝난 후 같은 위치에 2개 있는지 체크
    for i in range(n):
        for j in range(n):
            if(len(copy_maps[i][j])>1):
                total_m = 0
                total_s =0
                even_d = 0
                odd_d = 0
                cnt=0
                while(copy_maps[i][j]):
                    cur_m,cur_s,cur_d = copy_maps[i][j].pop()
                    total_m+= cur_m
                    total_s+= cur_s
                    if(cur_d%2==0):
                        even_d+=1
                    else:
                        odd_d+=1
                    cnt+=1
                m_ = total_m//5
                if(m_==0):
                    continue
                s_ = total_s//cnt
                if(even_d == cnt or odd_d == cnt):
                    dir_ =[0,2,4,6]
                else:
                    dir_ = [1,3,5,7]
                for k in range(4):
                    copy_maps[i][j].append((m_,s_,dir_[k]))
    maps = deepcopy(copy_maps)
    fire_location = deepcopy(next_candidate)

ans=0
#show()
for i in range(n):
    for j in range(n):
        if(len(maps[i][j])==1):
            ans += maps[i][j][0][0]
        else:
            for k in range(len(maps[i][j])):
                ans += maps[i][j][k][0]

print(ans)