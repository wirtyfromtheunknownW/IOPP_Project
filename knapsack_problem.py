def knapsack(capacity, weights, values, n):
    # Създаваме таблица за динамично програмиране
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Попълване на таблицата
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:  # Проверка дали предметът може да се включи
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    # Намиране на включените предмети
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)
            w -= weights[i-1]

    selected_items.reverse()
    return dp[n][capacity], selected_items

# Входни данни
capacity = 100
weights = [4, 8, 11, 16, 16, 20]
values = [7, 10, 12, 15, 27, 34]
n = len(weights)

# Решаване на задачата
max_value, selected_items = knapsack(capacity, weights, values, n)

# Извеждане на резултата
print(f"Максимална стойност: {max_value}")
print(f"Избрани предмети: {selected_items}")
