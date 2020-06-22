#BOJ 4153
'''
1. 3개의 변중 가장 긴 변 찾기
2. 나머지 변과 긴변에 대한 피타고라스 방정식 판별
'''

while(True):
    a,b,c = map(int,input().split())
    if(a==0 and b ==0 and c==0):
        break
    long_side = max(a,b,c)
    if(long_side==a):
        side_1 = b
        side_2 = c
    elif(long_side==b):
        side_1=a
        side_2=c
    else:
        side_1=a
        side_2=b

    if(long_side**2 == (side_1**2)+side_2**2):
        print('right')
    else:
        print('wrong')
