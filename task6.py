# з умови задачі, я зрозуміла, що ми не можемо брати одну страву двічі, тобто це як рюкзак, в нас обмежений набір предметів, а не нескінченний

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    global items

    # посортуємо словник у порядку спадання відношення калорій до ціни
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, values in sorted_items:
        if total_cost + values['cost'] <= budget:
            # беремо, якщо вписуємось у бюджет
            chosen_items.append(item)
            total_cost += values['cost']
            total_calories += values['calories']
    
    return chosen_items, total_cost, total_calories

def dynamic_programming(budget):
    global items

    # цього разу в нас буде вже таблиця двовимірна
    n = len(items)
    # де кількість рядків - це кожен з наших айтемів
    # а кількість стовпців - наш бюджет + 1
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    chosen_items = set()

    for i, (item, values) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            if values['cost'] <= j:
                # якщо вписуємось у поточну суму і можемо збільшити калорійність, то оновлюємо таблицю
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-values['cost']] + values['calories'])
            else:
                dp[i][j] = dp[i-1][j]

    total_calories = dp[n][budget]

    i = n
    j = budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            # складна конструкція, бо ми знаємо номер ключа у словнику, але не знаємо саму назву ключа
            chosen_items.add(list(items.keys())[i-1])
            j -= items[list(items.keys())[i-1]]['cost']
        i -= 1

    total_cost = sum(items[item]['cost'] for item in chosen_items)
    return list(chosen_items), total_cost, total_calories

budget = 100

chosen_items, total_cost, total_calories = greedy_algorithm(budget)
print("greedy_algorithm")
print(f"chosen_items: {chosen_items}")
print(f"total_cost: {total_cost}")
print(f"total_calories: {total_calories}")
print()
chosen_items, total_cost, total_calories = dynamic_programming(budget)
print("dynamic_programming")
print(f"chosen_items: {chosen_items}")
print(f"total_cost: {total_cost}")
print(f"total_calories: {total_calories}")

"""
з цікавих спостережень
на прикладі бюджету 100 можемо бачити, що жадібні алгоритми не завжди обирають найефективнішу комбінацію:

greedy_algorithm
chosen_items: ['cola', 'potato', 'pepsi', 'hot-dog']
total_cost: 80
total_calories: 870

dynamic_programming
chosen_items: ['potato', 'pepsi', 'pizza', 'cola']
total_cost: 100
total_calories: 970
"""