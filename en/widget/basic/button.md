# Runtime.Widget.Button

Component for working with buttons

Usage examples:
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

You can add a class to the button to change its properties:
```
<Button class="button--primary">Click</Button>
```

Button properties:
- button--small - Small button
- button--large - Large button
- button--primary - Primary button
- button--secondary - Secondary button
- button--outline - Button without background, border only
- button--danger - Danger button
- button--success - Success button
- button--info - Informational button
- button--warning - Warning button
- button--stretch - Stretch the button to the full width