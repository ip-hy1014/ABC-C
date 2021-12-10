from collections import Counter
N, K = map(int, input().split())
C = list(map(int, input().split()))
cnt = Counter(C[:K])  # 最初のK個
ans = len(cnt)  # 最初のK個の種類数
for i in range(K, N):
  left = C[i - K]  #  1回目が K - K = 0（一番左）になるようにする
  right = C[i]
  cnt[left] -= 1
  cnt[right] += 1
  if cnt[left] == 0:
      del cnt[left]  # 0個でもlenで数えられてしまうためdelで消す
  ans = max(ans, len(cnt))  # 現在の種類数で答えを更新
print(ans)
