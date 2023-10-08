def lepszy_range(num):
    i = 0
    while i < num:
        print("a")
        yield i
        i += 1
        print("b")


for x in lepszy_range(10):
    print(x)