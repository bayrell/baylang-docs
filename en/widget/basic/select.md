# Runtime.Widget.Select

Selection from a list

Usage example:
```bay
<class name="App.Example">

<use name="Runtime.Widget.Select" component="true" />

<template>
    <Select
        name="username"
        value={{ this.usertype }}
        options=[
            {"key": "user", "value": "User"},
            {"key": "admin", "value": "Admin"},
        ]
        @event:valueChange="this.setUserType(event.value)"
    />
</template>

<script>
string usertype = "";
void setUserType(string usertype)
{
    this.usertype = usertype;
}
</script>

</class>
```