# Язык программирования BayLang

BayLang - это инновационный FullStack язык программирования, обладающий уникальной функциональностью автоматического конвертирования кода программы в backend и frontend, без необходимости разрабатывать отдельный код для серверной и клиентской частей.

Основная идея это компиляция в PHP и JavaScript через компилятор. Это Позволяет создавать программу с единым кодом для разных платформ (веб сайты, php, wordpress, js, python, мобильное приложение, декстоп Windows, Linux).

Это устраняет необходимость в постоянном переключении между различными языками программирования и значительно повышает скорость разработки веб-приложений.

BayLang позволяет сохранять единую кодовую базу и при необходимости менять технологическую платформу, на которой будет работать программа.

Это полноценный язык программирования для создания различных программ для разных платформ.

**Особенности BayLang:**
- Разработка кроссплатформенных приложений (веб сайты, CRM и ERP системы, мобильные и десктоп приложения)
- Реактивность: автоматическое обновление страницы при изменении модели данных.
- Реализация MVC-архитектуры.
- Поддержка серверного рендеринга (SSR).
- Поддержка конструктора сайтов
- Поддержка MySQL и SQLite, с возможностью добавления других СУБД.
- Планируется поддержка Python.

Также в BayLang есть интеграция с ИИ.


## Пример программы на BayLang

```bay
namespace Main;

class App
{
    static int main()
    {
        print("Hello world!");
        return 0;
    }
}
```

Компонент:
```bay
<class name="App.Components.IndexPage.IndexPage">

<style>
.index_page{
    padding: 5px;
}
</style>

<template>
    <div class="index_page">
        Hello, {{ this.model.username }}!
    </div>
</template>

</class>
```

Модель:
```bay
namespace App.Components.IndexPage;

use Runtime.BaseModel;
use App.Components.IndexPage.IndexPage;

class IndexPageModel extends BaseModel
{
    string component = classof IndexPage;
    string username = "";
    
    
    /**
     * Build title
     */
    void buildTitle(RenderContainer container)
    {
        this.layout.setPageTitle("Index page");
    }
}
```

## История создания

[25 Nov 2025] Релиз версии 1.0

[15 May 2025] Начата работа на 1.0 версией

[05 Feb 2024] 0.12.4 - Добавлена поддержка переноса строк в HTML компонентах, функции высших порядков для выражений, исправлена работа CSS медиа запросов.

[27 Dec 2024] 0.12.3 - Релиз BayLang Constructor for WordPress.

[29 Jun 2024] 0.12.2 - Добавлены подмодули, команда make_all, opcode OpNegative, перезагрузка module.json, транслятор в BayLang, поддержка слотов и стилей, тесты. Первая версия конструктора сайтов 0.1.

[07 Apr 2024] 0.12.1 - Вложенные CSS стили

[29 Dec 2023] 0.12.0 - Поддержка VueJS

[02 Aug 2023] 0.11.6 - Создан первый сайт на BayLang. Полностью переработан Runtime.Web фрэймворк.

[20 Feb 2023] 0.11.5 - Четвертый бета релиз. Версия 0.11.

[25 Dec 2022] 0.11.0 - Начата работа над стабильным релизом 0.11 версия.

[21 Feb 2021] 0.10.9 - Add declare, annotations to ui, add watch model

[02 Feb 2021] 0.10.8 - Новая render функция, add svg support. Remove AssignObject, AssignValue, takeValue

[05 Dec 2020] 0.10.7 - Add meta information to ui

[28 Nov 2020] 0.10.6 - Фикс php pipe try catch fix

[15 Oct 2020] 0.10.5 - Добавлен флаг enable_check_types

[30 Sep 2020] 0.10.4 - Пофикшены pipe, добавлена команда render to ui, добавлены spreads, протестирован PHP translator

[02 Sep 2020] 0.10.3 - Третий бета релиз.

[28 Aug 2020] 0.10.2 - Возможность разрабатывать компоненты в ui шаблонах

[21 Aug 2020] 0.10.2 - Добавлены теги %if, %for, %while template

[07 Aug 2020] 0.10.0 - Перенос Context to Runtime.Core, Clear Runtime library, Async/Await in NodeJS, Fix pipes, |> as pipe

[25 Apr 2020] 0.9.1 - Запущен BayLang on Raspberry PI

[21 Apr 2020] 0.9.0 - Пайпы и монады.

[01 Mar 2020] 0.8.3 - Исправление CSS html bugfix, media nesting

[24 Feb 2020] 0.8.2 - Новая версия, Оптимизация CoreStruct and compiler

[25 Nov 2019] 0.8.0 - Вторая Alpha версия. BayLang переписан в функциональном стиле на чистых функциях и неизменяемых типах данных. (Как потом выясниться функциональный стиль медленно работает)

[29 Apr 2019] 0.7.2 - Исправление ошибок в lambda, pure, async bugfix

[25 Mar 2019] 0.7.1 - Добавил memorize, Dict, Collection, rtl::method, UIStruct normalization, DateTime as Struct

[27 Jan 2019] 0.7.0-alpha - Объединил Bayrell Template и Lang. Добавил lambda и pure функции

[16 Dec 2018] 0.6.0 - Добавил структуры и аннотации

[05 Nov 2018] 0.5.1 - Добавил async/await

[15 Jun 2018] 0.3.0 - Первая альфа рабочая версия

Summer 2016 - Начало работы