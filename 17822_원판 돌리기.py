from collections import deque

n, m, t = map(int, input().split())

circles = [0]

for _ in range(n):
    circles.append(deque(list(map(int, input().split()))))

commands = []

for _ in range(t):
    x, d, k = map(int, input().split())
    commands.append((x, d, k))

while (commands):
    x, d, k = commands.pop(0)
    for i in range(1, n + 1):
        # x의 배수인 원판만
        if (i % x == 0):
            if (d == 0):
                circles[i].rotate(k)
            else:
                circles[i].rotate(-k)

    # 인접수
    zeros = []
    # 1번 원판
    for i in range(m):
        if (i + 1 > m - 1):
            temp = 0
        else:
            temp = i + 1

        if (circles[1][i] == circles[1][i - 1] and circles[1][i] != 0):
            zeros.append((1, i))
            if (i - 1 < 0):
                zeros.append((1, m - 1))
            else:
                zeros.append((1, i - 1))
        if (circles[1][i] == circles[1][temp] and circles[1][i] != 0):
            zeros.append((1, i))
            zeros.append((1, temp))

        if (circles[1][i] == circles[2][i] and circles[1][i] != 0):
            zeros.append((1, i))
            zeros.append((2, i))

    # n번 원판
    for i in range(m):
        if (i + 1 > m - 1):
            temp = 0
        else:
            temp = i + 1

        if (circles[n][i] == circles[n][i - 1] and circles[n][i] != 0):
            zeros.append((n, i))
            if (i - 1 < 0):
                zeros.append((n, m - 1))
            else:
                zeros.append((n, i - 1))
        if (circles[n][i] == circles[n][temp] and circles[n][i] != 0):
            zeros.append((n, i))
            zeros.append((n, temp))

        if (circles[n][i] == circles[n - 1][i] and circles[n][i] != 0):
            zeros.append((n, i))
            zeros.append((n - 1, i))

    for i in range(2, n):
        # 2~n-1번원판
        for j in range(m):
            if (j + 1 > m - 1):
                temp = 0
            else:
                temp = j + 1

            if (circles[i][j] == circles[i][j - 1] and circles[i][j] != 0):
                zeros.append((i, j))
                if (j - 1 < 0):
                    zeros.append((i, m - 1))
                else:
                    zeros.append((i, j - 1))
            if (circles[i][j] == circles[i][temp] and circles[i][j] != 0):
                zeros.append((i, j))
                zeros.append((i, temp))
            if (circles[i][j] == circles[i - 1][j] and circles[i][j] != 0):
                zeros.append((i, j))
                zeros.append((i - 1, j))
            if (circles[i][j] == circles[i + 1][j] and circles[i][j] != 0):
                zeros.append((i, j))
                zeros.append((i + 1, j))

    zeros = list(set(zeros))

    if (zeros):
        for i in zeros:
            circles[i[0]][i[1]] = 0
    else:
        # 인접수가 없는경우
        sum_temp = 0
        cnt = 0
        for i in range(1, n + 1):
            for j in range(m):
                if (circles[i][j] != 0):
                    sum_temp += circles[i][j]
                    cnt += 1
        try:
            sum_temp = sum_temp / cnt
        except:
            continue

        for i in range(1, n + 1):
            for j in range(m):
                if (circles[i][j] > sum_temp and circles[i][j] != 0):
                    circles[i][j] -= 1
                elif (circles[i][j] < sum_temp and circles[i][j] != 0):
                    circles[i][j] += 1
    # 각 단계별로 원판 상태출력
    '''
    for i in range(1,n+1):
        print(circles[i])
    print()
    '''

ans = 0
for i in range(1, n + 1):
    ans += sum(circles[i])

print(ans)
