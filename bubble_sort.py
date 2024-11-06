# Сортировка пузырьком (Bubble Sort)

def bubble_sort(arr):
    n = len(arr)  # Получаем длину списка
    # Внешний цикл для прохода по всем элементам списка
    for i in range(n):
        # Внутренний цикл проходит по неотсортированной части списка
        for j in range(0, n - i - 1):  # На каждой итерации количество проверяемых элементов уменьшается
            # Сравниваем соседние элементы и меняем их местами, если они в неправильном порядке
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Меняем местами arr[j] и arr[j+1]
    return arr

# Пример использования
numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))  # Вывод: [11, 12, 22, 25, 34, 64, 90]