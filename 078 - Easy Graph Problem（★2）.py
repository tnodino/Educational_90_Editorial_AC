# 078 - Easy Graph Problem（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_bz
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/078.cpp

N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
answer = 0
for i in range(N):
    cnt = 0
    for j in G[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        answer += 1
print(answer)