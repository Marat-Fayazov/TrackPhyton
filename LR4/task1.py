class Vehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, brand: str, model: str, year: int, price: float) -> None:
        """
        Конструктор базового класса.

        Args:
            brand: Марка транспортного средства
            model: Модель
            year: Год выпуска
            price: Цена в долларах
        """
        self._brand = brand  # Непубличный атрибут (инкапсуляция)
        self._model = model  # Защита от прямого изменения
        self.year = year  # Публичный атрибут
        self.price = price  # Публичный атрибут

    @property
    def brand(self) -> str:
        """Геттер для марки (только для чтения)."""
        return self._brand

    @property
    def model(self) -> str:
        """Геттер для модели (только для чтения)."""
        return self._model

    def start_engine(self) -> str:
        """
        Запуск двигателя.

        Returns:
            Сообщение о запуске двигателя
        """
        return f"Двигатель {self._brand} {self._model} запущен"

    def stop_engine(self) -> str:
        """
        Остановка двигателя.

        Returns:
            Сообщение об остановке двигателя
        """
        return f"Двигатель {self._brand} {self._model} остановлен"

    def __str__(self) -> str:
        """Пользовательское строковое представление."""
        return f"{self._brand} {self._model} ({self.year} год) - ${self.price}"

    def __repr__(self) -> str:
        """Техническое строковое представление для разработчиков."""
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self.year}, price={self.price})"


class Car(Vehicle):
    """Дочерний класс для легковых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, price: float,
                 doors: int, fuel_type: str, has_sunroof: bool = False) -> None:
        """
        Конструктор дочернего класса (расширяет базовый).

        Args:
            brand: Марка автомобиля
            model: Модель
            year: Год выпуска
            price: Цена
            doors: Количество дверей
            fuel_type: Тип топлива (бензин, дизель, электро)
            has_sunroof: Наличие люка на крыше
        """
        # Расширение конструктора базового класса
        super().__init__(brand, model, year, price)
        self.doors = doors
        self.fuel_type = fuel_type
        self._has_sunroof = has_sunroof  # Непубличный атрибут

    @property
    def has_sunroof(self) -> bool:
        """Геттер для наличия люка (только для чтения)."""
        return self._has_sunroof

    def open_sunroof(self) -> str:
        """
        Открыть люк на крыше (только если он есть).

        Returns:
            Сообщение о результате операции
        """
        if self._has_sunroof:
            return f"Люк на {self.brand} {self.model} открыт"
        return f"У {self.brand} {self.model} нет люка"

    # Наследование метода start_engine (без переопределения)
    # Он будет работать как в базовом классе

    def stop_engine(self) -> str:
        """
        Остановка двигателя (перегруженный метод).

        Причина перегрузки: У легковых автомобилей есть дополнительная логика
        - проверка, что автомобиль припаркован
        - блокировка дверей после остановки
        - выключение музыки/кондиционера

        Returns:
            Сообщение об остановке с дополнительными действиями
        """
        # В реальной реализации здесь была бы сложная логика
        base_message = super().stop_engine()
        return f"{base_message}. Двери заблокированы, кондиционер выключен"

    def __str__(self) -> str:
        """
        Перегрузка строкового представления.

