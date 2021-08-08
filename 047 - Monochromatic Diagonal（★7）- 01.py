# 047 - Monochromatic Diagonal（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_au
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/047-01.cpp

N = int(input())
S = list(input())
T = list(input())
F = ['' for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i] == T[j]:
            # color: same as S[i] and T[j]
            F[i] += S[i]
        else:
            # color: different from S[i] and T[j]
            F[i] += chr(ord(S[i]) ^ ord(T[j]) ^ ord('R') ^ ord('G') ^ ord('B'))
answer = 0
for i in range(-(N-1),N):
    rcnt = 0
    gcnt = 0
    bcnt = 0
    for r in range(N):
        c = r + i
        if 0 <= c and c < N:
            if F[r][c] == 'R':
                rcnt += 1
            if F[r][c] == 'G':
                gcnt += 1
            if F[r][c] == 'B':
                bcnt += 1
    if rcnt == 0 and gcnt == 0:
        answer += 1
    if gcnt == 0 and bcnt == 0:
        answer += 1
    if bcnt == 0 and rcnt == 0:
        answer += 1
print(answer)