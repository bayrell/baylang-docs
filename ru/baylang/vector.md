# Vector

Vector - структура данных для работы с коллекциями в BayLang. Это упорядочный список элементов, который может изменять свою длинну при добавлении или удалении элементов.

Пример создания вектора:
```
Vector arr = [];
```

Узнать количество элементов:
```
print(arr.count());
```

Получить элемент по его индексу:
```
print(arr.get(index));
print(arr.get(index, default_value));
```

Установить значение элемента:
```
arr.set(index, value);
```

Получить первый элемент:
```
arr.first();
```

Получить последний элемент:
```
arr.last();
```


## Добавление и удаление элементов

Чтобы добавить элемент в конец списка выполните:
```
arr.push(item);
```

Удалить элемент по его индексу:
```
arr.remove(index);
```

Вставить элемент:
```
arr.insert(index, new_item);
```

Объединить вектор с другим вектором:
```
Vector new_arr = arr.concat(["new item"]);
```

Добавить несколько элементов:
```
arr.appendItems(items);
```

Вернуть новый массив:
```
arr.slice(offset)
arr.slice(offset, length)
```

offset - начало

length - длинна нового массива. Необязательный параметр. Если его нет, то возвращается весь массив, начиная с offset


## Поиск элементов

Найти индекс элемента по его значению:
```
int index = arr.indexOf(value);
```

Если элемент не найден, то функция вернет -1

Поиск элемента с помощью функции:
```
string item = arr.find(bool (string item) => rs::strlen(item) != 0);
```

Аналогично можно узнать индекс элемента:
```
int index = arr.findIndex(bool (string item) => rs::strlen(item) != 0);
```


## Функциональное программирование

Функция map:
```
Vector new_arr = arr.map(int (int item) => item * 2);
```

Функция reduce:
```
int sum = arr.reduce(
    int (int sum, int value) => sum + value, 0
);
```

Функция filter:
```
Vector new_arr = arr.filter(bool (int item) => item != 0);
```

Функция each:
```
int sum = 0;
arr.each(void (int item, int index) use (sum){
    sum += item;
})
```

Преобразование из Vector в Map
```
Map items = arr.transition(
    Vector (int value, int index)
    {
        return [index, value];
    }
);
```


## Сортировка массива

Обычная сортировка:
```
arr.sort()
```

Сортировка с пользовательской функцией:
```
arr.sort(int (int a, int b) => a > b);
```


## Функции работы с вектором

Развернуть массив:
```
arr.reverse();
```

Удалить дубликаты:
```
arr.removeDuplicates();
```

Убрать вложенные вектора:
```
arr.flatten();
```