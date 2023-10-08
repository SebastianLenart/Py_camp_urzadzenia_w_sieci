def moj_range(num):
    i = 0
    out = []
    while i < num:
        out.append(i)
        i += 1
    return out


def lepszy_range(num):
    print("a")
    yield 4
    print("b")
    yield 5
    print("c")

gen = lepszy_range(10)
print(next(gen))
print(next(gen))
print("*" * 15)
for x in lepszy_range(10):
    print(x)

#
#
# x = iter(moj_range(10))
# print(next(x))
# print(next(x))
# print(next(x))
#
#
# for x in moj_range(10):  # duzo pamieci zuzyje dla liczby 1000000
#     print(x)

#-----------------------------------------------------------------------------------------------------------------------

# print("*" * 15)
# class MojGen:
#     def __init__(self, num):
#         self.num = num
#         self.i = 0
#
#     def daj(self):
#         counter = self.i
#         self.i += 1
#         if self.i == self.num:
#             raise Exception
#         return counter
#
#
# moj_gen = MojGen(10)
# print(moj_gen.daj())  # w pamieci jest tylko jedna wartosc(ostatnia) a nie lista poprzednich wszystkich wartosci
# print(moj_gen.daj())
