import random
import time

random.seed(time.time())

def monte_carlo_simulation(num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_map_of_sums = {}

    for _ in range(num_experiments):
        N = 15000 # всі комбінації
        # Генерація випадкових точок
        points = [(random.randint(1, 6), random.randint(1, 6)) for _ in range(N)]

        map_of_sums = {}
        # Відбір точок, що дають потрібну суму
        for point in points:
            sum = point[0] + point[1]
            if sum not in map_of_sums.keys():
                map_of_sums[sum] = 0
            map_of_sums[sum] += 1

        # Розрахунок таблиці ймовірностей за методом Монте-Карло
        for key, value in map_of_sums.items():
            map_of_sums[key] = value / N
            # Додавання до середніх значень у average_map_of_sums
            if key not in average_map_of_sums:
                average_map_of_sums[key] = 0
            average_map_of_sums[key] += map_of_sums[key]

       
    # Обчислення середніх значень у average_map_of_sums
    for key, value in average_map_of_sums.items():
        average_map_of_sums[key] /= num_experiments
    return average_map_of_sums

# Кількість експериментів
num_experiments = 1000

# Виконання симуляції
average_map_of_sums = monte_carlo_simulation(num_experiments)

print("|{:<5}|{:<11}|".format("Сума", "Імовірність"))
print("-" * 19)
for i in range(2, 13):
    print("|{:<5}|{:<11}|".format(i, str(round(average_map_of_sums[i] * 100, 2)) + "%"))