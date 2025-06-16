class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


    def __add__(self, other):
        if isinstance(other, Product):
            new_quantity = self.quantity + other.quantity
            new_price = (self.price + other.price) * 2
            return Product(f"{self.name} + {other.name}", new_quantity, new_price)
        else:
            raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            return self.price
        else:
            raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self.price})"


class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.author = author

    def __str__(self):
        return f"Книга: {self.name}, Автор: {self.author} (Количество: {self.quantity}, Цена: {self.price})"


class Laptop(Product):
    def __init__(self, name: str, quantity: int, price: float, brand: str):
        super().__init__(name, quantity, price)
        self.brand = brand

    def __str__(self):
        return f"Ноутбук: {self.name}, Бренд: {self.brand} (Количество: {self.quantity}, Цена: {self.price})"


try:
    invalid_book = Book("Ошибка наследования", 1, -100, "Автор")
    print(invalid_book)  # Цена -100 пройдет без ошибки!

    # Синтаксическая ошибка в Laptop (код не запустится)
    # laptop = Laptop("Test", 1, 50000, "TestBrand")

except SyntaxError as e:
    print("Синтаксическая ошибка:", e)
except ValueError as e:
    print("Ошибка значения:", e)