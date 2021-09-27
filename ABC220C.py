"""
AのN要素を何回使うか考える．
これはAの総和をSとすると,x//s
Aの一部をどこまで使うかxを超えるかforループで回す
"""
n = int(input())
a = list(map(int,input().split()))
x = int(input())
s = 0 #現在の総和
ans = 0 #現在の項数
sa = sum(a)
c = x//sa
ans += c*n
s += c*sa
for i in a:
  s+=i
  ans+=1
  if s>x:
    break
print(ans)