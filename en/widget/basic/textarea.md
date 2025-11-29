# Runtime.Widget.TextArea

Text component

Usage example:
```bay
<class name="App.Example">

<use name="Runtime.Widget.TextArea" component="true" />

<template>
    <TextArea
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