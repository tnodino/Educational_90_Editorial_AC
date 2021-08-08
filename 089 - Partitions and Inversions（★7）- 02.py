# 089 - Partitions and Inversions（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ck
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/089-02.cpp

def count_inversions(vec):
    cnt = 0
    for i in range(len(vec)):
        for j in range(i+1,len(vec)):
            if vec[i] > vec[j]:
                cnt += 1
    return cnt

# Step #1. Input
N,K = map(int,input().split())
A = list(map(int,input().split()))

# Step #2. Brute Force
Answer = 0
for i in range(1<<(N-1)):
    vec = []
    flag = True
    for j in range(N):
        vec.append(A[j])
        if j == N - 1 or i & (1 << j) != 0:
            val = count_inversions(vec)
            if val > K:
                flag = False
            vec.clear()
    if flag == True:
        Answer += 1

# Step #3. Output
print(Answer)