def myDecorator(function):

    def wrapper():
        print("I am decorating your function!")
        function()
    return wrapper

def hello_world():
    print("Hello World!")

# fun = myDecorator(hello_world)
# fun()

myDecorator(hello_world)()