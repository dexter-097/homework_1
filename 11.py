arr = input('введите элементы списка через пробел: ').split()


def uniqueness(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
                if count > 1:
                    return False
    return True


result = uniqueness(arr)
if result:
    print('Все уникальны')
else:
    print('Не уникальны')
