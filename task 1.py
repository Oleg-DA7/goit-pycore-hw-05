# Завдання 1
# Ряд Фібоначчі

def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:              # if already calculated 
            return cache[n]
        if n <= 0:                  # 1st element
            return 0
        if n == 1:                  # 2nd element
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(f'{n} - {cache[n]}')
        return cache[n]
    return fibonacci

f1 = caching_fibonacci()
print(f1(5))

