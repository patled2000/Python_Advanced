def say_hello():
    print("Hello, World!")


def greet(func):
    print("Good Morning!")
    func()

greet(say_hello)
