# 090 - Tenkei90's Last Problem（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_cl
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/090-03.cpp

def check(N, K, A):
    for l in range(N):
        for r in range(l+1,N+1):
            rangemin = min(A[l:r])
            if rangemin * (r - l) > K:
                return False
    return True

N,K = map(int,input().split())
mul = pow(K + 1, N)
ans = 0
for i in range(mul):
    A = [0] * N
    x = i
    for j in range(N):
        A[j] = x % (K + 1)
        x //= (K + 1)
    if check(N, K, A):
        ans += 1
print(ans)