# Structured Query Language

SQL — это аббревиатура от Structured Query Language (структурированный язык запросов). Он является стандартным языком
для работы с реляционными базами данных и используется для:

- **Определения структуры данных:** с помощью SQL можно создавать, изменять и удалять таблицы, устанавливать связи между
  ними (через первичные и внешние ключи) и управлять схемой базы данных.
- **Манипулирования данными:** SQL предоставляет команды для вставки, обновления, удаления и выборки данных из таблиц.
- **Запросов к базе данных:** SQL позволяет формулировать сложные запросы для извлечения нужной информации с
  использованием фильтрации, группировки, сортировки и объединения таблиц.
- **Управления транзакциями и безопасностью:** SQL используется для контроля целостности данных, управления транзакциями
  и обеспечения безопасности доступа к базе данных.

Язык SQL делиться на несколько групп команд предназначенных для разного вида операций над данными

- DDL
- DML
- DCL
- TCL

## Data Definition Language - DDL

**DDL**, или **Data Definition Language** — это группа команд, которые используются для создания и изменения структуры
объектов базы данных: таблиц, представлений, схем и индексов.

К **DDL** относятся следующие команды SQL:

- ```CREATE``` – создание новых объектов базы данных (таблиц, схем, индексов, представлений, процедур и т.д.).
- ```ALTER``` – изменение структуры уже существующих объектов (например, добавление или удаление столбцов в таблице,
  изменение типа данных).
- ```DROP``` – удаление объектов базы данных.
- ```TRUNCATE``` – удаление всех строк из таблицы с сохранением её структуры (быстрая очистка таблицы).
- ```RENAME``` – переименование объектов базы данных (в некоторых СУБД эта команда реализована как ALTER).
- ```COMMENT``` – добавление комментариев к объектам базы данных (реализована не во всех СУБД).

### Несколько примеров

#### CREATE

Этот **DDL**-оператор создает объекты базы данных, например таблицы или представления.

```sql
CREATE TABLE IF NOT EXISTS table_name (
    user_id serial PRIMARY KEY,
    username VARCHAR ( 50 ) NOT NULL,
    last_login TIMESTAMP
);
```

#### ALTER

Оператор применяется для модификации существующей структуры базы данных. Может добавить или удалить столбцы в таблице,
изменить тип столбца, добавить ограничения и тому подобное. Вот пример переименования таблицы с использованием команды:

```sql
ALTER TABLE old_table_name RENAME TO new_table_name;
```

#### DROP

Команду используют для удаления объектов из базы данных: таблицы, представления или индекса. Пример удаляет таблицу с
именем ```my_table```.

## Data Manipulation Language - DDL

**DML**, или **Data Manipulation Language** — это группа операторов, которые позволяют получать и изменять записи,
присутствующие в таблице.

- ```SELECT``` – извлечение данных из базы данных.
- ```INSERT``` – вставка новых записей в таблицы.
- ```UPDATE``` – обновление существующих записей.
- ```DELETE``` – удаление записей из таблиц.
- ````MERGE```` – объединение операций вставки, обновления и удаления в одну команду (поддерживается не во всех СУБД).

Команда ```JOIN``` сама по себе не является отдельной командой SQL, а используется внутри операторов ```SELECT```,
которые относятся к **DML (Data Manipulation Language)**. JOIN позволяет объединять строки из двух и более таблиц на
основе логических связей между ними.

### Несколько примеров

#### SELECT

Эта инструкция используется для получения кортежей из таблицы.

```sql
SELECT user_id, username FROM table_name;
```

#### INSERT INTO

Это ключевое слово применяют для добавления новых записей в таблицу.

```sql
INSERT INTO table_name(user_id, username, last_login) VALUES(1, 'Ivan Petrov', NULL)
```

#### DELETE

DML-команда позволяет удалить одну или несколько записей.

```sql
DELETE FROM table_name WHERE username = 'nick';
```

#### UPDATE

Команда используется для обновления и изменения значений записи в таблице.

```sql
UPDATE table_name SET username = 'newnick' WHERE user_id = 1;
```

## Data Control Language - DCL

**DCL**, или **Data Control Language** — это команды SQL, которые используют для предоставления и отзыва привилегий
пользователя базы данных. При этом пользователь не может откатить изменения.

- ```GRANT``` – предоставляет пользователям или ролям определённые привилегии (например, право на чтение, запись,
  выполнение и т.д.).
- ```REVOKE``` – отзывает ранее предоставленные привилегии у пользователей или ролей.

Некоторые СУБД также поддерживают команду ```DENY``` (например, в T-SQL для SQL Server), которая явно запрещает
выполнение определённых действий, даже если привилегии были предоставлены через GRANT. Однако в стандарте SQL основными
командами DCL являются GRANT и REVOKE.

### Несколько примеров

#### GRANT

Используется для предоставления пользователям прав доступа к базе данных. Например, команда разрешает
пользователю `user` добавлять записи в таблицу `my_table`.

```sql
GRANT INSERT ON my_table TO user;
```

#### REVOKE

Команда, которая позволяет отозвать ранее выданные права доступа. Например, команда отзывает право на вставку в
таблицу `my_table` у пользователя `user`.

```sql
REVOKE INSERT ON my_table TO user;
```

## Transaction Control Language - TCL

**TCL**, или **Transaction Control Language** — одни из наиболее популярных команд SQL. Их используют для обеспечения
согласованности базы данных и для управления транзакциями.

**Транзакция** — это набор SQL-запросов, выполняемых над данными, которые объединены в атомарную секцию. Это значит, что
промежуточные результаты операции не видны для других конкурирующих транзакций — и вся секция будет либо выполнена, либо
полностью отменена в случае ошибки.

- **COMMIT** – фиксирует все изменения, внесённые в рамках текущей транзакции, делая их постоянными в базе данных.
- **ROLLBACK** – отменяет все изменения, внесённые в рамках текущей транзакции (либо до заданной точки сохранения, если
  используется SAVEPOINT).
- **SAVEPOINT** – устанавливает точку сохранения внутри транзакции, к которой можно откатиться, используя ROLLBACK.
- **SET TRANSACTION** – задаёт параметры для транзакции (например, уровень изоляции).

Некоторые СУБД также поддерживают команды для начала транзакции, например, ```START TRANSACTION``` или ```BEGIN```, но
они не всегда классифицируются как TCL-команды по стандарту SQL. Основными же командами TCL являются COMMIT, ROLLBACK,
SAVEPOINT и SET TRANSACTION.

### Несколько примеров

#### BEGIN/COMMIT

Команда, которая применяется для объявления транзакции. Команда иллюстрирует пример банковской транзакции: пользователь
с `user_id`, равным 10, переводит 100 условных единиц на баланс пользователя с `user_id`, равным 20.
Конструкция ```BEGIN/COMMIT``` гарантирует, что баланс изменится сразу у двух пользователей — либо ни у одного.

```sql
BEGIN;
UPDATE my_table SET balance = balance - 100 WHERE used_id = 10;
UPDATE my_table SET balance = balance + 100 WHERE used_id = 20;
COMMIT;
```

#### ROLLBACK

Откатывает текущую транзакцию и отменяет все обновления, сделанные транзакцией.

```sql
BEGIN;
UPDATE my_table SET balance = balance - 100 WHERE used_id = 10;
UPDATE my_table SET balance = balance + 100 WHERE used_id = 20;
ROLLBACK
COMMIT;
```
