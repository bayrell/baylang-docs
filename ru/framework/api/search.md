# Search

```
namespace App.Api;

use Runtime.ORM.Query;
use Runtime.Web.Annotations.ApiMethod;
use Runtime.Widget.Api.SearchApi;
use App.Database.Item;

class ItemSearchApi extends SearchAp
{
	/**
	 * Returns api name
	 */
	pure string getApiName() => "app.item";
	
	
	/**
	 * Returns relation name
	 */
	string getRelationName() => classof Item;
	
	
	/**
	 * Returns item fields
	 */
	void getItemFields() => [
		"id",
		"name"
	];
	
	
	/**
	 * Build Query
	 */
	async void buildQuery(Query q)
	{
	}
	
	
	/**
	 * Action search
	 */
	@ApiMethod{ "name": "search" }
	async void actionSearch()
	{
		await parent();
	}
}
```


## SaveApi

```
namespace App.Api;

use Runtime.Widget.Api.SaveApi;

class ItemSaveApi extends SaveApi
{
	/**
	 * Returns api name
	 */
	pure string getApiName() => "app.item";
	
	
	/**
	 * Returns relation name
	 */
	string getRelationName() => classof Item;
	
	
	/**
	 * Returns save rules
	 */
	Vector<BaseRule> rules() => [];
	
	
	/**
	 * Returns item rules
	 */
	void getItemRules(MapType rules)
	{
	}
	
	
	/**
	 * Returns item fields
	 */
	Vector<string> getItemFields() => [];
	
	
	/**
	 * Build query
	 */
	async void buildQuery(Query Q)
	{
	}
	
	
	/**
	 * Save action
	 */
	@ApiMethod{ "name": "save" }
	async void actionSave()
	{
		await parent();
	}
	
	
	/**
	 * Delete action
	 */
	@ApiMethod{ "name": "delete" }
	async void actionDelete()
	{
		await parent();
	}
}
```