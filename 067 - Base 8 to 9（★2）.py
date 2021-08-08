# 067 - Base 8 to 9（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_bo
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/067.cpp

def base8_to_long(N):
    res = 0
    for i in range(len(N)):
        res = res * 8 + int(N[i])
    return res

def long_to_base9(N):
    if N == 0:
        return '0'
    res = ''
    while N > 0:
        res = str(N % 9) + res
        N //= 9
    return res

N,K = input().split()
for _ in range(int(K)):
    N = long_to_base9(base8_to_long(N))
    M = ''
    for j in range(len(N)):
        if N[j] == '8':
            M += '5'
        else:
            M += N[j]
    N = M
print(N)