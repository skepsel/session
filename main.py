from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Product(AbstractProduct):
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self._price = None  # Initialize private price attribute
        self.set_price(price)  # Use setter to validate price

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Цена не может быть меньше нуля!")
        self._price = new_price

    def __add__(self, other):
        if isinstance(other, Product):
            new_quantity = self.quantity + other.quantity
            # Calculate weighted average price
            total_price = (self._price * self.quantity + other._price * other.quantity)
            new_price = total_price / new_quantity if new_quantity > 0 else 0
            return Product(f"{self.name} + {other.name}", new_quantity, new_price)
        raise TypeError("Можно складывать только объекты Product")

    def __lt__(self, other):
        if isinstance(other, Product):
            return self._price < other._price
        raise TypeError("Можно сравнивать только объекты Product")

    def __gt__(self, other):
        if isinstance(other, Product):
            return self._price > other._price
        raise TypeError("Можно сравнивать только объекты Product")

    def __str__(self):
        return f"{self.name} (Количество: {self.quantity}, Цена: {self._price})"

    def get_description(self) -> str:
        return f"Продукт: {self.name}"


class Book(Product):
    def __init__(self, name: str, quantity: int, price: float, author: str):
        super().__init__(name, quantity, price)
        self.author = author

    def __str__(self):
        return f"Книга: {self.name}, Автор: {self.author} (Количество: {self.quantity}, Цена: {self._price})"

    def get_description(self) -> str:
        return f"Книга: {self.name}, Автор: {self.author}"


class Laptop(Product):
    def __init__(self, name: str, quantity: int, price: float, brand: str):
        super().__init__(name, quantity, price)
        self.brand = brand

    def __str__(self):
        return f"Ноутбук: {self.name}, Бренд: {self.brand} (Количество: {self.quantity}, Цена: {self._price})"

    def get_description(self) -> str:
        return f"Ноутбук: {self.name}, Бренд: {self.brand}"


# Test the implementation
try:
    book1 = Book("Война и мир", 5, 500, "Лев Толстой")
    book2 = Book("Преступление и наказание", 3, 450, "Фёдор Достоевский")
    laptop = Laptop("Test", 1, 50000, "TestBrand")

    # Test task1 requirements
    print(book1 + book2)  # Война и мир + Преступление и наказание (Количество: 8, Цена: 481.25)
    print(book1 > book2)  # True
    print(book1 < book2)  # False

    # Test task2 requirements
    print(book1.get_description())  # Книга: Война и мир, Автор: Лев Толстой
    print(laptop.get_description())  # Ноутбук: Test, Бренд: TestBrand

    # Test task3 requirements
    print(book1.get_price())  # 500
    book1.set_price(600)  # Update price
    print(book1.get_price())  # 600

    # Test negative price
    invalid_book = Book("Ошибка", 1, -100, "Автор")  # Should raise ValueError

except ValueError as e:
    print("Ошибка значения:", e)
except SyntaxError as e:
    print("Синтаксическая ошибка:", e)
