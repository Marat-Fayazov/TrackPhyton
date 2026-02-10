# TODO Написать 3 класса с документацией и аннотацией типов

class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.

    Пример:
        >>> book = Book("Война и мир", "Лев Толстой", 1869)
        >>> book.title
        'Война и мир'
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Инициализирует объект книги.

        Args:
            title: Название книги (не может быть пустой строкой).
            author: Автор книги (не может быть пустой строкой).
            year: Год издания (должен быть положительным и не превышать текущий год).

        Raises:
            ValueError: Если название или автор - пустая строка,
                       или год издания некорректен.
        """
        if not title or not title.strip():
            raise ValueError("Название книги не может быть пустой строкой")
        if not author or not author.strip():
            raise ValueError("Автор книги не может быть пустой строкой")
        if year <= 0 or year > 2024:  # Предполагаем, что текущий год 2024
            raise ValueError("Год издания должен быть положительным и не превышать текущий год")

        self.title = title.strip()
        self.author = author.strip()
        self.year = year

    def read_page(self, page_number: int) -> str:
        """
        Читает указанную страницу книги.

        Args:
            page_number: Номер страницы (должен быть положительным).

        Returns:
            str: Содержимое страницы.

        Raises:
            ValueError: Если номер страницы не положительный.

        Пример:
            >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
            >>> isinstance(book.read_page(1), str)
            True
        """
        ...

    def get_age(self) -> int:
        """
        Вычисляет возраст книги.

        Returns:
            int: Возраст книги в годах.

        Пример:
            >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 1866)
            >>> book.get_age() >= 150
            True
        """
        ...

    def update_title(self, new_title: str) -> None:
        """
        Обновляет название книги.

        Args:
            new_title: Новое название книги (не может быть пустой строкой).

        Raises:
            ValueError: Если новое название - пустая строка.

        Пример:
            >>> book = Book("Старое название", "Автор", 2000)
            >>> book.update_title("Новое название")
            >>> book.title
            'Новое название'
        """

    class Smartphone:
        """
        Класс, представляющий смартфон.

        Атрибуты:
            brand (str): Бренд смартфона.
            model (str): Модель смартфона.
            battery_level (int): Уровень заряда батареи в процентах.

        Пример:
            >>> phone = Smartphone("Samsung", "Galaxy S23", 85)
            >>> phone.brand
            'Samsung'
            >>> phone.battery_level
            85
        """

        def __init__(self, brand: str, model: str, battery_level: int = 100) -> None:
            """
            Инициализирует объект смартфона.

            Args:
                brand: Бренд смартфона (не может быть пустой строкой).
                model: Модель смартфона (не может быть пустой строкой).
                battery_level: Уровень заряда батареи (должен быть от 0 до 100).

            Raises:
                ValueError: Если бренд или модель - пустая строка,
                           или уровень заряда не в диапазоне 0-100.
            """
            if not brand or not brand.strip():
                raise ValueError("Бренд не может быть пустой строкой")
            if not model or not model.strip():
                raise ValueError("Модель не может быть пустой строкой")
            if not 0 <= battery_level <= 100:
                raise ValueError("Уровень заряда должен быть в диапазоне от 0 до 100")

            self.brand = brand.strip()
            self.model = model.strip()
            self.battery_level = battery_level

            def make_call(self, phone_number: str, duration_minutes: int) -> bool:
                """
                Совершает телефонный звонок.

                Args:
                    phone_number: Номер телефона (не может быть пустой строкой).
                    duration_minutes: Длительность звонка в минутах (должна быть положительной).

                Returns:
                    bool: True если звонок успешно совершен, False если нет.

                Raises:
                    ValueError: Если номер телефона пустой или длительность не положительная.

                Пример:
                    >>> phone = Smartphone("Apple", "iPhone 14", 75)
                    >>> phone.make_call("+79991234567", 5)
                    True
                """
                ...

            def charge(self, charge_percentage: int) -> int:
                """
                Заряжает смартфон.

                Args:
                    charge_percentage: Процент заряда для добавления (должен быть положительным).

                Returns:
                    int: Новый уровень заряда батареи.

                Raises:
                    ValueError: Если процент заряда не положительный.

                Пример:
                    >>> phone = Smartphone("Xiaomi", "Redmi Note", 30)
                    >>> new_level = phone.charge(50)
                    >>> new_level <= 100
                    True
                """
                ...

            def install_app(self, app_name: str, app_size_mb: int) -> bool:
                """
                Устанавливает приложение на смартфон.

                Args:
                    app_name: Название приложения (не может быть пустой строкой).
                    app_size_mb: Размер приложения в мегабайтах (должен быть положительным).

                Returns:
                    bool: True если приложение успешно установлено, False если нет.

                Raises:
                    ValueError: Если название приложения пустое или размер не положительный.

                Пример:
                    >>> phone = Smartphone("Google", "Pixel 7", 60)
                    >>> phone.install_app("WhatsApp", 150)
                    True
                """
                ...

    class BankAccount:
        """
        Класс, представляющий банковский счет.

        Атрибуты:
            account_number (str): Номер счета.
            account_holder (str): Владелец счета.
            balance (float): Текущий баланс счета.

        Пример:
            >>> account = BankAccount("1234567890", "Иван Иванов", 1500.50)
            >>> account.account_number
            '1234567890'
            >>> account.balance
            1500.5
        """

        def __init__(self, account_number: str, account_holder: str,
                     initial_balance: float = 0.0) -> None:
            """
            Инициализирует банковский счет.

            Args:
                account_number: Номер счета (не может быть пустой строкой).
                account_holder: Владелец счета (не может быть пустой строкой).
                initial_balance: Начальный баланс (не может быть отрицательным).

            Raises:
                ValueError: Если номер счета или владелец - пустая строка,
                           или начальный баланс отрицательный.
            """
            if not account_number or not account_number.strip():
                raise ValueError("Номер счета не может быть пустой строкой")
            if not account_holder or not account_holder.strip():
                raise ValueError("Владелец счета не может быть пустой строкой")
            if initial_balance < 0:
                raise ValueError("Начальный баланс не может быть отрицательным")

            self.account_number = account_number.strip()
            self.account_holder = account_holder.strip()
            self.balance = initial_balance

        def deposit(self, amount: float) -> float:
            """
            Пополняет счет на указанную сумму.

            Args:
                amount: Сумма для пополнения (должна быть положительной).

            Returns:
                float: Новый баланс счета после пополнения.

            Raises:
                ValueError: Если сумма пополнения не положительная.

            Пример:
                >>> account = BankAccount("0987654321", "Петр Петров", 1000.0)
                >>> account.deposit(500.0)

