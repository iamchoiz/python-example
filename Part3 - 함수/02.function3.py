def add_10(value):

    if value < 10:
        return value
    else:
        result = value + 10
        return result, value

n = add_10(9)
print(n)

n, m = add_10(11)
print(n, m)

n = round(1.5)
print(n)