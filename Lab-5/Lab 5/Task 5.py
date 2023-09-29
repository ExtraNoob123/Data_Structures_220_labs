# Task 5
# m^n

def power(m, n):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    elif n == 0:
        return 1
    elif n == 1:
        return m
    else:
        return m * power(m, n-1)


print(power(5, 5))
