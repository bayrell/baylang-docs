# Шаблоны и компоненты

BayLang использует концепцию Model Component.

Это современный подход для создания полноценных Frontend приложений.

Model - хранит состояние и бизнес логику приложения

Component - отображает состояние на экране и производит рендер при изменения состояния.

BayLang использует Vue фрэймворк для рендера компонентов.

Существуют два вида компонентов:
- Компоненты без модели
- Компоненты с моделью.

Использование модели необходимо, если вы хотите управлять состоянием компонента из другого компонента. Например:
- появление диалоговых окон.
- работа с таблицами и формами.
- CRUD, работа с API
- и т.п.


## Пример простого компонента

Компонент состоит из 3х секций.
- Стили
- Шаблон
- Скрипт

```
<class name="App.Example">

<style>
.example{
	color: pink;
}
</style>

<template>
	<div class="example">
		Example component<br/>
		{{ this.message }}
	</div>
</template>

<script>
string message = "";
</script>

</class>
```

В стилях указываются CSS стили оформления компонента.

В шаблонах HTML код компонента

В script - функции для работы с фронтенд компонентом. Обычно там указываются функции, необходимые для рендера.

Если вам нужна бизнес логика, обращения по API, то этоn код стоит разместить в модели.


## Имена шаблонов

В компоненте может быть несколько шаблонов. Каждый шаблон должен обладать уникальным именем. По умолчанию имя шаблона render. Шаблон можно вызвать из другого шаблона.

Пример:
```
<class name="App.Example">

<template name="renderItem" args="Map item">
	<div class="item">
		{{ item }}
	</div>
</template>

<template>
	<div class="items">
	%for (int i=0; i<this.items.count(); i++)
	{
		%render this.renderItem(this.items.get(i));
	}
	</div>
</template>

<script>

Map items = [
	"item 1",
	"item 2",
	"item 3",
	"item 4",
	"item 5",
];

</script>

</class>
```


## Переменные

Виды переменых в шаблоне:
- Обычные переменные
- Props. Это переменные, которые передаются в компонент из других компонентов
- Вычисляемые переменные. Используются для оптимизации вычислений при рендере компонента. Computed переменная вычисляется и сохраняет свое значение. При изменении модели или данных компонента, она производит повторное вычисление.

Пример:
```
<script>

/* Обычная переменная */
string message = "Hello world!";

/* Props */
props string name = "";

/* Имя пользователя */
computed string user_name()
{
	return this.name;
}

</script>
```


## События компонента

Пример нажатия на кпопку
```
<class name="App.Example">

<template>
	<div class="example">
		<div class="message">Hello, {{ this.message }}!</div>
		<button @event:click="this.onClick()">
			Click
		</button>
	</div>
</template>

<script>

string message = "User";

void onClick()
{
	this.message ~= "!";
}

</script>

</class>
```


## Вызов компонентов из других компонентов

```
<class name="App.Example">

<use name="Runtime.Widget.Button" component="true" />

<template>
	<div class="example">
		<Button>Click</Button>
	</div>
</template>

</class>
```


## Слоты

Чтобы передать из одного компонента в другой шаблоны, нужно использовать слоты

```
<class name="App.Box">

<template>
	<div class="box">
		<div class="box_header">
			%render this.renderSlot("title");
		</div>
		<div class="box_content">
			%render this.renderSlot("content");
		</div>
	</div>
</template>

</class>
```

Вызов компонента:
```
<class name="App.Example">

<use name="App.Box" component="true" />

<template>
	<Box>
		<slot name="title">
			Title
		</slot>
		<slot name="content">
			<p>Content</p>
		</slot>
	</Box>
</template>

</class>
```