# Relation


## Relation example

```
namespace App;

use Runtime.ORM.Relation;
use Runtime.ORM.Record;

class Item extends Relation
{
	/**
     * Returns table name
     */
    pure string getTableName() => "items";
	
	
	/**
     * Returns table schema
     */
    pure memorize Collection<BaseObject> schema() =>
	[
		/* Fields */
		new BigIntType{"name": "id"},
		new StringType{"name": "name"},
		new DateTimeType{"name": "gmtime_create", "autocreate": true},
		new DateTimeType{"name": "gmtime_update", "autoupdate": true},
		
		/* Index */
		new AutoIncrement{"name": "id"},
		new Primary{"keys": ["id"]},
	];
}
```


## Create record

```
Record<Relation> createRecord(Map data = null);
```

Example:
```
/* Create item */
Item relation_item = new Item();
Record<Item> item = relation_item.createRecord({
	"name": "Item",
});
await item.save();

/* Refresh item */
await item.refresh();
DateTime gmtime_create = item.gmtime_create;
```


## Annotation

Gets a list of all annotations for a Relation. Annotations are the data schema.
```
Vector<BaseObject> getAnotations();
```

Gets the annotation for the counter field.
```
AutoIncrement getAutoIncrement();
```

Gets a list of primary keys for a Relation
```
Vector<string> getPrimaryKeys();
```

Get the primary key from the data
```
Map getPrimaryKey(Map data);
```

Gets a filter for the primary key. The use_full_key parameter appends the table name to the field name.
```
Vector<QueryFilter> getPrimaryFilter(Map data, bool use_full_key = true);
```

Example
```
Relation item = new Item();
Map post_data = this.filter(this.request.data, new MapData{
	"pk": item.getPrimaryRules(),
	"item": item.getItemRules(),
});

/* Get primary key */
Map pk = relation_item.getPrimaryFilter(post_data.get("item"));
```

## Data conversion

Prepare data for saving to the database
```
async Map toDatabase(Map data);
```

Convert data from a database into primitive objects
```
async Map fromDatabase(Map data);
```


## Creating and deleting an object

Save or create an object in the database
```
async void save(Record<Relation> item);
```

Delete an object from the database
```
async void delete(Record<Relation> item);
```


## Updating an object

Update object data from the database. Useful when an object has been saved to the database and you need to retrieve a new version.
```
async void refresh(Record<Relation> item);
```


## Database queries

Creating a new query instance
```
Query query();
Query select(Vector fields = null);
```

Get the query result
```
async QueryResult<Map> fetchAll(Query q)
```

Get the query result as a Record
```
async QueryResult<Record<Relation>> fetchAllRecords(Query q)
```

Get only one line
```
async Map fetchOne(Query q)
```

Get only one Record
```
async Record<Relation> fetchRecord(Query q)
```

Find rows by filter
```
async QueryResult find(Vector<QueryFilter> filter)
```

Find a Record by filter
```
async Record<Relation> findRecord(Vector<QueryFilter> filter)
```

Find a Record by Primary Key
```
async Record<Relation> findByPk(Map pk)
async Record<Relation> findById(var id)
```

Find or create an object by filter.
```
async Record<Relation> findOrCreate(Map filter)
```

If the object doesn't exist in the database, a Record instance will be created. However, it won't appear in the database until after save().