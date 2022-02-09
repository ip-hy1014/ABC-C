"""
N-A*B>=1 ならCは一意に定まる
つまり試すのはA*Bだけで良い
N-1 >= A*B になるA*Bの組み合わせが何通りあるかを求める
(N-1)//A がBの上限
"""
n = int(input())
ans = 0
for i in range(1,n+1):
  ans += (n-1)//i
print(ans)