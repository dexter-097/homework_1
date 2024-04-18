numbers = input('введите числа через запятую: ')
result_1 = numbers.split(', ')
result_2 = tuple(result_1)

new_arr_1 = []
for i in range(len(result_1)):
    new_arr_1.append(int(result_1[i]))
print(new_arr_1)

new_arr_2 = []
for i in range(len(result_2)):
    new_arr_2.append(int(result_2[i]))
print(new_arr_2)
