# Templates and Components

BayLang uses the Model Component concept.

This is a modern approach to creating full-fledged frontend applications.

Model - stores the application state and business logic

Component - displays the state on the screen and renders when the state changes.

BayLang uses the Vue framework to render components.

There are two types of components:
- Components without model
- Components with model.

Using a model is necessary if you want to control the state of a component from another component. For example:
- appearance of dialog boxes.
- working with tables and forms.
- CRUD, working with API
- etc.


## Simple component example

The component consists of 3 sections.
- Styles
- Template
- Script

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

Styles specify CSS styles for component design.

Templates contain the HTML code of the component

In script - functions for working with the frontend component. Usually there are functions necessary for rendering.

If you need business logic, API calls, then this code should be placed in the model.


## Template Names

A component can have multiple templates. Each template must have a unique name. By default, the template name is render. A template can be called from another template.

Example:
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


## Variables

Types of variables in the template:
- Regular variables
- Props. These are variables that are passed to the component from other components
- Computed variables. Used to optimize calculations when rendering a component. A computed variable is calculated and stores its value. When the component’s model or data changes, it performs a recalculation.

Example:
```
<script>

/* Regular variable */
string message = "Hello world!";

/* Props */
props string name = "";

/* User name */
computed string user_name()
{
	return this.name;
}

</script>
```


## Component Events

Example of button click
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


## Calling Components from Other Components

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


## Slots

To pass templates from one component to another, you need to use slots

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

Component call:
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