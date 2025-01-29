# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
# without permanently modifying it.


def decorator(func):
    def wrapper():
        print("This is printed before function called")
        func()
        print("This is printed after function called")

    return 2


@decorator
def say_hello():
    print("Hello!")
    


say_hello()
