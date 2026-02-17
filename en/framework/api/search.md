# SearchApi and SaveApi

This documentation describes the use of the basic API modules `SearchApi` and `SaveApi`, designed for rapid development of RESTful API endpoints. These modules allow you to create, read, update, and delete (CRUD) data with a minimal amount of code, providing flexible mechanisms for validation, filtering, and data transformation.


## Example database

```
namespace App.Database;

use Runtime.BaseObject;
use Runtime.ORM.Record;
use Runtime.ORM.Annotations.AutoIncrement;
use Runtime.ORM.Annotations.BigIntType;
use Runtime.ORM.Annotations.Primary;
use Runtime.ORM.Annotations.StringType;


class Item extends Record
{
	/**
     * Returns table name
     */
    pure string getTableName() => "forms";
	
	
	/**
	 * Returns table schema
	 */
	pure memorize Collection<BaseObject> schema() =>
	[
		/* Fields */
		new BigIntType{"name": "id"},
		new StringType{"name": "name"},
		new StringType{"name": "description"},
		new BigIntType{"name": "category_id"},
		new DateTimeType{"name": "gmtime_add", "autocreate": true},
		new DateTimeType{"name": "gmtime_edit", "autoupdate": true},
		
		/* Index */
		new AutoIncrement{"name": "id"},
		new Primary{"keys": ["id"]},
	];
}
```


## Search

The `SearchApi` module provides basic functionality for creating API endpoints designed for searching and retrieving data from a database. It is developed for flexible query configuration and result processing.

**Key Features**

- **Automatic Query Generation**: Building database queries based on API request parameters.
- **Input Data Validation**: Checking request parameters (filters, limits, pages).
- **Flexible Field Definition**: Ability to specify which entity fields should be returned.
- **Query Customization**: Mechanisms for adding complex filtering conditions, sorting, and joins.
- `search`: Searching and retrieving a list of records with pagination.
- `item`: Retrieving a single record by its primary key.


## Methods SearchApi

- **getApiName**: Used for routing. Returns a unique name for your API.
- **getRecordName**: Returns the name of the entity class (Record) that the API works with.
- **getMiddleware**: Defines a list of Middleware for authentication, authorization, etc.
- **getDataRules**: Defines validation rules for incoming request data (e.g., filters).
- **getItemFields**: Defines a list of fields that will be included in the search result. If the list is empty, all entity fields are returned.
- **buildQuery**: Allows modifying the Query object before performing the search. Here you can add filtering conditions, sorting, joins, and other query parameters.
- **convertItem**: Allows transforming the data of each record before it is returned in the response.


## SearchApi Example

```
namespace App.Api;

use Runtime.ORM.Query;
use Runtime.Web.Annotations.ApiMethod;
use Runtime.Widget.Api.SearchApi;
use App.Database.Item;

class ItemSearchApi extends SearchApi
{
	/**
	 * Returns api name
	 */
	pure string getApiName() => "app.item";
	
	
	/**
	 * Returns record name
	 */
	pure string getRecordName() => classof Item;
	
	
	/**
	 * Returns middleware
	 */
	Vector<Middleware> getMiddleware() => [];
	
	
	/**
	 * Returns data rules
	 */
	void getDataRules(MapType rules)
	{
	}
	
	
	/**
	 * Returns item fields
	 */
	Vector<string> getItemFields() =>
	[
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
	
	
	/**
	 * Action item
	 */
	@ApiMethod{ "name": "item" }
	async void actionItem()
	{
		await parent();
	}
}
```


## SaveApi

The `SaveApi` module provides basic functionality for creating API endpoints designed for saving (creating and updating) and deleting data in a database. It ensures robust data validation, handles CRUD operations, and offers flexible logic configuration through a hook system.

**Key Features**

-   **Automatic Save/Update**: Recognizing whether to create a new record or update an existing one based on the presence of a primary key.
-   **Strict Data Validation**: Applying validation rules to the fields of each record.
-   **Field Management**: Defining fields allowed for saving and fields to be returned in the response.
-   **Lifecycle Hooks**: Extension points (`onSaveBefore`, `onSaveAfter`, `onDeleteBefore`, `onDeleteAfter`) for embedding business logic.

