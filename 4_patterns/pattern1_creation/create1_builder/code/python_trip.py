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
