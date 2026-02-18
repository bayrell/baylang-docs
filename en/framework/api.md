# Api

Api interaction is handled via the `sendApi` method.

Example:
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

Api operates using the Data Bus pattern between system components. The `Runtime.BusInterface` system interface is responsible for this.

Its implementation is available in `layout` via `sendApi`.

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

The implementation uses the Api provider and calls the `send` method.

If you need to use the API for communication between microservices, you should use the system data bus and specify the name of the service to address.

Example:

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