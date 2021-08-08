# 077 - Planes on a 2D Plane（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_by
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/077-01.cpp

def check(R, S):
    R.sort()
    S.sort()
    if R == S:
        return True
    return False

# Step #1. Input
N,T = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(N)]
AX,AY = [list(i) for i in zip(*_L)]
_L = [list(map(int,input().split())) for _ in range(N)]
BX,BY = [list(i) for i in zip(*_L)]
assert(N <= 6)

# Step #2. Bit Zentansaku
dx = [ 1, 1, 0,-1,-1,-1, 0, 1]
dy = [ 0, 1, 1, 1, 0,-1,-1,-1]
power8 = [0] * (N+1)
power8[0] = 1
for i in range(1,N+1):
    power8[i] = 8 * power8[i-1]
for i in range(power8[N]):
    bit = [0] * (N+1)
    for j in range(N):
        bit[j+1] = (i // power8[j]) % 8
    R,S = [],[]
    for j in range(N):
        p = AX[j] + dx[bit[j+1]] * T
        q = AY[j] + dy[bit[j+1]] * T
        S.append((p, q))
        R.append((BX[j], BY[j]))
    if check(R, S) == True:
        print('Yes')
        for j in range(1,N+1):
            bit[j] += 1
        print(*bit[1:N+1])
        exit()
print('No')