mpg = float(input())
g = 3.785411784
km = 1.609344
liters_per_100_km = (100 * g) / (mpg * km)

print('{:.6f}'.format(liters_per_100_km))
