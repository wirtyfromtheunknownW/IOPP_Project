# IOPP_Project

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
capacity = 35
weights = [4, 8, 11, 16, 16, 20]
values = [7, 10, 12, 15, 27, 34]
n = len(weights)

# Решаване на задачата
max_value, selected_items = knapsack(capacity, weights, values, n)

# Извеждане на резултата
print(f"Максимална стойност: {max_value}")
print(f"Избрани предмети: {selected_items}")

# README
"""
# Knapsack Problem Solution

## Описание
Това е програма, която решава класическия проблем за раницата с динамично програмиране. Целта е да се максимизира стойността на предметите включени в раница при ограничен капацитет.

## Входни данни
- `capacity` (цяло число): Капацитет на раницата.
- `weights` (списък): Списък с теглата на предметите.
- `values` (списък): Списък със стойностите на предметите.

## Изходни данни
- `max_value`: Максималната стойност на предметите.
- `selected_items`: Списък с предметите, включени в раницата.

## Пример за изпълнение
```python
capacity = 35
weights = [4, 8, 11, 16, 16, 20]
values = [7, 10, 12, 15, 27, 34]
n = len(weights)

max_value, selected_items = knapsack(capacity, weights, values, n)
print(f"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u043d\u0430 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442: {max_value}")
print(f"\u0418\u0437\u0431\u0440\u0430\u043d\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0438: {selected_items}")
```
