# Syntax

BayLang uses C-like syntax.


## Program example

```
namespace Main;

class App
{
    static int main()
    {
        print("Hello world");
        return 0;
    }
}
```

Component example:
```
<class name="App.Components.IndexPage.IndexPage">

<style>
.index_page{
    padding: 5px;
}
</style>

<template>
    <div class="index_page">
        <h1>Index page</h1>
    </div>
</template>

</class>
```


## Variable types

Scalar types:
- int - integer
- double - double precision floating point number
- bool - boolean type
- string - string

Objects:
- Vector - vector
- Map - Dictionary where keys are strings. Converting object hash function to string needs to be done manually or with the help of additional libraries.
- Date, DateTime - Classes for working with date and time


## Standard classes

- rlt - Runtime library with common functions
- rs - Class for working with strings
- re - Regular expressions
- fs - Class for working with file system

Main classes:
- BaseModel - basic model implementation
- BaseObject - base object from which most classes inherit
- BaseProvider - provider
- Chain, ChainAsync - call chains
- Component - base component
- Context - main class implementing application context
- Curl - Sending HTTP requests
- File - File object
- Method - Calling functions by name
- Money - Class for working with money
- Reference - Reference
- Serializer - Object serialization
- VirtualDom - Virtual DOM


## Variables

In BayLang it is customary to use variables in snake_case style: lowercase and using underscores. This is needed to visually distinguish variables from methods. Methods on the contrary use CamelCase.

Example:
```
int count = 0;
string message = "Hello";
bool is_active = false;
Vector items = [];
Map map = {};
```

Template example:
```
<template>
    %set int count = 0;
    %set string message = "Hello";
    %set bool is_active = false;
    %set Vector items = [];
    %set Map map = {};
</template>
```


## Conditions

Example:
```
if (a > b)
{
    print ("A is greater than B");
}
else
{
    print ("A is less than or equal to B");
}
```

Conditions in templates:
```
<template>
    %if (a > b)
    {
        <span>A is greater than B</span>
    }
    %else
    {
        <span>A is less than or equal to B</span>
    }
</template>
```


## Loops

```
int sum(Vector items)
{
    int result = 0;
    for (int i=0; i<items.count(); i++)
    {
        sum += items.get(i);
    }
    return result;
}
```

Loop in template:
```
<template>
    <div class="items">
    %for (int i=0; i<this.items.count(); i++)
    {
        <div class="item">{{ this.items.get(i) }}</div>
    }
    </div>
</template>
```
