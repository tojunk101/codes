# Calculate the n-th fibonacci number
# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, ....
# Solution O(n)
def fibonacci(n):
    # return -1 (invalid) for input < 0
    if n < 0:
        return -1

    # for input 0 or 1, no need for calculation
    if n == 0 or n == 1:
        return n

    prev = 1
    prev_prev = 0
    fib = None

    count = 2
    while count <= n:
        fib = prev + prev_prev
        prev_prev = prev
        prev = fib
        count += 1
    return fib

print ("Fibonacci 10: %d" % (fibonacci(10)))
print ("Fibonacci 4 : %d" % (fibonacci(4)))
print ("Fibonacci -3: %d" % (fibonacci(-3)))
print ("Fibonacci 0 : %d" % (fibonacci(0)))
