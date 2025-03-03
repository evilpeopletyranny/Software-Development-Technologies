# Builder

## Строитель

**Билдер** — это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово. Строитель
даёт возможность использовать один и тот же код строительства для получения разных представлений объектов.

В разработке программного обеспечения часто возникает необходимость создания объектов с множеством параметров, особенно
когда некоторые из них являются опциональными. Паттерн проектирования **Билдер (Builder)** предоставляет гибкий способ
создания сложных объектов, разделяя процесс их конструирования и представляя различные варианты их построения.

Почему-то билдер не очень любят, но на самом деле у него есть много хороших применений:

- Разбиение гигантского конструктора на отдельные шаги.
- Вариация шагов при создании объекта.
- За счет разных версий строителя может достигаться разный набор параметров в объекте.
- **Использование параметров по умолчанию (т.к. Java такого не умеет)**.
- Построение объекта на основе данных, получаемых в разных местах.

### Реализация

Реализация билдера в общем случае проста и заключается в разбиении телескопического конструктора на шаги.

#### Вариации для остальных языков

Есть множество вариантов как реализовать билдер, например:

- Статический внутренний класс.
- Внешний класс с использованием интерфейсов.
- Билдер со всеми обязательными полями.
- Билдер с полями по умолчанию.
- Билдер без проверки переданных данных перед построением объекта.
- Билдер с проверкой переданных данных перед построением объекта.
- Объединение нескольких указанных выше вариантов.

#### Вариация для Python

Поскольку Python поддерживает именованные параметры и параметры по умолчанию, то паттерн **Builder** в Python редко
реализуют в его обычном виде. Зачастую обходятся просто конструктором.

### Примеры

#### О примерах в книгах

В книге **Погружение в паттерны проектирования** *Александра Швеца* объяснение билдера осложнено введением класса
Директора. Директор не имеет прямого отношения к билдеру и является лишь надстройкой, которая позволяет использовать (
подсовывать директору) разные реализации билдеров, если такие есть.

#### Пример [trip](code/base_trip.py) с большим конструктором (обычный билдер)

В данном примере рассматривается следующее:

- Конструктор с большим кол-вом параметров.
- Вложенный статический билдер.
- В билдере указываются значения по умолчанию.
- Использование **паттерна Fluent Interface**.

**Fluent Interface** — это стиль программирования/паттерн, который позволяет связывать вызовы методов друг с другом для
создания более читаемого и выразительного кода. В данном примере он выражается в цепочке вызовов методов билдера.

