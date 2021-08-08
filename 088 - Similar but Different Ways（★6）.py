# 088 - Similar but Different Ways（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_cj
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/088.cpp

def dfs(pos, dep):
    global flag
    if flag == True:
        return
    if pos == N:
        Answer[dep].append(list(vec))
        if len(Answer[dep]) == 2:
            flag = True
        return
    # Don't Choose
    dfs(pos + 1, dep)
    # Choose
    if c[pos] == 0:
        vec.append(pos)
        for i in G[pos]:
            c[i] += 1
        dfs(pos + 1, dep + A[pos])
        for i in G[pos]:
            c[i] -= 1
        vec.pop()

# Step #1. Input
N,Q = map(int,input().split())
A = list(map(int,input().split()))
G = [[] for _ in range(N)]
for i in range(Q):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    G[x].append(y)

# Step #2. DFS
Answer = [[] for _ in range(10000)]
c = [0] * 10000
vec = []
flag = False
dfs(0, 0)

# Step #3. Output The Answer
for i in range(10000):
    if len(Answer[i]) <= 1:
        continue
    print(len(Answer[i][0]))
    for j in range(len(Answer[i][0])):
        Answer[i][0][j] += 1
    print(*Answer[i][0])
    print(len(Answer[i][1]))
    for j in range(len(Answer[i][1])):
        Answer[i][1][j] += 1
    print(*Answer[i][1])
    exit()