# SearchApi и SaveApi

Эта документация описывает использование базовых API-модулей `SearchApi` и `SaveApi`, предназначенных для быстрой разработки RESTful API-endpoints. Эти модули позволяют создавать, читать, обновлять и удалять (CRUD) данные с минимальным количеством кода, предоставляя гибкие механизмы для валидации, фильтрации и преобразования данных.


## Пример базы данных


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


## SearchApi

Модуль `SearchApi` предоставляет базовый функционал для создания API-endpoints, предназначенных для поиска и получения данных из базы данных. Он разработан для гибкой настройки запросов и обработки результатов.

**Ключевые возможности**

- Автоматическое формирование запросов: Построение запросов к базе данных на основе параметров API-запроса.
- Валидация входящих данных: Проверка параметров запроса (фильтры, лимиты, страницы).
- Гибкое определение полей: Возможность указать, какие поля сущности должны быть возвращены.
- Кастомизация запросов: Механизмы для добавления сложных условий фильтрации, сортировки и джойнов.
- `search`: Поиск и получение списка записей с пагинацией.
- `item`: Получение одной записи по первичному ключу.


## Методы SearchApi

- **getApiName** Используется для маршрутизации. Возвращает уникальное имя для вашего API.
- **getRecordName** Возвращает имя класса сущности (Record), с которой работает AP
- **getMiddleware** Определяет список Middleware для аутентификации, авторизации и т.д.
- **getDataRules** Определяет правила валидации для входных данных запроса (например, фильтров).
- **getItemFields** Определяет список полей, которые будут включены в результат поиска. Если список пуст, возвращаются все поля сущности.
- **buildQuery** Позволяет изменять объект Query перед выполнением поиска. Здесь можно добавить условия фильтрации, сортировки, джойны и другие параметры запроса.
- **convertItem** Позволяет преобразовать данные каждой записи перед их возвратом в ответе.


## Пример SearchApi

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

Модуль SaveApi предоставляет базовый функционал для создания API-endpoints, предназначенных для сохранения (создания и обновления) и удаления данных в базе данных. Он обеспечивает надежную валидацию данных, обработку CRUD-операций и гибкую настройку логики через систему хуков.

**Ключевые возможности**

- Автоматическое сохранение/обновление: Распознавание, нужно ли создавать новую запись или обновлять существующую, на основе наличия первичного ключа.

- Строгая валидация данных: Применение правил валидации к полям каждой записи.

- Управление полями: Определение разрешенных к сохранению полей и полей для возврата в ответе.

- Хуки жизненного цикла: Точки расширения (onSaveBefore, onSaveAfter, onDeleteBefore, onDeleteAfter) для встраивания бизнес-логики.

Два основных действия:
- save: Создание или обновление записи.
- delete: Удаление записи по первичному ключу.


## Методы SaveApi

- getApiName(): Возвращает уникальное имя для вашего API.

- getRecordName(): Возвращает имя класса Record (сущности), с которой работает API.

- getMiddleware(): Определяет список промежуточного ПО (Middleware) для обработки запросов.

- getDataRules(MapType rules): Определяет правила валидации для входных параметров запроса, которые не являются полями самой записи (например, foreign_key).

- getItemRules(MapType rules): Важнейший метод для определения правил валидации и фильтрации для полей самой записи (item), которые приходят от клиента.

- getItemFields(): Возвращает Vector<string> с именами полей, которые должны быть возвращены в ответе после сохранения.

- getSaveFields(): Возвращает Vector<string> с именами полей, разрешенных к сохранению. Это критически важно для безопасности, чтобы не позволить клиенту изменять несанкционированные поля. Если метод возвращает null, сохраняются все валидные поля.

- convertItem(Map item): Позволяет преобразовать данные записи перед их возвратом в ответе.

- buildQuery(Query q): Изменяет объект Query перед поиском существующей записи в методах save и delete.

- onSaveBefore(): Хук, вызываемый перед сохранением записи (созданием/обновлением). Идеально для автоматической установки полей (gmtime_add, gmtime_edit), или выполнения бизнес-логики.

- onSaveAfter(): Хук, вызываемый после успешного сохранения записи.

- onDeleteBefore(): Хук, вызываемый перед удалением записи. Идеально для проверки прав доступа, наличия связанных данных.

- onDeleteAfter(): Хук, вызываемый после успешного удаления записи.


## Пример использования

Продолжая пример с сущностью Item, для создания API для сохранения и удаления товаров, мы можем определить следующий класс:

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
					"name": "Имя уже используется."
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
			throw new ApiError(new RuntimeException("Невозможно удалить запись, так как существуют связанные заказы."));
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