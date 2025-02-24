# SQLAlchemy ORM 1:n

Ниже приведён пример, демонстрирующий, как с помощью SQLAlchemy в Python создать связь «один ко многим». В данном
примере один пользователь (```User```) может иметь несколько записей (```Post```).

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Базовый класс для декларативных моделей
Base = declarative_base()


# Модель User – "один" в отношении "один ко многим"
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Связь: один пользователь имеет много постов.
    # back_populates связывает обе стороны отношения.
    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")


# Модель Post – "много" в отношении "один ко многим"
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Обратная связь: каждый пост принадлежит одному пользователю.
    author = relationship("User", back_populates="posts")


# Создаем движок для подключения к базе данных (здесь используется SQLite для примера)
engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления данных:
user1 = User(name="Alice")
post1 = Post(title="First Post", content="Content of first post", author=user1)
post2 = Post(title="Second Post", content="Content of second post", author=user1)

session.add(user1)
session.commit()

# Запрос и вывод: печатаем все заголовки постов пользователя Alice
for post in user1.posts:
    print(post.title)
```

#### Пояснение

- **Определение моделей:**
    - Класс ```User``` описывает таблицу ```users``` с полями ```id``` и ```name```, а также содержит поле ```posts```,
      которое представляет собой связь «один ко многим» с моделью ```Post```.
    - Класс ```Post``` описывает таблицу ```posts``` с полями ```id```, ```title```, ```content``` и внешним
      ключом ```user_id```, указывающим на ```users.id```. Связь ```author``` устанавливает обратную сторону отношения.
- **relationship и back_populates:** Метод ```relationship``` используется для задания связи между моделями.
  Параметр ```back_populates``` связывает свойства обеих моделей, позволяя обращаться к постам пользователя
  через ```user.posts``` и к пользователю поста через ```post.author```.
- **cascade="all, delete-orphan":** Этот параметр в ```relationship``` гарантирует, что при удалении пользователя будут
  удалены и все его посты, что помогает поддерживать целостность данных.

Таким образом, данный пример демонстрирует, как с помощью SQLAlchemy создать и использовать связь «один ко многим» между таблицами в базе данных.