Two main actions:
-   `save`: Creating or updating a record.
-   `delete`: Deleting a record by its primary key.


## Methods SaveApi

-   `getApiName()`: Returns a unique name for your API.
-   `getRecordName()`: Returns the name of the Record class (entity) that the API works with.
-   `getMiddleware()`: Defines a list of Middleware for processing requests.
-   `getDataRules(MapType rules)`: Defines validation rules for incoming request parameters that are not fields of the record itself (e.g., `foreign_key`).
-   `getItemRules(MapType rules)`: The most important method for defining validation and filtering rules for the record's own fields (`item`) coming from the client.
-   `getItemFields()`: Returns `Vector<string>` with the names of the fields that should be returned in the response after saving.
-   `getSaveFields()`: Returns `Vector<string>` with the names of the fields allowed to be saved. This is critically important for security, to prevent clients from modifying unauthorized fields. If the method returns null, all valid fields are saved.
-   `convertItem(Map item)`: Allows transforming the record data before it is returned in the response.
-   `buildQuery(Query q)`: Modifies the Query object before searching for an existing record in the `save` and `delete` methods.
-   `onSaveBefore()`: Hook called before saving a record (creation/update). Ideal for automatically setting fields (`gmtime_add`, `gmtime_edit`) or executing business logic.
-   `onSaveAfter()`: Hook called after a successful record save.
-   `onDeleteBefore()`: Hook called before deleting a record. Ideal for checking access rights, or for the presence of related data.
-   `onDeleteAfter()`: Hook called after a successful record delete.


## Example SaveApi

Continuing the example with the `Item` entity, to create an API for saving and deleting items, we can define the following class:

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
	 * Returns record name
	 */
	pure string getRecordName() => classof Item;
	
	
	/**
	 * Returns middleware
	 */
	Vector<Middleware> getMiddleware() => [];
	
	
	/**
	 * Returns save rules
	 */
	Vector<BaseRule> rules() => [];
	
	
	/**
	 * Returns data rules
	 */
	void getDataRules(MapType rules)
	{
	}
	
	
	/**
	 * Returns item rules
	 */
	void getItemRules(MapType rules)
	{
		rules.addType("id", new IntegerType());
		rules.addType("name", new Required());
		rules.addType("name", new StringType());
		rules.addType("description", new StringType());
		rules.addType("category_id", new IntegerType());
	}
	
	
	/**
	 * Returns item fields
	 */
	Vector<string> getItemFields() =>
	[
		"id"
		"name",
		"description",
		"category_id",
		"gmtime_add",
		"gmtime_edit",
	];
	
	
	/**
	 * Build query
	 */
	async void buildQuery(Query q)
	{
		await parent(q);
		
		if (this.foreign_key && this.foreign_key.has("category_id"))
		{
			q.where("category_id", "=", this.foreign_key.get("category_id"));
		}
	}
	
	
	/**
	 * Save before
	 */
	async void onSaveBefore()
	{
		await parent();
		
		/* Check unique */
		Query q = this.relation.select()
			.where("name", "=", this.item.get("name"));
		if (this.item.isExists())
		{
			q.where("id", "!=", this.item.get("id"));
		}
		
		Record existing_item = await this.relation.fetchRecord(q);
		if (existing_item)
		{
			throw new ApiError(new FieldException({
				"error": {
					"name": "Name is already in use."
				}
			}));
		}
	}
	
	
	/**
	 * Save after
	 */
	async void onSaveAfter()
	{
		await parent();
	}
	
	
	/**
	 * Delete before
	 */
	async void onDeleteBefore()
	{
		await parent();
		
		/* Запрет удаления, если есть связанные заказы */
		if (this.item.get("has_orders"))
		{
			throw new ApiError(new RuntimeException("Cannot delete record because there are related orders.));
		}
	}
	
	
	/**
	 * Delete after
	 */
	async void onDeleteAfter()
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