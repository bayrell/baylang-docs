# Runtime.Widget.Input

Поле ввода

Пример использования:
```bay
<class name="App.Example">

<use name="Runtime.Widget.Input" component="true" />

<template>
    <Input
        name="username"
        value={{ this.username }}
        @event:valueChange="this.setUsername(event.value)"
    />
</template>

<script>
string username = "";
void setUsername(string name)
{
    this.username = name;
}
</script>

</class>
```