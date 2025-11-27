# Runtime.Widget.UploadFileButton

Компонент загрузки файла

Примеры использования:
```
<class name="App.Example">

<use name="Runtime.Widget.UploadFileButton" component="true" />

<template>
    <UploadFileButton @event:file="this.onUploadFileClick(event.value)">
        Click
    </UploadFileButton>
</template>

<script>
void onUploadFileClick(var file)
{
    var_dump(file);
}
</script>

</class>
```