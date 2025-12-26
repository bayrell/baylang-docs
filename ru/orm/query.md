# Query

Объект, который позволяет отправлять SQL запросы в базу данных.

Пример запроса:
```
Query q = new Query()
    .select(["id", "name"])
    .from("items")
    .where("item", "=", "1")
;

Connection conn = Connection::get();
QueryResult<Map> rows = await conn.fetchAll();
```

## Создание запросов

Получить Raw SQL query
```
Query raw(string sql, Map data);
```

Посчитать найденные строки
```
Query calcFoundRows(bool value = true);
```

Удалить из ответа дубликаты
```
Query distinct(bool value = true)
```

Включить отладку запроса
```
Query debug(bool value = true)
```

Выполнить select запрос
```
Query select(Vector fields = null)
```

Указать название таблицы и его синоним
```
Query table(string table_name = "", string alias_name = "")
Query from(string table_name = "", string alias_name = "")
```

Выполнить запрос на вставку данных
```
Query insert(string table_name = "")
```

Пример:
```
Query q = new Query()
    .insert("items")
    .values({
        "name": "item",
    });

Connection conn = Connection::get();
await conn.execute(q);
```

Выполнить запрос на обновление данных
```
Query update(string table_name = "")
```

Пример:
```
Query q = new Query()
    .update("items")
    .where("id", "=", 1)
    .values({
        "name": "item",
    })
;

Connection conn = Connection::get();
await conn.execute(q);
```

Выполнить запрос на удаление данных
```
Query delete(string table_name = "")
```

Пример:
```
Query q = new Query()
    .delete("items")
    .where("id", "=", 1)
;

Connection conn = Connection::get();
await conn.execute(q);
```

Получить тип запроса (select, insert, update, delete, raw)
```
Query kind(string kind)
```


## Список полей запроса

Очистить поля
```
Query clearFields()
```

Заменить поля запроса на другие
```
Query fields(Vector<string> fields)
```

Добавить поле запроса
```
Query addField(string field)
```

Добавить сырое поле запроса. Нужно для запросов вида `count(*) as c` или полнотекстовых запросов
```
Query addRawField(string field_name)
```

Добавить список полей
```
Query addFields(Collection<string> fields)
```


## Значения запроса

Добавить значение
```
Query value(string key, string value)
```

Добавить список значений
```
Query values(Dict data)
Query data(Dict data)
```

## Пагинация

Установить номер страницы. Страница начинается с нуля
```
Query page(int page, int limit = null)
```

Установить смещение offset
```
Query offset(int start)
Query start(int start)
```

Установить лимит на строчки
```
Query limit(int limit)
```

Получить номер текущей страницы. Считается как offset / limit
```
int getPage()
```

Получить список страниц
```
int getPages(int rows)
```

## Сортировка


Очистить сортировку
```
Query clearOrder()
```

Сортировка по имени поля
```
Query orderBy(string name, string sort)
```


## Фильтр

Поиск по значению поля
```
Query where(string key, string op, var value)
```

Установить новый фильтр
```
Query setFilter(Collection<QueryFilter> filter)
```

Добавить фильтр
```
Query addFilter(var filter)
```

Добавить или
```
Query addOrFilter(Collection filter)
```

Очистить фильтр
```
Query clearFilter()
```


## Inner Join

```
Query innerJoin(string table_name, Collection filter, string alias_name = "")
Query leftJoin(string table_name, Collection filter, string alias_name = "")
```