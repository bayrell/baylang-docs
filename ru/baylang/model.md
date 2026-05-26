# Модели

Модели в BayLang хранят состояние проекта и бизнес логику работы приложения. Важно понимать, что модели это часть фронтенд. Они отвечают как будут храниться данные на клиенте.

Data Transfer Object (DTO) тоже являются моделями.

Очень важно в моделях обеспечивать сериализацию. Сериализация позволяет передавать данные из бэкенд на фронтенд.

Пример модели:
```
namespace App;

use Runtime.ApiResult;
use Runtime.BaseModel;
use Runtime.RenderContainer;
use Runtime.Serializer.ObjectType;
use Runtime.Serializer.StringType;
use Runtime.Web.RouteInfo;
use App.ExamplePage;
use App.Models.User;

class PageModel extends BaseModel
{
	string component = classof ExamplePage;
	string name = "";
	User user = null;
	
	
	/**
	 * Init params
	 */
	void initParams(Map params)
	{
		parent(params);
	}
	
	
	/**
	 * Init widget
	 */
	void initWidget(Map params)
	{
		parent(params);
	}
	
	
	/**
	 * Serialize model
	 */
	static void serialize(ObjectType rules)
	{
		parent(rules);
		rules.addType("name", new StringType());
		rules.addType("user", new ObjectType{
			"class_name": classof User,
		});
	}
	
	
	/**
	 * Load data
	 */
	async void loadData(RenderContainer container)
	{
		await parent(container);
		
		RouteInfo route = this.layout.get("route");
		int id = route.matches.get("user_id");
		await this.loadUser(id);
	}
	
	
	/**
	 * Load user
	 */
	async void loadUser(int id)
	{
		ApiResult result = this.layout.sendApi({
			"api_name": "app.user",
			"method_name": "item",
			"data":
			{
				"pk":
				{
					"id": id
				}
			}
		});
		
		if (result.isSuccess())
		{
			/* Set user by filter rules */
			this.user = static::filter("user", result.data.get("item"));
			
			/* Or set value */
			this.setValue("user", result.data.get("item"));
		}
	}
	
	
	/**
	 * Build title
	 */
	void buildTitle(RenderContainer container)
	{
		this.layout.setPageTitle("Page");
	}
}
```

Когда модель создается, ей передаются параметры. Существуют две функции, которые вызываются в момент создания модели:
- initParams – используется для инициализации параметров модели. Используется для инициализации переменных модели.
- initWidget – инициализация виджетов модели. Обычно используется, чтобы создать другие модели и их настроить.

Функция serialize отвечает за сериализацию данных модели. Сериализация это процесс преобразования класса модели в объект, который готов к передаче. Обычно данные модели передаются из бэкенд во фронтенд. Но это необязательно. Можно также сохранять данные модели в базу данных.

Если модель загружает какие либо данные, то эти данные нужно добавить в функцию сериализации.

Функция loadData загружает данные из бэкенд по api. Вызывается, когда RenderContainer рендерит страницу.

Функция buildTitle устанавливается заголовок страницы.

RenderContainer - это контейнер, который используется приложением в момент инициализации страницы. Он отвечает за поиск маршрута Route и загрузку данных модели.

Переменная component указывает на то, какой компонет должен отображаться вместо с этой моделью.

## Layout

Layout - это глобальная модель всего приложения. Обычно она доступна из модели и шаблона. Обратиться к ней можно через переменную this.layout.

Layout содержит функции такие, как:
- Заголовок страницы
- Текущий роут
- Модели страницы и виджеты
- Список компонентов, используемых в приложении.
