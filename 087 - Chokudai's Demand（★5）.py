# 087 - Chokudai's Demand（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_ci
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/087.cpp

INF = 10**10

def count_number(lens):
    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                dist[i][j] = lens
            if A[i][j] != -1:
                dist[i][j] = A[i][j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if dist[i][j] <= P:
                cnt += 1
    return cnt

def get_border(cnts):
    cl = 1
    cr = INF
    minx = INF
    for _ in range(40):
        cm = (cl + cr) // 2
        res = count_number(cm)
        if res <= cnts:
            cr = cm
            minx = min(minx, cm)
        else:
            cl = cm
    return minx

N,P,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
L = get_border(K)
R = get_border(K - 1)
if R - L >= INF // 5:
    print('Infinity')
else:
    print(R - L)