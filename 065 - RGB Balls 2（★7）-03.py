# 065 - RGB Balls 2（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_bm
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/065-03.cpp

mod = 998244353

class FFT():
    def primitive_root_constexpr(self,m):
        if m==2:return 1
        if m==167772161:return 3
        if m==469762049:return 3
        if m==754974721:return 11
        if m==998244353:return 3
        divs=[0]*20
        divs[0]=2
        cnt=1
        x=(m-1)//2
        while(x%2==0):x//=2
        i=3
        while(i*i<=x):
            if (x%i==0):
                divs[cnt]=i
                cnt+=1
                while(x%i==0):
                    x//=i
            i+=2
        if x>1:
            divs[cnt]=x
            cnt+=1
        g=2
        while(1):
            ok=True
            for i in range(cnt):
                if pow(g,(m-1)//divs[i],m)==1:
                    ok=False
                    break
            if ok:
                return g
            g+=1
    def bsf(self,x):
        res=0
        while(x%2==0):
            res+=1
            x//=2
        return res
    butterfly_first=True
    butterfly_inv_first=True
    sum_e=[0]*30
    sum_ie=[0]*30
    def __init__(self,MOD):
        self.mod=MOD
        self.g=self.primitive_root_constexpr(self.mod)
    def butterfly(self,a):
        n=len(a)
        h=(n-1).bit_length()
        if self.butterfly_first:
            self.butterfly_first=False
            es=[0]*30
            ies=[0]*30
            cnt2=self.bsf(self.mod-1)
            e=pow(self.g,(self.mod-1)>>cnt2,self.mod)
            ie=pow(e,self.mod-2,self.mod)
            for i in range(cnt2,1,-1):
                es[i-2]=e
                ies[i-2]=ie
                e=(e*e)%self.mod
                ie=(ie*ie)%self.mod
            now=1
            for i in range(cnt2-2):
                self.sum_e[i]=((es[i]*now)%self.mod)
                now*=ies[i]
                now%=self.mod
        for ph in range(1,h+1):
            w=1<<(ph-1)
            p=1<<(h-ph)
            now=1
            for s in range(w):
                offset=s<<(h-ph+1)
                for i in range(p):
                    l=a[i+offset]
                    r=a[i+offset+p]*now
                    r%=self.mod
                    a[i+offset]=l+r
                    a[i+offset]%=self.mod
                    a[i+offset+p]=l-r
                    a[i+offset+p]%=self.mod
                now*=self.sum_e[(~s & -~s).bit_length()-1]
                now%=self.mod
    def butterfly_inv(self,a):
        n=len(a)
        h=(n-1).bit_length()
        if self.butterfly_inv_first:
            self.butterfly_inv_first=False
            es=[0]*30
            ies=[0]*30
            cnt2=self.bsf(self.mod-1)
            e=pow(self.g,(self.mod-1)>>cnt2,self.mod)
            ie=pow(e,self.mod-2,self.mod)
            for i in range(cnt2,1,-1):
                es[i-2]=e
                ies[i-2]=ie
                e=(e*e)%self.mod
                ie=(ie*ie)%self.mod
            now=1
            for i in range(cnt2-2):
                self.sum_ie[i]=((ies[i]*now)%self.mod)
                now*=es[i]
                now%=self.mod
        for ph in range(h,0,-1):
            w=1<<(ph-1)
            p=1<<(h-ph)
            inow=1
            for s in range(w):
                offset=s<<(h-ph+1)
                for i in range(p):
                    l=a[i+offset]
                    r=a[i+offset+p]
                    a[i+offset]=l+r
                    a[i+offset]%=self.mod
                    a[i+offset+p]=(l-r)*inow
                    a[i+offset+p]%=self.mod
                inow*=self.sum_ie[(~s & -~s).bit_length()-1]
                inow%=self.mod
    def convolution(self,a,b):
        n=len(a);m=len(b)
        if not(a) or not(b):
            return []
        if min(n,m)<=40:
            if n<m:
                n,m=m,n
                a,b=b,a
            res=[0]*(n+m-1)
            for i in range(n):
                for j in range(m):
                    res[i+j]+=a[i]*b[j]
                    res[i+j]%=self.mod
            return res
        z=1<<((n+m-2).bit_length())
        a=a+[0]*(z-n)
        b=b+[0]*(z-m)
        self.butterfly(a)
        self.butterfly(b)
        c=[0]*z
        for i in range(z):
            c[i]=(a[i]*b[i])%self.mod
        self.butterfly_inv(c)
        iz=pow(z,self.mod-2,self.mod)
        for i in range(n+m-1):
            c[i]=(c[i]*iz)%self.mod
        return c[:n+m-1]

def ncr(n, r):
    if n < r or r < 0:
        return 0
    return (fact[n] * inv[r] % mod) * inv[n-r] % mod

def init():
    fact[0] = 1
    inv[0] = 1
    for i in range(1,N+1):
        fact[i] = (i * fact[i-1]) % mod
        inv[i] = pow(fact[i], mod - 2, mod) % mod

N = 10**5*5
fact = [0] * (N+1)
inv = [0] * (N+1)
init()

# Step #1. 入力
R,G,B,K = map(int,input().split())
X,Y,Z = map(int,input().split())

# Step #2. 前処理
R_left = K - Y
R_right = R
G_left = K - Z
G_right = G
B_left = K - X
B_right = B
ar = [0] * (R+1)
ag = [0] * (G+1)
ab = [0] * (B+1)
for i in range(R+1):
    ar[i] = ncr(R, i)
for i in range(G+1):
    ag[i] = ncr(G, i)
for i in range(B+1):
    ab[i] = ncr(B, i)

# Step #3. FFT
p1 = [0] * (R+1)
p2 = [0] * (G+1)
p3 = []
for i in range(R_left,R_right+1):
    p1[i] = ar[i]
for i in range(G_left,G_right+1):
    p2[i] = ag[i]
CONV = FFT(mod)
p3 = CONV.convolution(p1, p2)

# Srep #4. 答えを求める
Answer = 0
for i in range(B_left,B_right+1):
    ret1 = 0
    ret2 = ab[i]
    if 0 <= K - i and K - i <= len(p3):
        ret1 = p3[K-i]
    Answer += ret1 * ret2
    Answer %= mod
print(Answer)