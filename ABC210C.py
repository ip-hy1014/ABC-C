"""
キャンディの色は最大で 10^9 種類あります。長さが 10^9 のリストで管理しようとすると、MLE（メモリ上限超過）になります。

そこで、collections モジュールのCounter を使います。存在する要素だけを管理できるので、メモリの問題はなくなります。

さらに、len(counter) で、含まれているKeyの数（≒種類数）を O(1) で求めることができます。
ただし、ある色のキャンディの個数が 0 個でも、Keyとして含まれていれば len(counter) で数えられてしまいます。
個数が 0 個になった色のキャンディーはdelを使って削除する必要があります。
"""
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