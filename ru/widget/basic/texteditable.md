# Runtime.Widget.TextEditable

Компонент текст


```bay
<class name="App.Example">

<use name="Runtime.Widget.TextEditable" component="true" />

<template>
    <TextEditable
        name="textarea"
        value={{ this.text }}
        @event:valueChange="this.setText(event.value)"
    />
</template>

<script>
string text = "";
void setText(string text)
{
    this.text = text;
}
</script>

</class>
```