# Маршрутизация

Для того, чтобы объявить маршрутизацию ее надо зарегистрировать в ModuleDescription.

```
pure Vector<Entity> entities() =>
[
	new Route("App.Components.Pages.Routes"),
];
```

Затем создать файл App.Components.Pages.Routes

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

Методы:
- getLayoutName - Объявляет название layout, который будет отображаться. Список layout регистрируется через SetupLayout::hook
- getRoutes - Регистрирует маршруты приложения

Типы маршрутов:
- RouteAction - будет вызвана функция для обработки запроса
- RouteModel - будет вызвана модель страницы
- RoutePage - будет отображен компонент


Пример RouteAction:
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


Пример RoutePage:

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

## URL параметры

В URL возможно добавлять параметры:

```
new RouteModel
{
	"uri": "/{lang}/catalog/{id}",
	"name": "app:catalog:item",
	"model": "App.Components.Pages.Catalog.ItemPageModel",
}
```

В модели можно получить эти параметры через контейнер:

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

При этом на бэкенде данные будут загружены через api. И модель автоматически сериализуется и восстановлена на фронтенде.