a = {"first_name": "Kacper"}
b = {"last_name": "Lenart"}

# przed python 3.9
together = {**a, **b}
print(together)

# python 3.9
together2 = a | b
print(together2)