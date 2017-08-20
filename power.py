# 10^3 = 1000
# 2^5  = 32
# Complexity: O(log m) => m = exp
def power(base, exp):
    result = 1
    while (exp):
        if (exp  & 1):
            result *= base
        exp >>= 1
        base *= base
    return result

print "Power of 10^3: %d" % power(10, 3)
print "Power if 2^5:  %d" % power(2, 5)
