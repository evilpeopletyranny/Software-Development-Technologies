# CRUD операции

**CRUD** — это аббревиатура, обозначающая четыре основных операции управления данными:

1. **Create** («создать»). Добавление новой записи или ресурса в базу данных.
2. **Read** («прочитать»). Получение данных из базы данных или ресурса.
3. **Update** («обновить»). Изменение существующей записи.
4. **Delete** («удалить»). Удаление записи или ресурса из базы данных.

# DAO

**DAO (Data Access Object)** — это шаблон проектирования, который предоставляет абстрактный интерфейс для доступа к
данным из базы данных или другого источника хранения. Основная идея заключается в том, чтобы отделить логику работы с
данными от бизнес-логики приложения, что упрощает сопровождение, тестирование и возможность изменения источника данных
без значительного переписывания кода.

## Преимущества DAO

- **Инкапсуляция логики доступа к данным**: все операции с БД (или другим хранилищем) находятся в одном классе или
  наборе классов.
- **Упрощение модификаций**: при изменении способа хранения данных (например, переходе на другую СУБД) изменения
  вносятся только в DAO, а не во всей кодовой базе.
- **Улучшенная тестируемость**: можно изолировать и протестировать логику работы с данными отдельно от бизнес-логики.

## Дополнение

- Помимо стандартного набора CRUD-операций DAO для конкретного класса/сущности может также содержать необходимый
  специфичный набор операций (например выбор пользователя по ```username```)
- Всегда добавляйте метод для получения сразу некоторого списка сущностей.
- Используйте возможности задания параметров по умолчанию если ваш ЯП это позволяет. Например для выбора сразу списка
  сущностей можно сразу указать по умолчанию параметры ```offset```, ```limit```, ```sort_by```, ```order```. Которые
  при необходимости могут быть явно изменены при вызове.

## Пример

Ниже приведён пример реализации класса DAO, который инкапсулирует полный набор CRUD-операций (создание, чтение,
обновление, удаление) с использованием SQLAlchemy, а также содержит метод для выборки всех сущностей с
параметрами ```offset```, ```limit```, ```sort_by='id'```, ```order = ACD```

```Python
from sqlalchemy import create_engine, Column, Integer, String, asc, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс для моделей
Base = declarative_base()


# Пример модели, которая будет представлена в виде таблицы в БД
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"


# Создаем движок и сессию для подключения к БД (например, SQLite для примера,
# для PostgreSQL измените строку подключения соответственно)
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Создаем таблицы
Base.metadata.create_all(engine)


# DAO-класс для модели User
class UserDAO:
    def __init__(self, session):
        self.session = session

    # CREATE: Добавление новой записи
    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        return user

    # READ: Получение записи по id
    def get_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter(User.id == user_id).first()

    # UPDATE: Обновление записи (при условии, что объект уже прикреплен к сессии)
    def update(self, user: User) -> User:
        self.session.commit()
        return user

    # DELETE: Удаление записи
    def delete(self, user: User):
        self.session.delete(user)
        self.session.commit()

    # Выборка всех сущностей с параметрами поиска.
    # По умолчанию offset=0, limit=100, сортировка по столбцу 'id' в порядке возрастания.
    def get_all(self, offset: int = 0, limit: int = 100, sort_by: str = 'id', order: str = 'ASC'):
        query = self.session.query(User)
        sort_column = getattr(User, sort_by)  # динамически получаем столбец для сортировки
        if order.upper() == 'ASC':
            query = query.order_by(asc(sort_column))
        else:
            query = query.order_by(desc(sort_column))
        return query.offset(offset).limit(limit).all()


# Пример использования DAO:
if __name__ == '__main__':
    dao = UserDAO(session)

    # CREATE: Добавляем несколько пользователей
    dao.create(User(name='Alice'))
    dao.create(User(name='Bob'))
    dao.create(User(name='Charlie'))

    # READ: Получаем пользователя по id
    user = dao.get_by_id(1)
    print("User with id 1:", user)

    # UPDATE: Обновляем данные пользователя
    if user:
        user.name = 'Alicia'
        dao.update(user)
        print("Updated user:", dao.get_by_id(1))

    # GET ALL: Получаем всех пользователей с параметрами по умолчанию
    all_users = dao.get_all()
    print("All users:")
    for u in all_users:
        print(u)

    # DELETE: Удаляем пользователя
    user_to_delete = dao.get_by_id(2)
    if user_to_delete:
        dao.delete(user_to_delete)
        print("After deletion, remaining users:")
        for u in dao.get_all():
            print(u)
```

- **Модель User:** Определена с использованием декларативного стиля. Таблица ```users``` имеет два столбца: ```id```
  и ```name```.
- **DAO-класс UserDAO:**
    - ```create```: добавляет новый объект в базу.
    - ```get_by_id```: возвращает объект по идентификатору.
    - ```update```: фиксирует изменения в базе.
    - ```delete```: удаляет объект из базы.
    - ```get_all```: возвращает все записи с возможностью задать ```offset```, ```limit```, столбец для сортировки и
      порядок сортировки. По умолчанию ```offset=0```, ```limit=100```, сортировка по '```id```' в порядке возрастания.

