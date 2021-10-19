n,k = map(int,input().split())
for _ in range(k):
  n_asc = int(''.join(sorted(str(n))))
  n_desc = int(''.join(sorted(str(n))[::-1]))
  n = n_desc - n_asc
print(n)