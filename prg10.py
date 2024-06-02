import time

def show_time(func):
    def wrapper():
        print("Time before Execution")
        ts = time.time()
        print(ts)
        result = func()
        print("Time after Execution")
        te = time.time()
        print(te)
        print("Time executed: %.2f" % ((te - ts) * 10**6))  # Convert seconds to microseconds
        return result
    return wrapper

@show_time
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Enter a number: "))
fibonacci = fib()
for _ in range(n):
    print(next(fibonacci))
