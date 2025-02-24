# ORM

**ORM (Object Relational Mapping, объектно-реляционное отображение)** — это технология, которая позволяет работать с
базами данных так, как если бы это были объекты из языков программирования.

Ниже приведён пример создания класса, который будет отображаться в виде таблицы в базе данных **PostgreSQL** с
использованием **SQLAlchemy ORM** и декларативного стиля:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс для декларативного описания моделей
Base = declarative_base()


# Определяем модель (класс), который будет отображаться в виде таблицы
class User(Base):
    __tablename__ = 'users'  # Имя таблицы в БД

    id = Column(Integer, primary_key=True)  # Первичный ключ
    name = Column(String, nullable=False)  # Имя пользователя
    age = Column(Integer)  # Возраст пользователя

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"


# Создаем движок для подключения к PostgreSQL
# Замените username, password, localhost, порт (обычно 5432) и mydatabase на актуальные значения.
engine = create_engine("postgresql://username:password@localhost:5432/mydatabase", echo=True)

# Создаем таблицы в базе данных, соответствующие всем моделям, наследуемым от Base.
Base.metadata.create_all(engine)

# Создаем сессию для работы с БД (добавление, запрос, обновление и удаление данных)
Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления нового пользователя
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

# Пример запроса для получения пользователя
user = session.query(User).filter_by(name="Alice").first()
print(user)
```

#### Пояснение

1. **Импорт модулей:** Импортируются необходимые классы и функции из SQLAlchemy для создания движка, описания модели и
   работы с сессией.
2. **Декларативный базовый класс:** Функция ```declarative_base()``` создаёт базовый класс **Base**, от которого
   наследуются все модели, отображаемые в виде таблиц в базе данных.
3. **Описание модели:** Класс User определяет структуру таблицы users с тремя столбцами: id (целое число, первичный
   ключ), name (строка, обязательное поле) и age (целое число). Метод __repr__ используется для удобного отображения
   объектов.
4. **Создание движка:** Функция ```create_engine``` создаёт подключение к PostgreSQL. Адрес подключения имеет вид:

```
postgresql://username:password@localhost:5432/mydatabase
```

где необходимо заменить данные на реальные параметры подключения к вашей базе данных.

5. Вызов ```Base.metadata.create_all(engine)``` создаёт все таблицы, определенные моделями, в базе данных, если их еще
   нет.
6. **Работа с сессией:** С помощью sessionmaker создаётся сессия для взаимодействия с базой данных. Пример добавления
   новой записи и запроса пользователя демонстрирует, как работать с объектами модели.