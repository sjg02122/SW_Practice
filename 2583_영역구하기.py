m,n,k = map(int,input().split())
maps = [[0]*n for i in range(m)]


for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            maps[j][i]=1

#for i in range(m-1,-1,-1):
#    print(maps[i])

visited = [[0]*n for i in range(m)]
for i in range(n):
    for j in range(m):
        if(maps[j][i]==1):
            visited[j][i]=1

def dfs(start):
    global maps, visited,m,n
    area = 1
    stack = [start]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]]=1
    maps[start[0]][start[1]]=2

    while(stack):
        node_y,node_x = stack.pop()
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if (ny >= m or ny < 0 or nx >= n or nx < 0):
                continue
            if(visited[ny][nx] ==0 and maps[ny][nx] ==0):
                visited[ny][nx]=1
                maps[ny][nx]=2
                area+=1
                stack.append((ny, nx))

    return area

areas = []

for i in range(n):
    for j in range(m):
        if(maps[j][i]==0):
            temp = dfs((j,i))
            if(temp!=0):
                areas.append(temp)

areas.sort()
print(len(areas))
for i in areas:
    print(i,end=' ')
