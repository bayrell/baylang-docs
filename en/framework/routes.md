# Routes

To declare routing, it must be registered in ModuleDescription.

```
pure Vector<Entity> entities() =>
[
	new Route("App.Components.Pages.Routes"),
];
```

Then create the `App.Components.Pages.Routes` file.

```
namespace App.Components.Pages;

use Runtime.Web.BaseRoute;
use Runtime.Web.RouteInfo;
use Runtime.Web.RouteModel;


class Routes extends BaseRoute
{
	/**
	 * Returns layout name
	 */
	static string getLayoutName() => "default";
	
	
	/**
	 * Returns routes
	 */
	static Vector<RouteInfo> getRoutes() =>
	[
		new RouteModel
		{
			"uri": "/",
			"name": "app:index",
			"model": "App.Components.Pages.IndexPage.IndexPageModel"
		}
	];
}
```

Methods:
- `getLayoutName` - Declares the name of the layout that will be displayed. The list of layouts is registered via `SetupLayout::hook`.
- `getRoutes` - Registers the application routes.

Route types:
- `RouteAction` - A function will be called to handle the request.
- `RouteModel` - A page model will be called.
- `RoutePage` - A component will be displayed.


Example `RouteAction`:
```
namespace App.Components;

class Routes extends BaseRoute
{
	static Vector<RouteInfo> getRoutes() =>
	[
		new RouteAction
		{
			"uri": "/",
			"name": "app:root",
			"action": "actionRedirect",
		},
		new RouteAction
		{
			"uri": "/{lang}",
			"name": "app:root:lang",
			"action": "actionRedirect",
		},
	];
	
	
	/**
	 * Action redirect
	 */
	static async void actionRedirect(RenderContainer container)
	{
		string lang = container.layout.lang;
		if (container.route.name == "app:root") lang = "en";
		container.setResponse(new RedirectResponse("/" ~ lang ~ "/"));
	}
}
```


Example `RoutePage`:

```
namespace App.Components.Pages;

use Runtime.Web.BaseRoute;
use Runtime.Web.RouteInfo;
use Runtime.Web.RoutePage;


class Routes extends BaseRoute
{
	/**
	 * Returns layout name
	 */
	static string getLayoutName() => "default";
	
	
	/**
	 * Returns routes
	 */
	static Vector<RouteInfo> getRoutes() =>
	[
		new RoutePage
		{
			"uri": "/",
			"name": "app:index",
			"page": "App.Components.Pages.IndexPage.IndexPage",
			"data":
			{
				"title": "Index page"
			},
		}
	];
}
```

## URL parameters

Parameters can be added to the URL:

```
new RouteModel
{
	"uri": "/{lang}/catalog/{id}",
	"name": "app:catalog:item",
	"model": "App.Components.Pages.Catalog.ItemPageModel",
}
```

In the model, these parameters can be retrieved via the container:

```
namespace App.Components.Pages.Catalog;

use Runtime.BaseModel;
use App.Components.Pages.Catalog.IndexPage;


class ItemPageModel extends BaseModel
{
	string component = classof IndexPage;
	Vector<Product> items = [];
	
	
	/**
	 * Serialize object
	 */
	static void serialize(ObjectType rules)
	{
		parent(rules);
		rules.addType("items", new VectorType(new ObjectType{
			"class_name": classof Product,
		}));
	}
	
	
	/**
	 * Load data
	 */
	async void loadData(RenderContainer container)
	{
		await parent(container);
		
		int id = container.route.matches.get("id");
		ApiResult result = await this.layout.sendApi({
			"api_name": "app.catalog",
			"method_name": "item",
			"data": {
				"lang": this.layout.lang,
				"pk": {
					"id": id,
				}
			},
		});
		if (result.isSuccess())
		{
			this.items = result.data.get("items");
		}
	}
}
```

In this case, data will be loaded from the backend via API. The model will be automatically serialized and restored on the frontend.