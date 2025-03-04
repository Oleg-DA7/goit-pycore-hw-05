from typing import Callable
import re
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


# Завдання 2
# 
def generator_numbers(text: str):
    temp = re.findall(r'\d+\.\d+', text)    
    result = list(map(float, temp))
    for i in result:
        yield i

def sum_profit(text: str, func: Callable):
    result = 0
    for i in func(text):
        result += i
    return result


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

