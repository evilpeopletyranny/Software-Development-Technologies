# SQLAlchemy ORM n:n

Для создания связи "многие ко многим" (n к n) в SQLAlchemy обычно используется дополнительная таблица-связка (
association table), которая хранит пары идентификаторов из двух таблиц. Эта таблица не представлена в виде отдельной
модели (хотя её можно определить и как модель, если нужно хранить дополнительные атрибуты), а создаётся с помощью
функции ```Table``` из SQLAlchemy.

Ниже приведён пример реализации связи "многие ко многим" между таблицами ```Student``` и ```Course```:

```python
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Связь многие ко многим через таблицу-связку
    courses = relationship("Course", secondary=student_course_association, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    # Обратная связь
    students = relationship("Student", secondary=student_course_association, back_populates="courses")
    
# Таблица-связка между студентами и курсами
student_course_association = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Создаем движок и базу данных (например, SQLite для примера)
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления данных:
student1 = Student(name="Alice")
student2 = Student(name="Bob")
course1 = Course(title="Mathematics")
course2 = Course(title="History")

# Связываем студентов и курсы
student1.courses.append(course1)
student1.courses.append(course2)
student2.courses.append(course1)

session.add_all([student1, student2, course1, course2])
session.commit()

# Запрос и вывод данных:
for student in session.query(Student).all():
    print(f"Student: {student.name}")
    for course in student.courses:
        print(f"  Course: {course.title}")
```

#### Пояснение

- **Association Table:** Таблица ```student_course``` создаётся с помощью функции ```Table``` и содержит два столбца: ```student_id``` и ```course_id```, которые ссылаются на первичные ключи таблиц ```students``` и ```courses``` соответственно. Использование ```primary_key=True``` для обоих столбцов гарантирует уникальность каждой пары.
- **Secondary Parameter:** В обеих моделях (```Student``` и ```Course```) указываем параметр ```secondary=student_course_association``` в вызове ```relationship```, что информирует SQLAlchemy о том, что связь реализована через дополнительную таблицу.
- **Back_populates:** Параметр ```back_populates``` обеспечивает двустороннюю синхронизацию между связанными объектами.

Таким образом, для реализации связи "многие ко многим" создаётся дополнительная таблица-связка, которая хранит связи между записями двух таблиц. Эта таблица создается явно с помощью ```Table```, и её наличие является стандартной практикой для реализации отношений многие-ко-многим в SQLAlchemy.