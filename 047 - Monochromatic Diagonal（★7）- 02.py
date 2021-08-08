# 047 - Monochromatic Diagonal（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_au
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/047-02.cpp

mod = 699999953

N = int(input())
S = list(input())
T = list(input())
seq1 = [0] * N
seq3 = [0] * N
for i in range(N):
    seq1[i] = 0 if S[i] == 'R' else (1 if S[i] == 'G' else 2)
    seq3[i] = 0 if T[i] == 'R' else (1 if T[i] == 'G' else 2)
answer = 0
for i in range(3):
    seq2 = [0] * N
    for j in range(N):
        seq2[j] = (i - seq3[j] + 3) % 3
    power3 = 1
    hash1 = 0
    hash2 = 0
    for j in range(N):
        hash1 = (hash1 * 3 + seq1[j]) % mod
        hash2 = (hash2 + power3 * seq2[N-j-1]) % mod
        if hash1 == hash2:
            answer += 1
        power3 = power3 * 3 % mod
    power3 = 1
    hash1 = 0
    hash2 = 0
    for j in range(N-1):
        hash1 = (hash1 + power3 * seq1[N-j-1]) % mod
        hash2 = (hash2 * 3 + seq2[j]) % mod
        if hash1 == hash2:
            answer += 1
        power3 = power3 * 3 % mod
print(answer)