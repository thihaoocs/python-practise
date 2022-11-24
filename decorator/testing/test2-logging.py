# Practical Example 1 , Logging

def logged(function):
    def warpper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('./decorator/testing/logfile.txt', 'a') as f:
            fname = function.__name__
            print(f'{fname} returned value {value}')
            f.write(f'{fname} returned value {value}\n')
        return value
    return warpper

@logged
def add(x, y):
    return x + y

print(add(19, 2))