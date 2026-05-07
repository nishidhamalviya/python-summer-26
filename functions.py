def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

tuples = [(1,'one'), (2,'two'),(3,'three')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

numbers = [10, 20, 30, 40, 50]
doubled_numbers = list(map(lambda x:x * 2, numbers))
large_numbers = list(filter(lambda x:x > 25, numbers))

print(doubled_numbers)
print(large_numbers)