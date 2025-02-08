import itertools

L, R = map(int, input().split())

def calc_sneak_num(num):
    num_list = list(str(num))
    top_digit_num = int(num_list[0])
    ans = 0
    for digit in range(2, len(num_list) + 1):
        for i in range(1, 10):
            if digit < len(num_list):
                ans += i ** (digit - 1)
            else:
                if i < top_digit_num:
                    ans += i ** (digit - 1)
                elif i == top_digit_num:
                    nums_list = [str(i) for i in range(i)]
                    nums_comb_list = list(itertools.product(nums_list, repeat=digit - 1))
                    ans += len(nums_comb_list)
                    for nums_comb in nums_comb_list:
                        num = str(i) + "".join(map(str, nums_comb))
                        if int(num) < L:
                            ans -= 1
                else:
                    continue

print(calc_sneak_num(R) - calc_sneak_num(L - 1))