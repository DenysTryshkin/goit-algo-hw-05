def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iteration_count = 0 # кількість ітерацій, потрібних для знаходження елемента
    bigger_or_equal = None # Верхня межа — це найменший елемент, який є більшим або рівним заданому значенню.

    while left <= right:
        iteration_count += 1 # Збільшуємо кількість ітерацій на одну
        mid = (left + right) // 2  # Знаходимо середину масиву

        if arr[mid] == target:
            return (iteration_count, arr[mid])  # Якщо знайдено шуканий елемент, повертаємо його індекс
        elif arr[mid] < target:
            left = mid + 1  # Якщо шуканий елемент більший, зміщуємо ліву межу
        else:
            right = mid - 1  # Якщо шуканий елемент менший, зміщуємо праву межу
    
    if left < len(arr):
        bigger_or_equal = arr[left]
    else:
        bigger_or_equal  = "No bigger_or_equal found!"

    return (iteration_count, bigger_or_equal)

# Приклад використання
arr = [4.5, 8,5, 24.6, 54.2, 7.7, 8.8, 23.6]
target = 9
iteration_count, bigger_or_equal = binary_search(arr, target)
print(f"iterations: {iteration_count}, bigger or equal: {bigger_or_equal}")