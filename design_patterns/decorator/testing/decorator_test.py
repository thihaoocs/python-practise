import time

def timeis(func):
    def wrap(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()

        print(func.__name__, end - start)
        return result
    return wrap

# countdown = timeis(countdown)
@timeis
def countdown(n):
    while n > 0:
        n -= 1

countdown(5)
countdown(1000)