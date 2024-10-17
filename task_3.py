import timeit

# Функція для пошуку підрядка за алгоритмом Бойера-Мура
def boyer_moore(text, pattern):
    m = len(pattern)  # Довжина патерну
    n = len(text)     # Довжина тексту
    if m == 0:
        return 0      # Якщо патерн порожній, повертаємо 0
    bad_char = {}     # Словник для запам'ятовування останніх індексів символів патерну
    for i in range(m):
        bad_char[pattern[i]] = i  # Заповнюємо словник

    s = 0  # Зсув для порівняння
    while s <= n - m:
        j = m - 1  # Починаємо з кінця патерну
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1  # Порівнюємо символи патерну та тексту
        if j < 0:
            return s  # Патерн знайдено
        else:
            # Зсув згідно з останнім індексом символу
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1  # Якщо патерн не знайдено


# Функція для пошуку підрядка за алгоритмом Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    # Функція для обчислення масиву LPS (Longest Prefix Suffix)
    def compute_lps(pattern):
        lps = [0] * len(pattern)  # Ініціалізуємо масив LPS
        length = 0  # Довжина попереднього найдовшого префікса
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length  # Зберігаємо довжину
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]  # Зменшуємо довжину
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)  # Обчислюємо масив LPS
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j  # Патерн знайдено
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Використовуємо LPS для зменшення зсуву
            else:
                i += 1
    return -1  # Якщо патерн не знайдено


# Функція для пошуку підрядка за алгоритмом Рабіна-Карпа
def rabin_karp(text, pattern, q=101):
    d = 256  # Кількість символів у вхідному алфавіті
    m = len(pattern)
    n = len(text)
    p = 0  # Хеш значення патерну
    t = 0  # Хеш значення тексту
    h = 1  # Значення для зсуву
    for i in range(m - 1):
        h = (h * d) % q  # Обчислюємо значення h
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q  # Обчислюємо хеш патерну
        t = (d * t + ord(text[i])) % q  # Обчислюємо хеш тексту
    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i  # Патерн знайдено
        if i < n - m:
            # Оновлюємо хеш тексту
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1  # Якщо патерн не знайдено


# Патерни для пошуку
pattern_exist = "структури даних"
pattern_non_exist = "вигаданий підрядок"

# Зчитування текстів з файлів
text_1 = open("article_1.txt", "r", encoding="utf-8").read()
text_2 = open("article_2.txt", "r", encoding="utf-8").read()

# Функція для вимірювання часу виконання алгоритму
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=10)

# Вимірювання часу для кожного алгоритму та патерна
time_bm_1_exist = measure_time(boyer_moore, text_1, pattern_exist)
time_bm_1_non_exist = measure_time(boyer_moore, text_1, pattern_non_exist)

time_kmp_1_exist = measure_time(knuth_morris_pratt, text_1, pattern_exist)
time_kmp_1_non_exist = measure_time(knuth_morris_pratt, text_1, pattern_non_exist)

time_rk_1_exist = measure_time(rabin_karp, text_1, pattern_exist)
time_rk_1_non_exist = measure_time(rabin_karp, text_1, pattern_non_exist)

time_bm_2_exist = measure_time(boyer_moore, text_2, pattern_exist)
time_bm_2_non_exist = measure_time(boyer_moore, text_2, pattern_non_exist)

time_kmp_2_exist = measure_time(knuth_morris_pratt, text_2, pattern_exist)
time_kmp_2_non_exist = measure_time(knuth_morris_pratt, text_2, pattern_non_exist)

time_rk_2_exist = measure_time(rabin_karp, text_2, pattern_exist)
time_rk_2_non_exist = measure_time(rabin_karp, text_2, pattern_non_exist)

# Зберігаємо результати в словнику
results = {
    "Article_1": {
        "Exist": {
            "Boyer-Moore": time_bm_1_exist,
            "Knuth-Morris-Pratt": time_kmp_1_exist,
            "Rabin-Karp": time_rk_1_exist,
        },
        "Non-Exist": {
            "Boyer-Moore": time_bm_1_non_exist,
            "Knuth-Morris-Pratt": time_kmp_1_non_exist,
            "Rabin-Karp": time_rk_1_non_exist,
        },
    },
    "Article_2": {
        "Exist": {
            "Boyer-Moore": time_bm_2_exist,
            "Knuth-Morris-Pratt": time_kmp_2_exist,
            "Rabin-Karp": time_rk_2_exist,
        },
        "Non-Exist": {
            "Boyer-Moore": time_bm_2_non_exist,
            "Knuth-Morris-Pratt": time_kmp_2_non_exist,
            "Rabin-Karp": time_rk_2_non_exist,
        },
    },
}

# Функція для виведення результатів
def print_results(results):
    for article, types in results.items():
        print(f"{article}:")
        for result_type, algorithms in types.items():
            print(f"  {result_type}:")
            for algo, time in algorithms.items():
                print(f"- {algo}: {time:.6f} seconds")
        print()
# Виводимо результати
print_results(results)