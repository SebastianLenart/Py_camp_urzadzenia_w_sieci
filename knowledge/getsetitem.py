class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.dynamic = {}

    def __setitem__(self, key, index):  # dodawanie wartosci slownika do klasy
        print("setitem", "key: ", key, "index: ", index)
        self.dynamic[key] = index

    def __getitem__(self, index):
        print("getitem index: ", index)
        if index in self.dynamic:
            return self.dynamic[index]
        return getattr(self, index)


book = Book("Adam Mickiewicz", "Ogniem i Mieczem")
print(book.author)
book["id"] = 1  # setitem
print(book.dynamic)
# print(book.test)

print(book["author"])  # getitem
# print(book["test"])
print("*" * 15)


class Queue:
    def __init__(self, items):
        self.elements = items

    def __getitem__(self, key):
        self.elements.sort()
        return self.elements[key]

    def add(self, item):
        self.elements.append(item)


queue = Queue(["Zbyszel", "Adam", "Wojtek", "Kacper"])
queue.add("Zenek")
print(queue[0])
print(queue[-1])
