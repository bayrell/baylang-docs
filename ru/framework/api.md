# Api

Работа с Api осуществляется через метод sendApi.

Пример:
```
ApiResult result = await this.layout.sendApi({
	"api_name": "app.catalog",
	"method_name": "search",
	"data":
	{
		"search": "product",
		"page": 0,
		"limit": 10,
	},
});
if (result.isSuccess())
{
}
```

Api работает по методу Bus шины данных между компонентами системы. За это отвечает системный интерфейс Runtime.BusInterface.

Его реализация доступна в layout через sendApi.

```
/**
 * Send api
 */
async ApiResult sendApi(Map params)
{
	BusInterface api = @.provider("api");
	#ifdef BACKEND then
	params.set("storage", this.storage.backend);
	#endif
	return await api.send(params);
}
```

В реализации используется Api провайдер и вызывается метод send.

Если нужно использовать api для общения между микросервисами, то следует использовать системную шину данных и указывать название сервиса, к которому нужно обратиться.

Пример:

```
BusInterface api = @.provider("system_bus");
ApiResult result = api.send({
	"service": "service_name",
	"api_name": "app.catalog",
	"method_name": "search",
	"data":
	{
		"search": "product",
		"page": 0,
		"limit": 10,
	},
});
```