from itertools import combinations

lst = list(range(1,11))
#lst = ['A','B','C','D','E','F','G','H','I','J']

#10人を6人と4人で分ける
comb = combinations(lst, 6)
comb_list = list(comb)
not_in_comb_list = [[] for _ in range(len(comb_list))] #210個のリストを持つリストを生成



for i in range(len(comb_list)):
    comb_list[i] = list(comb_list[i]) #タプルのリスト化
    not_in_comb_list[i] = list(item for item in lst if item not in comb_list[i])
    print('6人のリスト:',comb_list[i],' 4人のリスト:', not_in_comb_list[i], '\n')

    #6人を3人と3人で分ける
    comb_comb = combinations(comb_list[i], 3)
    comb_comb_list = list(comb_comb)
    not_in_2comb_list = [[] for _ in range(len(comb_comb_list))]


    for j in range(len(comb_comb_list) // 2):
        comb_comb_list[j] = list(comb_comb_list[j]) #タプルのリスト化
        not_in_2comb_list[j] = list(item for item in comb_list[i] 
                                    if item not in comb_comb_list[j])

        print('4人のリスト:', not_in_comb_list[i], end=' ')
        print('3人のリスト:',comb_comb_list[j], end=' ')
        print('残り3人のリスト:', not_in_2comb_list[j], end=' ')

        print(f'最初の組合せ {i+1} * 2度目の組み合わせ {j+1} = { (i+1)*(j+1) }')
    print('\n')

print('comb_listの個数:', len(comb_list))
print('comb_comb_listの個数:', len(comb_comb_list))