def max_profit(price_list, count):
    table = [0]

    for i in range(1, count + 1):
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        for j in range(1, i // 2 + 1):
            profit = max(profit, table[j] + table[i - j])

        table.append(profit)

    return table


# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
