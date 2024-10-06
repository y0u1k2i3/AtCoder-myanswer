def main():
    D, G = map(int, input().split())
    p = [0] * 11
    c = [0] * 11
    for i in range(D):
        p[i], c[i] = map(int, input().split())

    ans = float('inf')  # 問題数の最小値を無限大で初期化

    # 全てのパターンをbit全探索する
    for mask in range(1 << D):
        s = 0    # 総合スコア
        num = 0  # 解いた問題数
        rest_max = -1  # 解いていない問題セットの中で一番高得点の問題セット

        # 各問題セットをチェック
        for i in range(D):
            if mask >> i & 1:  # i番目のセットを解いた場合
                s += 100 * (i + 1) * p[i] + c[i]  # i番目の問題セットを全問解く（コンプリートボーナスも加算）
                num += p[i]  # 解いた問題数を更新
            else:
                rest_max = i  # 解いていない問題セットの中で最大得点のものを記録

        # 総合スコアがGに満たない場合
        if s < G:
            # 最大得点セットを一部だけ解いて不足分を補う
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1  # あと何問必要か計算
            if need >= p[rest_max]:  # 必要数がそのセットの問題数を超えた場合は無効
                continue
            num += need  # 必要な問題数を加算

        ans = min(ans, num)  # 最小の問題数を更新

    print(ans)

if __name__ == "__main__":
    main()
