# Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print(' display function ran')

# display = decorator_function(display)

@decorator_function
def display_info(name, age):
    print(f' display_info ran with args {name}, {age}')

display()
display_info('Thiha', 24)