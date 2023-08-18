from itertools import combinations
import time

# 各宝石の重さと価格
weights = [13, 23, 27, 33, 41, 45, 58, 60]
prices = [15, 30, 40, 60, 70, 80, 85, 90]


start_time = time.time()

def combination_limit(items, capacity):
    max_price = 0
    best_combination = None

    for r in range(1, len(items) + 1):
        for combination in combinations(items, r):
            total_weight = sum(item[0] for item in combination)
            total_price = sum(item[1] for item in combination)

            if total_weight <= capacity and total_price > max_price:
                max_price = total_price
                best_combination = combination
    
    return best_combination


items = list(zip(weights, prices))


best_combination = combination_limit(items, 190)

accumulate_weight = 0


print("組み合わせ:")
for item in best_combination:
    print("重さ:", item[0], "価格:", item[1])
    accumulate_weight += item[0]

print('accumulate_weight', accumulate_weight)

end_time = time.time()

print("time: ", end_time - start_time)