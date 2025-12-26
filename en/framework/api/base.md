# BaseApi

```
namespace App.Api;

use Runtime.Serializer.MapType;
use Runtime.Serializer.StringType;
use Runtime.Web.Annotations.ApiMethod;
use Runtime.Web.BaseApi;

class ExampleApi extends BaseApi
{
	pure string getApiName() => "app.example";
	
	
	@ApiMethod{ "name": "index" }
	async void actionIndex()
	{
		this.data = this.filter(this.request.data, new MapType{
			"name": new StringType(),
		});
		
		this.success({
			"data": {
				"name": name,
			}
		})
	}
}
```

Register api in module:
```
namespace App;

use Runtime.Entity.Entity;
use Runtime.Web.Annotations.Api;

class ModuleDescription
{
	pure string getModuleName() => "App";
	pure string getModuleVersion() => "1.0";
	pure Map<string> requiredModules() => {
		"Runtime": "*"
	};
	pure Vector<Entity> modules() => [
		new Api("App.Api.ExampleApi")
	];
}
```