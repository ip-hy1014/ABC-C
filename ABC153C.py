n,k = map(int,input().split())
h = sorted(list(map(int,input().split())))[::-1]
s = sum(h[k:])
print(s)