1500.0
        """
        ...

    def withdraw(self, amount: float) -> float:
        """
        Снимает деньги со счета.

        Args:
            amount: Сумма для снятия (должна быть положительной).

        Returns:
            float: Новый баланс счета после снятия.

        Raises:
            ValueError: Если сумма снятия не положительная или недостаточно средств.

        Пример:
            >>> account = BankAccount("1122334455", "Мария Сидорова", 2000.0)
            >>> account.withdraw(300.0)
            1700.0
        """
        ...

    def transfer(self, target_account: 'BankAccount', amount: float) -> bool:
        """
        Переводит деньги на другой счет.

        Args:
            target_account: Счет-получатель.
            amount: Сумма перевода (должна быть положительной).

        Returns:
            bool: True если перевод успешно выполнен, False если нет.

        Raises:
            ValueError: Если сумма перевода не положительная или недостаточно средств.

        Пример:
            >>> account1 = BankAccount("111", "Алексей", 1000.0)
            >>> account2 = BankAccount("222", "Ольга", 500.0)
            >>> account1.transfer(account2, 200.0)
            True
            >>> account1.balance
            800.0
        """
        ...

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


if name == "__main__":
    import doctest

    # Тестирование класса Book
    print("Тестирование класса Book:")
    doctest.testmod(extraglobs={'Book': Book}, verbose=True)

    # Тестирование класса Smartphone
    print("\nТестирование класса Smartphone:")
    doctest.testmod(extraglobs={'Smartphone': Smartphone}, verbose=True)

    # Тестирование класса BankAccount
    print("\nТестирование класса BankAccount:")
    doctest.testmod(extraglobs={'BankAccount': BankAccount}, verbose=True)
    try:
        # Успешное создание книги
        book1 = Book("1984", "Джордж Оруэлл", 1949)
        print(f"Создана книга: '{book1.title}' автора {book1.author}")
    except ValueError as e:
        print(f"Ошибка создания книги: {e}")

    try:
        # Неудачное создание книги (некорректный год)
        book2 = Book("Некорректная книга", "Автор", -100)
    except ValueError as e:
        print(f"Ошибка создания книги: {e}")

    try:
        # Успешное создание смартфона
        phone = Smartphone("Apple", "iPhone 15 Pro", 65)
        print(f"Создан смартфон: {phone.brand} {phone.model}")
    except ValueError as e:
        print(f"Ошибка создания смартфона: {e}")

    try:
        # Успешное создание банковского счета
        account = BankAccount("1234-5678-9012-3456", "Сергей Сергеев", 25000.75)
        print(f"Создан банковский счет: {account.account_number}")
    except ValueError as e:
        print(f"Ошибка создания банковского счета: {e}")