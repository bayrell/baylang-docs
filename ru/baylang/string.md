# Работа со строками

Строки это скалярный неизменяемый объект. Строки объявляются в виде:

```bay
string message = "Hello";
```

Конкатенация строк:

```bay
string username = "User";
string new_message = message ~ " " ~ username;
```

При конкатенации строк, создается новый объект. Поэтому, если нужно соединить множество строк, то необходимо использовать Vector:

```bay
Vector messages = [];
string message = rs::join("", messages);
print(message);
```


## Библиотека работы со строками

Для работы со строками используется библиотека Runtime.rs

### Длина строки

Чтобы узнать длину строки, нужно использовать strlen
```
int rs::strlen(string s);
```

### Получить новую строку из строки

```
string rs::substr(string s, int start, int len);
```

s - строка

start - начало

len - длина новой строки

### Получить символ строки

```
char rs::charAt(string s, string pos);
```

s - строка

pos - номер символа


### Получить ASCII символ

```
int rs::chr(int code);
```

code - Код


### Получить ASCII код

```
int rs::ord(char ch);
```

ch - символ


### Преобразовать строку в нижний регистр

```
string rs::lower(string s);
```

s - строка


### Преобразовать строку в верхний регистр

```
string rs::upper(string s);
```

s - строка


### Сравнить строки между собой

```
int rs::compare(string a, string b);
```

a и b строки

Пример использования:

```
Vector arr = [
    "apple",
    "banana",
    "orange"
];
arr.sort(int (string a, string b) => rs::compare(a, b));
```


### Заменить одну строку на другую

```
int rs::replace(string search, string item, string s);
```

search - Ищем строку

item - Новая строка

s - Строка, в которой происходит поиск


### Повторить строку несколько раз

```
string rs::str_repeat(string s, int n);
```

s - строка

n - сколько раз повторить


### Разбить строку на несколько строк

```
string rs::split(string delimiter, string s, int limit = -1)
```

delimiter - разделитель

s - строка

limit - максимальное количество строк


```
Vector<string> rs::splitArr(Vector<string> delimiters, string s, int limit = -1);
```

delimiters - разделители

s - строка

limit - максимальное количество


### Соединить строки

```
string rs::join(string ch, Vector<string> arr);
```

ch - символ или строка

arr - строки


### Соединить путь

```
string rs::join_path(Vector arr);
```

arr - путь url

Пример
```
string path = rs::join_path(["folder", "name.txt"]);
```


### Удалить лишние символы слева и справа

```
string rs::trim(string s, string ch = "");
```

s - строка

ch - какие символы нужно удалять


### Поиск строки в строке

```
int rs::indexOf(string s, string search, string offset = 0);
```

s - строка, в которой происходит поиск

search - искомая строка

offset - с какого символа начинаем поиск


### Форматирование строки

```
string rs::format(string s, Dict params = null);
```

s - строка

params - параметры

Пример:

```
string message = rs::format("Hello %username%", {"username": "User"});
```