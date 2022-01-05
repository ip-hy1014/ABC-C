from sys import setrecursionlimit
setrecursionlimit(10 ** 7)
def rec(bag_i: int, all_product: int):
    """bag_i番目の袋からボールを選ぶ"""
    # すべての袋から1つづつボールを選び終わった場合
    if bag_i >= N:
        if all_product == X:
            return 1
        else:
            return 0
    # まだボールを選んでいない袋がある場合
    res = 0
    for a in A[bag_i]:
        res += rec(bag_i + 1, all_product * a)
    return res

N, X = map(int, input().split())
# 入力は数列Aだけ欲しいので、Lは捨てている
A = [list(map(int, input().split()[1:])) for _ in range(N)]
print(rec(0, 1))