Причина: Для легкового автомобиля важно показывать
        количество дверей и тип топлива.
        """
        base_str = super().__str__()
        return f"{base_str} | Легковой, {self.doors} двери, топливо: {self.fuel_type}"

    def __repr__(self) -> str:
        """
        Перегрузка технического представления.

        Причина: В дочернем классе добавились новые атрибуты (doors, fuel_type),
        которые важны для воссоздания объекта.
        """
        return (f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"price={self.price}, doors={self.doors}, fuel_type='{self.fuel_type}', "
                f"has_sunroof={self._has_sunroof})")


class Truck(Vehicle):
    """Дочерний класс для грузовых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, price: float,
                 load_capacity: float, num_axles: int) -> None:
        """
        Конструктор грузового автомобиля.

        Args:
            brand: Марка
            model: Модель
            year: Год выпуска
            price: Цена
            load_capacity: Грузоподъемность (тонн)
            num_axles: Количество осей
        """
        super().__init__(brand, model, year, price)
        self.load_capacity = load_capacity
        self.num_axles = num_axles
        self._current_load: float = 0.0  # Непубличный атрибут - текущая загрузка

    def load_cargo(self, weight: float) -> str:
        """
        Загрузить груз.

        Args:
            weight: Вес груза в тоннах

        Returns:
            Сообщение о результате загрузки
        """
        if self._current_load + weight <= self.load_capacity:
            self._current_load += weight
            return f"Загружено {weight} тонн. Текущая загрузка: {self._current_load} тонн"
        return f"Превышение грузоподъемности! Максимум: {self.load_capacity} тонн"

    # Наследование метода start_engine (без изменений)

    def stop_engine(self) -> str:
        """
        Остановка двигателя (перегруженный метод).

        Причина перегрузки: Для грузовиков критично проверить,
        что пневматическая тормозная система заблокирована
        и груз зафиксирован перед остановкой двигателя.

        Returns:
            Сообщение об остановке с проверками
        """
        # В реальности здесь была бы проверка фиксации груза
        base_message = super().stop_engine()
        return f"{base_message}. Пневмотормоза активированы, груз зафиксирован"

    def __str__(self) -> str:
        """
        Перегрузка строкового представления.

        Причина: Для грузовиков важно показывать грузоподъемность.
        """
        base_str = super().__str__()
        return f"{base_str} | Грузовой, {self.load_capacity} тонн, {self.num_axles} осей"

    def __repr__(self) -> str:
        """
        Перегрузка технического представления.

        Причина: Добавлены специфичные для грузовика атрибуты.
        """
        return (f"Truck(brand='{self.brand}', model='{self.model}', year={self.year}, "
                f"price={self.price}, load_capacity={self.load_capacity}, "
                f"num_axles={self.num_axles})")

if __name__ == "__main__":
    # Создание объектов
    car = Car("Toyota", "Camry", 2022, 35000, 4, "бензин", True)
    truck = Truck("Volvo", "FH16", 2021, 120000, 25.5, 3)
    basic_vehicle = Vehicle("Generic", "Model", 2020, 10000)

    # Демонстрация работы методов
    print("=" * 50)
    print("СТРОКОВЫЕ ПРЕДСТАВЛЕНИЯ:")
    print(f"Vehicle: {basic_vehicle}")
    print(f"Car: {car}")
    print(f"Truck: {truck}")

    print("\n" + "=" * 50)
    print("ТЕХНИЧЕСКИЕ ПРЕДСТАВЛЕНИЯ:")
    print(f"repr(Vehicle): {repr(basic_vehicle)}")
    print(f"repr(Car): {repr(car)}")
    print(f"repr(Truck): {repr(truck)}")

    print("\n" + "=" * 50)
    print("ЗАПУСК ДВИГАТЕЛЯ (унаследованный метод):")
    print(car.start_engine())
    print(truck.start_engine())

    print("\n" + "=" * 50)

print("ОСТАНОВКА ДВИГАТЕЛЯ (перегруженный метод):")
print(car.stop_engine())
print(truck.stop_engine())

print("\n" + "=" * 50)
print("СПЕЦИФИЧНЫЕ МЕТОДЫ:")
print(car.open_sunroof())
print(truck.load_cargo(10))
print(truck.load_cargo(20))  # Попытка превысить грузоподъемность

print("\n" + "=" * 50)
print("ДОСТУП К АТРИБУТАМ (инкапсуляция):")
print(f"Марка Car (через геттер): {car.brand}")
# print(car._brand)  # Можно, но не рекомендуется (соглашение о непубличности)
# car.brand = "Honda"  #