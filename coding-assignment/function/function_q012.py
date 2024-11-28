def decorator_function(func):
    def wrapper():
        print("Function is being called")
        func()
        print("Function has been called")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
