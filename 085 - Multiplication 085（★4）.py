# 085 - Multiplication 085（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_cg
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/085.cpp

# Step #1. Input
K = int(input())

# Step #2. Enumerate Divisors
vec = []
for i in range(1,K+1):
    if i * i > K:
        break
    if K % i != 0:
        continue
    vec.append(i)
    if i != K // i:
        vec.append(K // i)
vec.sort()

# Step #3. Brute Force
Answer = 0
for i in range(len(vec)):
    for j in range(i,len(vec)):
        a = vec[i]
        b = vec[j]
        c = 0
        if K // a < b:
            continue
        if K % (a * b) != 0:
            continue
        c = K // (vec[i] * vec[j])
        if b <= c:
            Answer += 1

# Step #4. Output
print(Answer)