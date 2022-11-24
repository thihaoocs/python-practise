def myDecorator(function):

    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        result = function(*args, **kwargs)
        return result

    return wrapper

@myDecorator
def hello(person):
    print(f"Hello guy")
    return f"Hello {person}!"

print(hello('John'))
