def decorator_func(func):
    def wrapper():
        print("before function...")
        func()
        print("After function...")
    return wrapper

@decorator_func
def say_hello():
    print("hello , world!")

say_hello()