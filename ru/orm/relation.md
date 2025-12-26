# Relation


## Пример Relation

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


## Создание Record

```
Record<Relation> createRecord(Map data = null);
```

Пример:
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
Relation item = new Item();
Map post_data = this.filter(this.request.data, new MapData{
	"pk": item.getPrimaryRules(),
	"item": item.getItemRules(),
});

/* Get primary key */
Map pk = relation_item.getPrimaryFilter(post_data.get("item"));
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
async void save(Record<Relation> item);
```

Удалить объект из базы данных
```
async void delete(Record<Relation> item);
```


## Обновление объекта

Обновить данные объекта из базы данных. Полезно, когда объект был сохранен в базу данных и нужно получить его новую версию.
```
async void refresh(Record<Relation> item);
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
async QueryResult<Record<Relation>> fetchAllRecords(Query q)
```

Получить только одну строчку
```
async Map fetchOne(Query q)
```

Получить только один Record
```
async Record<Relation> fetchRecord(Query q)
```

Найти строчки по фильтру
```
async QueryResult find(Vector<QueryFilter> filter)
```

Найти Record по фильтру
```
async Record<Relation> findRecord(Vector<QueryFilter> filter)
```

Найти Record по primary key
```
async Record<Relation> findByPk(Map pk)
async Record<Relation> findById(var id)
```

Найти или создать объект по фильтру.
```
async Record<Relation> findOrCreate(Map filter)
```

Если объекта в базе нет, то будет создан экземпляр Record. Но в базе он появится, только после save()