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
