def decorator_fun(func):
    def wrapper():
        print("before function chalne se pahle....")
        func()
        print("function ke bad bhi kuchh ho rha hai ....")
    return wrapper

def say_hello():
    print("hello , world!")


decorated = decorator_fun(say_hello)
decorated()