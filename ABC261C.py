from collections import defaultdict
n = int(input())
d = defaultdict(int)
for _ in range(n):
  s = input()
  if not d[s]:
    print(s)
  else:
    print(s+"("+str(d[s])+")")
  d[s]+=1

#別解
#類題 ABC137C
n = int(input())
d = {}
for _ in range(n):
  s = input()
  if s not in d:
    print(s)
    d[s]=0
  else:
    print(s+"("+str(d[s])+")")
  d[s]+=1