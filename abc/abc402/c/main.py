N, M = map(int, input().split())

# 各料理に含まれる食材と、食材 -> 含む料理のリスト
ingredient_to_recipes = [[] for _ in range(N)]  # 食材 i を含む料理のID一覧
cnt = []  # 各料理に含まれる苦手な食材の数（最初はすべて苦手）
for recipe_id in range(M):
    tmp = list(map(int, input().split()))
    K = tmp[0]
    ingredients = [x - 1 for x in tmp[1:]]  # 0-indexed に変換
    cnt.append(K)
    for ing in ingredients:
        ingredient_to_recipes[ing].append(recipe_id)
B = list(map(int, input().split()))
B = [x - 1 for x in B]  # 克服する食材を0-indexedに
ans = 0
res = []
for b in B:
    for recipe_id in ingredient_to_recipes[b]:
        cnt[recipe_id] -= 1
        if cnt[recipe_id] == 0:
            ans += 1
    res.append(ans)
for r in res:
    print(r)
