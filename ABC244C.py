n = int(input())
s = set(range(1,2*n+2))
while True:
  print(s.pop(),flush=True)
  m = int(input())
  if m==0:
    break
  s.discard(m)