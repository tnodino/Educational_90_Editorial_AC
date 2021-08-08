# 032 - AtCoder Ekiden（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_af
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/032.cpp

from itertools import permutations
INF = 1<<30

# Step #1. Input
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

# Step #2. Init
M = int(input())
kenaku = [[False] * N for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    kenaku[x][y] = True
    kenaku[y][x] = True

# Step #3. Brute Force
Answer = INF
for vec in permutations([i for i in range(N)],N):
    flag = True
    Sum = 0
    for i in range(N-1):
        if kenaku[vec[i]][vec[i+1]] == True:
            flag = False
    for i in range(N):
        Sum += A[vec[i]][i]
    if flag == True:
        Answer = min(Answer, Sum)

# Step #4. Output The Answer
if Answer == INF:
    Answer = -1
print(Answer)