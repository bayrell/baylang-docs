# Record

Пример Record:
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

Получить объект из базы
```
use Runtime.ORM.Relation;

Relation<Item> relation = new Relation(classof Item);
Item item = await relation.fetchRecord(
    relation.select().where("id", "=", "1")
);
```

Получить primary key:
```
Map pk = item.getPrimaryKey();
```

Сохранить объект
```
await item.save();
```

Удалить объект:
```
await item.delete();
```

Получить данные объекта:
```
item.all();
```

Получить старые данные объекта:
```
item.old();
```

Получить только определенные поля:
```
item.intersect(["id", "name"]);
```

Установить новые данные:
```
item.assign({
    "name": "Name"
})
```

Проверить изменился ли объект:
```
bool is_changed = item.isChanged();
```

Проверить новый ли объект:
```
bool is_new = item.isNew()
```

Проверить объект был загружен из базы данных:
```
bool is_update = item.isUpdate();
```