#BOJ 1107
'''
1. 이동하려는 채널의 범위 대로 후보군을 만든다 (0~500,000)
2. 고장난 버튼이 들어가 있는 경우를 후보군에서 뺀다.
3. 남은 후보들 중에 그 차이가 가장 작은 값을 정답으로 한다.
3-1. x에 대한 값 : x(버튼 눌러서 이동수 ) + (x-N) (목표까지 +,-로 이동)
'''

if __name__=="__main__":
    N = int(input())
    m = int(input())
    error_key = list(map(str,input().split()))
    channels=[]
    cur_c = 100
    for i in range(0,1000001):
        isError = True
        for str_i in str(i):
            if(str_i in error_key):
                isError=False
                break
        if isError:
            channels.append(i)

    ans = 987654321
    val = ''
    for i in channels:
        if(abs(i-N)<ans):
            ans = abs(i-N)
            val = str(i)

    res = len(val)+abs(ans)
    res = min(abs(N-cur_c),res)

    print(res)
