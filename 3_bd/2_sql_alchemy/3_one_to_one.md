# SQLAlchemy ORM 1:1

Ниже приведён пример создания связи "```один к одному```" между таблицами с помощью SQLAlchemy:

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Один к одному: пользователь имеет один адрес.
    # uselist=False указывает, что связь возвращает один объект, а не список.
    address = relationship("Address", uselist=False, back_populates="user")


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String)

    # Внешний ключ с уникальным ограничением – гарантирует, что каждому пользователю соответствует не более одного адреса.
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)

    # Обратная связь
    user = relationship("User", back_populates="address")


# Создаем движок (здесь используем SQLite для примера, но можно заменить на PostgreSQL и т.д.)
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления данных
user1 = User(name='Alice')
address1 = Address(email='alice@example.com', user=user1)
session.add(user1)
session.add(address1)
session.commit()

# Запрос и вывод адреса, связанного с пользователем
retrievedUser = session.query(User).filter_by(name='Alice').first()
print("Пользователь:", retrievedUser.name)
print("Его адрес:", retrievedUser.address.email)
```

#### Пояснение

1. **Класс User**

- Определяет таблицу ```users``` с полями ```id``` и ```name```.
- Связь с таблицей addresses задается через ```relationship("Address", uselist=False, back_populates="user")```.
  Параметр ```uselist=False``` указывает, что связь "один к одному" возвращает одиночный объект (а не список).

2. **Класс Address**

- Определяет таблицу addresses с полями ```id```, ```email``` и ```user_id```.
- ```user_id``` является внешним ключом, ссылающимся на ```users.id```, и имеет уникальное
  ограничение (```unique=True```), что гарантирует, что каждый пользователь может иметь не более одного адреса.
- Связь с классом ```User``` определяется через ```relationship("User", back_populates="address")```.

3. При создании экземпляра ```Address``` мы связываем его с экземпляром ```User```, что позволяет получить доступ к
   адресу пользователя через свойство address и наоборот – к пользователю через свойство ```user```.

Таким образом, с помощью **SQLAlchemy** можно легко настроить связь "**один к одному**", используя
параметр ```uselist=False``` в ```relationship``` и уникальное ограничение на внешний ключ.



