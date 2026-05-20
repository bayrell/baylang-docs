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
	
	
	/**
	 * Returns data rules
	 */
	void getDataRules(MapType rules)
	{
		rules.addType("name", new StringType());
	}
	
	
	@ApiMethod{ "name": "index" }
	async void actionIndex()
	{
		this.filterData();
		
		string name = this.data.get("name");
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