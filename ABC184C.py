a,b = map(int, input().split())
c,d = map(int, input().split())
if a == c and b == d:
  ans = 0
elif a + b == c + d:
  ans = 1
elif a - b == c - d:
  ans = 1
elif abs(a-c) + abs(b-d) <= 3:
  ans = 1
elif abs(a-c) + abs(b-d) <= 6:
  ans = 2
elif (abs(a-c) + abs(b-d)) % 2 == 0:
  ans = 2
elif abs((a+b) - (c+d)) <= 3:
  ans = 2
elif abs((a-b) - (c-d)) <= 3:
  ans = 2
else:
  ans = 3
print(ans)