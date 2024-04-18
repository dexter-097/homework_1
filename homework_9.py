arr_1 = input('введите элементы списка через пробел: ').split()
arr_2 = input('введите элементы списка через пробел: ').split()

arr_1 += arr_2
new_arr = set(arr_1)
new_arr = list(new_arr)
new_arr.sort()
result_arr = []
for i in range(len(new_arr)):
    result_arr.append(int(new_arr[i]))
print(result_arr)
