def float_range(start, stop, step=.25):
    current = float(start)
    while current < stop:
        yield current
        current += step
for num in float_range(1,3,1):
    print(f"{num:05.2f}")