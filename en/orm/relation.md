# Relation


## Example record

```
namespace App;

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

## Create Relation

```
use Runtime.ORM.Relation;

Relation<Item> relation = new Relation(classof Item);
```


## Create Record

```
Record createRecord(Map data = null);
```

Example:
```
/* Create item */
Record<Item> item = relation.createRecord({
	"name": "Item",
});

/* Or */
Item item = new Item();
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
Relation relation = new Relation(classof Item);
Map post_data = this.filter(this.request.data, new MapData{
	"pk": relation.getPrimaryRules(),
	"item": relation.getItemRules(),
});

/* Get primary key */
Map pk = relation.getPrimaryFilter(post_data.get("item"));
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
async void save(Record item);
```

Delete an object from the database
```
async void delete(Record item);
```


## Updating an object

Update object data from the database. Useful when an object has been saved to the database and you need to retrieve a new version.
```
async void refresh(Record item);
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
async QueryResult<Record> fetchAllRecords(Query q)
```

Get only one line
```
async Map fetchOne(Query q)
```

Get only one Record
```
async Record fetchRecord(Query q)
```

Find rows by filter
```
async QueryResult find(Vector<QueryFilter> filter)
```

Find a Record by filter
```
async Record findRecord(Vector<QueryFilter> filter)
```

Find a Record by Primary Key
```
async Record findByPk(Map pk)
async Record findById(var id)
```

Find or create an object by filter.
```
async Record findOrCreate(Map filter)
```

If the object doesn't exist in the database, a Record instance will be created. However, it won't appear in the database until after save().