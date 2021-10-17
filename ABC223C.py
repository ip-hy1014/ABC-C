#Ai/Biの総和の2分の1が2つの火がぶつかる時間
#上記時間において左の火がどこに到達しているかを求める
n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
s = 0
for a,b in ab:
  s += a/b #総和
t = s/2 #火がぶつかる時間
ans = 0
for a,b in ab:
  ans += min(a,t*b)
  t -= min(a/b,t)
print(ans)