```python
from datetime import date, timedelta


class Trip:
    def __init__(self, start_date: date, end_date: date, start: str, end: str,
                 duration: int, number_traveller: int, number_kids: int,
                 minimum_stars: int, minimum_recommendations: int,
                 rating: int, minimum_number_ratings: int):
        self.start_date = start_date
        self.end_date = end_date
        self.start = start
        self.end = end
        self.duration = duration
        self.number_traveller = number_traveller
        self.number_kids = number_kids
        self.minimum_stars = minimum_stars
        self.minimum_recommendations = minimum_recommendations
        self.rating = rating
        self.minimum_number_ratings = minimum_number_ratings

    def __eq__(self, other):
        if not isinstance(other, Trip):
            return False
        return (self.start_date == other.start_date and
                self.end_date == other.end_date and
                self.start == other.start and
                self.end == other.end and
                self.duration == other.duration and
                self.number_traveller == other.number_traveller and
                self.number_kids == other.number_kids and
                self.minimum_stars == other.minimum_stars and
                self.minimum_recommendations == other.minimum_recommendations and
                self.rating == other.rating and
                self.minimum_number_ratings == other.minimum_number_ratings)

    def __hash__(self):
        return hash((self.start_date, self.end_date, self.start, self.end,
                     self.duration, self.number_traveller, self.number_kids,
                     self.minimum_stars, self.minimum_recommendations,
                     self.rating, self.minimum_number_ratings))

    def __str__(self):
        return (f"Trip[start_date={self.start_date}, end_date={self.end_date}, "
                f"start='{self.start}', end='{self.end}', duration={self.duration}, "
                f"number_traveller={self.number_traveller}, number_kids={self.number_kids}, "
                f"minimum_stars={self.minimum_stars}, minimum_recommendations={self.minimum_recommendations}, "
                f"rating={self.rating}, minimum_number_ratings={self.minimum_number_ratings}]")

    class Builder:
        def __init__(self, start_date: date, end_date: date, start: str, end: str):
            self.start_date = start_date
            self.end_date = end_date
            self.start = start
            self.end = end
            self.duration = 1  # По умолчанию: продолжительность 1 день
            self.number_traveller = 1  # По умолчанию: 1 путешественник
            self.number_kids = 0  # По умолчанию: 0 детей
            self.minimum_stars = 3  # По умолчанию: минимум 3 звезды
            self.minimum_recommendations = 100  # По умолчанию: минимум 100 отзывов
            self.rating = 4  # По умолчанию: рейтинг 4
            self.minimum_number_ratings = 20  # По умолчанию: минимум 20 отзывов с рейтингом

        def set_duration(self, duration: int):
            self.duration = duration
            return self

        def set_number_traveller(self, number_traveller: int):
            self.number_traveller = number_traveller
            return self

        def set_number_kids(self, number_kids: int):
            self.number_kids = number_kids
            return self

        def set_minimum_stars(self, minimum_stars: int):
            self.minimum_stars = minimum_stars
            return self

        def set_minimum_recommendations(self, minimum_recommendations: int):
            self.minimum_recommendations = minimum_recommendations
            return self

        def set_rating(self, rating: int):
            self.rating = rating
            return self

        def set_minimum_number_ratings(self, minimum_number_ratings: int):
            self.minimum_number_ratings = minimum_number_ratings
            return self

        def build(self):
            return Trip(
                start_date=self.start_date,
                end_date=self.end_date,
                start=self.start,
                end=self.end,
                duration=self.duration,
                number_traveller=self.number_traveller,
                number_kids=self.number_kids,
                minimum_stars=self.minimum_stars,
                minimum_recommendations=self.minimum_recommendations,
                rating=self.rating,
                minimum_number_ratings=self.minimum_number_ratings
            )


def main():
    # Использование прямого конструктора (аналог большого и страшного конструктора)
    manual_trip = Trip(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=14),
        start="НГТУ им.Р.Е.Алексеева",
        end="IBIS",
        duration=14,
        number_traveller=1,
        number_kids=0,
        minimum_stars=4,
        minimum_recommendations=100,
        rating=4,
        minimum_number_ratings=20
    )
    print(manual_trip)

    # Использование билдера
    builder_trip = (Trip.Builder(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=14),
        start="НГТУ им.Р.Е.Алексеева",
        end="IBIS")
                    .set_duration(14)
                    .set_number_traveller(1)
                    .set_number_kids(0)
                    .set_minimum_stars(4)
                    .set_minimum_recommendations(100)
                    .set_rating(4)
                    .set_minimum_number_ratings(20)
                    .build())
    print(builder_trip)

    # Создание через билдер с пропуском некоторых шагов
    without_some_steps_trip = (Trip.Builder(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=14),
        start="НГТУ им.Р.Е.Алексеева",
        end="IBIS")
                               .set_duration(14)
                               .set_number_kids(0)
                               .set_minimum_recommendations(100)
                               .set_minimum_number_ratings(4)
                               .build())
    print(without_some_steps_trip)


if __name__ == "__main__":
    main()
```

#### Пример того же [trip](code/base_trip.py) используя возможности Python

```python
from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class Trip:
    start_date: date
    end_date: date
    start: str
    end: str
    duration: int = 1
    number_traveller: int = 1
    number_kids: int = 0
    minimum_stars: int = 3
    minimum_recommendations: int = 100
    rating: int = 4
    minimum_number_ratings: int = 20

    def __str__(self):
        return (f"Trip[start_date={self.start_date}, end_date={self.end_date}, start='{self.start}', "
                f"end='{self.end}', duration={self.duration}, number_traveller={self.number_traveller}, "
                f"number_kids={self.number_kids}, minimum_stars={self.minimum_stars}, "
                f"minimum_recommendations={self.minimum_recommendations}, rating={self.rating}, "
                f"minimum_number_ratings={self.minimum_number_ratings}]")


def main():
    # Создание объекта с явным указанием всех параметров
    trip_full = Trip(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=14),
        start="НГТУ им.Р.Е.Алексеева",
        end="IBIS",
        duration=14,
        number_traveller=1,
        number_kids=0,
        minimum_stars=4,
        minimum_recommendations=100,
        rating=4,
        minimum_number_ratings=20
    )
    print(trip_full)

    # Создание объекта с использованием значений по умолчанию для части параметров
    trip_default = Trip(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=14),
        start="НГТУ им.Р.Е.Алексеева",
        end="IBIS"
    )
    print(trip_default)


if __name__ == "__main__":
    main()

```


### Плюсы данного паттерна

- **Разделение конструкции и представления**: Позволяет создавать различные представления объекта, используя один и тот
  же процесс построения.
- **Упрощение создания объектов**: Избегает необходимости создавать конструкторы с большим числом параметров или
  использовать множество конструкторов для различных комбинаций параметров.
- **Повышение читаемости кода**: Код создания объекта становится более понятным и структурированным, особенно при
  использовании Fluent Interface.
- **Гибкость**: Легко добавлять новые опциональные параметры без изменения существующих классов.

### Недостатки данного паттерна

- **Увеличение количества кода**: Требуется создание дополнительных классов (Builder), что может привести к увеличению
  объёма кода.
- **Отсутствие поддержки рекурсии**: Паттерн может быть неудобен при создании объектов, содержащих рекурсивные
  структуры.