# does not handle division by zero

ceil = lambda n: n if int(n) == n else int(n + 1)
mod = lambda n, d: int(((n / d) - int(n / d) + 0.1) * d)

def pow(x, n):
    if n == 1:
        return x
    else:
        return pow(x, (n + 1) // 2) * pow(x, ceil((n - 1) / 2))

def modPow(x, n, d):
    return mod(pow(2, 3), 3)


# # Example test case
# print(modPow(2,3,3))
