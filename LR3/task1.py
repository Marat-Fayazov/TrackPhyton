class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        """Свойство только для чтения"""
        return self._name

    @property
    def author(self):
        """Свойство только для чтения"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Количество страниц должно быть целым числом, получено {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"Количество страниц должно быть положительным, получено {value}")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Продолжительность должна быть числом, получено {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"Продолжительность должна быть положительной, получено {value}")
        self._duration = float(value)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
