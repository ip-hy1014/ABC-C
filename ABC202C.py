from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt_a = Counter(a) #aの値が何回出現するか
ans = 0

for i in c:
  j = i - 1
  k = b[j]
  ans += cnt_a[k]

print(ans)