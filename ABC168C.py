import math
a,b,h,m = map(int,input().split())
h_r = 30*h
m_r = 0.5*m
r = h_r + m_r - 6*m #角度
if r > 180:
  r = 360-r
ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(r)))
print(ans)