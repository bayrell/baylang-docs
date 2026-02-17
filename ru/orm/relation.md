# Relation


## Пример Record

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

## Создание Relation

```
use Runtime.ORM.Relation;

Relation<Item> relation = new Relation(classof Item);
```


## Создание Record

```
Record createRecord(Map data = null);
```

Пример:
```
/* Create item */
Item item = relation.createRecord({
	"name": "Item",
});

/* Or */
Item item = new Item();
await item.save();

/* Refresh item */
await item.refresh();
DateTime gmtime_create = item.gmtime_create;
```


## Аннотации

Получает список всех аннотаций для Relation. Аннотации это схема данных.
```
Vector<BaseObject> getAnotations();
```

Получает аннотацию для поля счетчика.
```
AutoIncrement getAutoIncrement();
```

Получает список первичных ключей для Relation
```
Vector<string> getPrimaryKeys();
```

Получат первичный ключ по данным
```
Map getPrimaryKey(Map data);
```

Получает фильтр для первичного ключа. Параметр use_full_key добавляет названию таблицы к названию поля.
```
Vector<QueryFilter> getPrimaryFilter(Map data, bool use_full_key = true);
```

Пример:
```
Relation relation = new Relation(classof Item);
Map post_data = this.filter(this.request.data, new MapData{
	"pk": relation.getPrimaryRules(),
	"item": relation.getItemRules(),
});

/* Get primary key */
Map pk = relation.getPrimaryFilter(post_data.get("item"));
```


## Конвертация данных

Подготовить данные к сохранению в базу данных
```
async Map toDatabase(Map data);
```

Преобразовать данные из базы данных в примитивные объекты
```
async Map fromDatabase(Map data);
```


## Создание и удаление объекта


Сохранить или создать объект в базе данных
```
async void save(Record item);
```

Удалить объект из базы данных
```
async void delete(Record item);
```


## Обновление объекта

Обновить данные объекта из базы данных. Полезно, когда объект был сохранен в базу данных и нужно получить его новую версию.
```
async void refresh(Record item);
```


## Запросы в базу данных


Создание нового экземпляра запроса
```
Query query();
Query select(Vector fields = null);
```

Получить результат запроса
```
async QueryResult<Map> fetchAll(Query q)
```

Получить результат запроса в виде Record
```
async QueryResult<Record> fetchAllRecords(Query q)
```

Получить только одну строчку
```
async Map fetchOne(Query q)
```

Получить только один Record
```
async Record fetchRecord(Query q)
```

Найти строчки по фильтру
```
async QueryResult find(Vector<QueryFilter> filter)
```

Найти Record по фильтру
```
async Record findRecord(Vector<QueryFilter> filter)
```

Найти Record по primary key
```
async Record findByPk(Map pk)
async Record findById(var id)
```

Найти или создать объект по фильтру.
```
async Record findOrCreate(Map filter)
```

Если объекта в базе нет, то будет создан экземпляр Record. Но в базе он появится, только после save()