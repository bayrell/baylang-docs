# Record

Example:
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

Get object from database
```
use Runtime.ORM.Relation;

Relation<Item> relation = new Relation(classof Item);
Record<Item> item = await relation.fetchRecord(
    relation.select().where("id", "=", "1")
);
```

Get primary key:
```
Map pk = item.getPrimaryKey();
```

Save item:
```
await item.save();
```

Delete item:
```
await item.delete();
```

Get objet data:
```
item.all();
```

Get old object data:
```
item.old();
```

Get only specific fields:
```
item.intersect(["id", "name"]);
```

Assign new data:
```
item.assign({
    "name": "Name"
})
```

Returns true if object is changed:
```
bool is_changed = item.isChanged();
```

Check if object is new:
```
bool is_new = item.isNew()
```

Check if object is loaded from database:
```
bool is_update = item.isUpdate();
```