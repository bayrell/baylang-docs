# Create custom hook

Create file

```
namespace App.Hooks;

use Runtime.BaseLayout;
use Runtime.RenderContainer;
use Runtime.Hooks.BaseHook;
use Runtime.Hooks.RuntimeHook;
use Runtime.Web.Hooks.AppHook as WebHook;


class AppHook extends BaseHook
{
	/**
	 * Register hooks
	 */
	void register_hooks()
	{
		this.register(WebHook::ROUTE_AFTER, "routeAfter");
	}
	
	
	/**
	 * Route after
	 */
	void routeAfter(Map params)
	{
		RenderContainer container = params.get("container");
	}
}
```

Register hook in ModuleDescription

```
namespace App;

class ModuleDescription
{
	Vector<Entity> entities() =>
	[
		new Hook("App.Hooks.AppHook"),
	];
}
```