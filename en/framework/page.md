# Пример страницы

To create a page, you need to create a model and a component. The model stores the state and business logic of the system, while the component displays this state.

Example model:

```
namespace App.Components.Pages.IndexPage;

use Runtime.BaseModel;
use Runtime.Serializer.ObjectType;
use Runtime.Serializer.StringType;
use Runtime.Web.RenderContainer;
use App.Components.Pages.IndexPage.IndexPage;

class IndexPageModel extends BaseModel
{
	string component = classof IndexPage;
	string message = "Hello world!";
	
	
	/**
	 * Serialize object
	 */
	static void serialize(ObjectType rules)
	{
		parent(rules);
		rules.addType("message", new StringType());
	}
	
	
	/**
	 * Load data
	 */
	async void loadData(RenderContainer container)
	{
		await parent(container);
	}
	
	
	/**
	 * Set message
	 */
	void setMessage(string message)
	{
		this.message = message;
	}
	
	
	/**
	 * Build title
	 */
	void buildTitle(RenderContainer container)
	{
		container.layout.setPageTitle("Index page");
	}
}
```

Example component:

```
<class name="App.Components.Pages.IndexPage.IndexPage">

<use name="Runtime.Widget.Button" component="true" />

<style>
.index_page{
	padding-top: 100px;
	text-align: center;
	.message{
		margin-bottom: var(--space);
	}
}
</style>

<template>
	<div class="page index_page">
		<div class="message">{{ this.model.message }}</div>
		<Button class="button--default" @event:click="this.onClick()">Click</Button>
	</div>
</template>

<script>

void onClick()
{
	this.model.setMessage(this.model.message ~ "!");
}

</script>

</class>
```

It also needs to be registered in the routes:

```
namespace App.Components;

class Routes extends BaseRoute
{
	/**
	 * Returns layout name
	 */
	static string getLayoutName() => "default";
	
	
	/**
	 * Returns routes
	 */
	static Collection<RouteInfo> getRoutes() =>
	[
		new RouteModel
		{
			"uri": "/{lang}/",
			"name": "app:index",
			"model": "App.Components.Pages.IndexPage.IndexPageModel",
		},
	];
}
```