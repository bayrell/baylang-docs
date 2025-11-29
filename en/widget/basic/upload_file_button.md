# Runtime.Widget.UploadFileButton

File upload component

Usage examples:
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