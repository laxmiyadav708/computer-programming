def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

stats = get_stats([1, 2, 3, 4, 5])
print(stats)  # Output: (15, 5, 3.0)
