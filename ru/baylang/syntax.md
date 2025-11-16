# Синтаксис

BayLang использует C подобный синтаксис.


## Пример программы

```
namespace Main;

class App
{
    static int main()
    {
        print("Hello world");
        return 0;
    }
}
```

Пример компонента:
```
<class name="App.Components.IndexPage.IndexPage">

<style>
.index_page{
    padding: 5px;
}
</style>

<template>
    <div class="index_page">
        <h1>Index page</h1>
    </div>
</template>

</class>
```


## Типы переменных

Скалярные типы:
- int - целое число
- double - вещественное число с двойной точностью
- bool - логический тип
- string - строка

Объекты:
- Vector - вектор
- Map - Словарь, где ключи являются строки. Преобразование хэш функции объекта в строку нужно делать самостоятельно или с использование дополнительных библиотек.
- Date, DateTime - Классы для работы с датой и временем


## Стандартные классы

- rlt - Runtime бибилотека с общими функциями
- rs - Класс для работы со строками
- re - Регулярные выражения
- fs - Класс для работы с файловой системой

Основные классы:
- BaseModel - базовая реализация модели
- BaseObject - базовый объект, от которого наследуются большинство классов
- BaseProvider - провайдер
- Chain, ChainAsync - цепочки вызовов
- Component - базовый компонент
- Context - основной класс, реализующий контекст приложения
- Curl - Отправка HTTP запросов
- File - Объект файл
- Method - Вызов функций по имени
- Money - Класс для работы с деньгами
- Reference - Ссылка
- Serializer - Сериализация объектов
- VirtualDom - Вирутальный DOM


## Переменные

В BayLang принято использовать переменные в стиле snake case: в нижнем регистре и использовать подчеркивание. Это нужно, чтобы визуально отличать переменные от методов. Методы наоборот используют CamelCase.

Пример:
```
int count = 0;
string message = "Hello";
bool is_active = false;
Vector items = [];
Map map = {};
```

Пример для шаблонов:
```
<template>
    %set int count = 0;
    %set string message = "Hello";
    %set bool is_active = false;
    %set Vector items = [];
    %set Map map = {};
</template>
```


## Условия

Пример:
```
if (a > b)
{
    print ("A больше B");
}
else
{
    print ("A меньше или равно B");
}
```

Условия в шаблонах:
```
<template>
    %if (a > b)
    {
        <span>A больше B</span>
    }
    %else
    {
        <span>A меньши или равно B</span>
    }
</template>
```


## Циклы

```
int sum(Vector items)
{
    int result = 0;
    for (int i=0; i<items.count(); i++)
    {
        sum += items.get(i);
    }
    return result;
}
```

Цикл в шаблоне:
```
<template>
    <div class="items">
    %for (int i=0; i<this.items.count(); i++)
    {
        <div class="item">{{ this.items.get(i) }}</div>
    }
    </div>
</template>
```
