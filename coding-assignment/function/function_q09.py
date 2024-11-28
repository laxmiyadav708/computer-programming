def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x**2, 5)
print(result)  # Output: 25
