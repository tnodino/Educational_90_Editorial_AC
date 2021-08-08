# 048 - I will not drop out（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_av
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/048.cpp

# Step #1. 入力など
N,K = map(int,input().split())
vec = []
for _ in range(N):
    A,B = map(int,input().split())
    vec.append(B)
    vec.append(A - B)

# Step #2. 答えを求める
Answer = 0
vec.sort()
vec.reverse()
for i in range(K):
    Answer += vec[i]

# Step #3. 出力
print(Answer)