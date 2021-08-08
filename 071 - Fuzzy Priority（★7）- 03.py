# 071 - Fuzzy Priority（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_bs
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/071-03.cpp

from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(depth):
    if depth == N:
        answer_list.append(list(perm))
        return True
    if not st:
        return False
    for i in range(len(st)-1,-1,-1):
        if len(answer_list) == K:
            break
        x = st[i]
        st.pop(i)
        for j in G[x]:
            deg[j] -= 1
            if deg[j] == 0:
                st.append(j)
        perm[depth] = x
        sign = dfs(depth + 1)
        if not sign:
            return False
        for j in G[x]:
            if deg[j] == 0:
                st.pop(-1)
            deg[j] += 1
        st.insert(i, x)
    return True

N,M,K = map(int,input().split())
G = [[] for _ in range(N)]
deg = [0] * N
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    deg[b] += 1
st = []
perm = [-1] * N
answer_list = []
for i in range(N):
    if deg[i] == 0:
        st.append(i)
dfs(0)
if len(answer_list) != K:
    print(-1)
else:
    for v in range(K):
        for i in range(N):
            answer_list[v][i] += 1
        print(*answer_list[v])