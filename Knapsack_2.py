from itertools import combinations
import time
import random

def generate(n):
    random_list = []
    for i in range(n):
        random_number = random.randrange(10,100)
        random_list.append(random_number)
    return random_list

#何個のリストを作るか指定する
weights = generate(19)
prices = generate(19)

print('weights :', weights)
print('prices :', prices)

start_time = time.time()

def combination_limit(items, capacity):
    max_price = 0
    best_combination = None

    for r in range(1, len(items) + 1):
        #1からlen(items)個までの組み合わせを調べる
        for combination in combinations(items, r):
            total_weight = sum(item[0] for item in combination)
            total_price = sum(item[1] for item in combination)

            if total_weight <= capacity and total_price > max_price:
                #total_weightが範囲内でtotal_priceが最大値を更新
                max_price = total_price
                best_combination = combination
    
    return best_combination


items = list(zip(weights, prices))


best_combination = combination_limit(items, 190)

accumulate_weight = 0
accumulate_price = 0

print("組み合わせ:")
for item in best_combination:
    print("重さ:", item[0], "価格:", item[1])
    accumulate_weight += item[0]
    accumulate_price += item[1]

print('accumulate_weight', accumulate_weight)
print('accumulate_price', accumulate_price)

end_time = time.time()

print("time: ", end_time - start_time, end = '\n\n')