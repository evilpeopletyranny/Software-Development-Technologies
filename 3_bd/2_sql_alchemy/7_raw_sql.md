# Вызов "сырого" SQL при помощи SQLAlchemy

Чтобы выполнить "сырой" SQL-запрос с помощью **SQLAlchemy**, можно использовать метод ```execute``` на объекте
подключения (```connection```) или сессии. Современные версии SQLAlchemy (1.4+) возвращают объект типа ```Result```,
который позволяет итерироваться по строкам результата. Каждая строка представлена в виде объекта ```Row```, с которым
можно работать как с кортежем или словарем (доступ по индексам и именам столбцов).

```python
from sqlalchemy import create_engine
from sqlalchemy import text 

# Создаем движок подключения к базе данных (пример с SQLite)
engine = create_engine("sqlite:///:memory:")

# Создаем соединение
with engine.connect() as conn:
    # Выполняем сырой SQL-запрос
    sql = text('SELECT * from BOOKS WHERE BOOKS.book_price > 50') 
    results = engine.execute(sql) 

    # Объект result является экземпляром sqlalchemy.engine.Result.
    # Мы можем итерироваться по нему и получать строки (объекты Row)
for record in results: 
    print("\n", record) 
```

```python
from sqlalchemy import create_engine
from sqlalchemy import text 

engine = create_engine("sqlite:///:memory:")

# define a tuple of dictionary of 
# values to be inserted 
data = ( { "book_id": 6, 
		"book_price": 400, 
		"genre": "fiction", 
		"book_name": "yoga is science" }, 
		
		{ "book_id": 7, 
		"book_price": 800, 
		"genre": "non-fiction", 
		"book_name": "alchemy tutorials" }, 
) 

# write the insert statement 
statement = text("""INSERT INTO BOOKS (book_id, book_price, 
genre, book_name) VALUES(:book_id, :book_price, 
:genre, :book_name)""") 

#insert the data one after other using execute 
# statement by unpacking dictionary elements 
for line in data: 
	engine.execute(statement, **line) 

# write the SQL query to check 
# whether the records are inserted 
sql = text("SELECT * FROM BOOKS ") 

results = engine.execute(sql) 

# View the records 
for record in results: 
	print("\n", record)
```
-