# Runtime.Widget.Button

Компонент работы с кнопками

Примеры использования:
```
<class name="App.Example">

<use name="Runtime.Widget.Button" component="true" />

<template>
    <Button @event:click="this.onClick()">Click</Button>
</template>

<script>
void onClick()
{
    rtl::print("Click");
}
</script>

</class>
```

У кнопки можно добавить класс, чтобы изменить ее свойства:
```
<Button class="button--primary">Click</Button>
```

Свойства кнопки:
- button--small - Маленька кнопка
- button--large - Большая кнопка
- button--primary - Главная кнопка
- button--secondary - Вторая кнопка
- button--outline - Кнопка без background, только border
- button--danger - Кнопка опасности
- button--success - Кнопка успеха
- button--info - Информационная кнопка
- button--warning - Кнопка предупреждение
- button--stretch - Растянуть кнопку на всю ширину