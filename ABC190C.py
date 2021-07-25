n, m = map(int,input().split())

A = []
B = []
for i in range(m):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

k = int(input())

C = []
D = []
for i in range(k):
    c, d = map(int,input().split())
    C.append(c)
    D.append(d)

ans = 0
for i in range(2 ** k):
    dish = [0] * n
    for j in range(k):
        if (i >> j) & 1:
            dish[D[j]-1] += 1
        else:
            dish[C[j]-1] += 1
    sum_i = 0
    for l in range(m):
        if dish[A[l]-1] > 0 and dish[B[l]-1] > 0:
            sum_i += 1

    if ans < sum_i:
        ans = sum_i
else:
    print(ans)

#別解
def solve():
    from itertools import product

    ans = 0

    # 2^K通りの置き方をbit全探索します
    # productで0か1をK個並べてできる数列を全列挙します
    # ループで (0,0,0), (0,0,1), (0,1,0),(0,1,1)...
    # の要素を1つずつ取りして使います
    for bit in product((0, 1), repeat=K):
        cnt = [0] * (N + 1)  # 各皿のボールの数をカウントします
        for i in range(K):
            # i番目の人がA_i, B_iのどちらか片方にボールを置きます
            # bit[i] == 0ならA_i、bit[i]==1ならばB_iを選びます
            ball = people[i][bit[i]]
            cnt[ball] += 1

        score = 0
        for i in range(M):
            c, d = conditions[i]
            if cnt[c] > 0 and cnt[d] > 0:
                # 条件は皿C, 皿Dの両方にボールが1個以上置かれていることです
                score += 1
        ans = max(ans, score)  # 最大値を更新します
    return ans


N, M = map(int, input().split())

conditions = []
for _ in range(M):
    a, b = map(int, input().split())
    conditions.append((a, b))

people = []
K = int(input())
for _ in range(K):
    c, d = map(int, input().split())
    people.append((c, d))

print(solve())