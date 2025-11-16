# Map

Map - это структура данных для работы с хэш таблицей ключ-значение. В качестве ключей используются строки. Для хранения объектов, пользователь должен сам определить хэш функцию или использовать готовые из библиотеки.

Альтернативные названия: map, хэш таблица, словарь.

Пример создания хэш таблицы:
```
Map items = {};
```

Установка значения:
```
items.set(key, value);
```

Получить значение по ключу:
```
items.get(key);
```

Объединить словарь с другим словарем:
```
items.concat({"key": "value"});
```


## Функциональное программирование

Функция map позволяет изменять значения словаря:
```
Map new_map = items.map(int (int value, string key) => value * 2);
```

Функция map, позволяет изменять значения и ключи:
```
Map new_map = items.mapWithKeys(Vector (int value, string key) => [key, value * 2]);
```

Функция reduce:
```
int sum = items.reduce(
    int (int sum, int value, string key) => sum + value, 0
);
```

Функция filter:
```
Map new_map = items.filter(bool (int value, string key) => value != 0);
```

Функция each:
```
int sum = 0;
items.each(
    void (int value, string key) use (sum)
    {
        sum += value;
    }
);
```

Функция transition. Позволяет конвертировать Map в Vector:
```
Vector arr = items.transition(
    int (int value, string key) => value
)
```