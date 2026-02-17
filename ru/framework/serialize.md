# Сериализация данных

Веб-фреймворк позволяет передавать данные с фронтенда на бэкенд и проверять их в соответствии с заданными правилами.


## Проверка Map

Параметр MapType используется для проверки структур Map. Для каждого ожидаемого ключа можно определить правила.

```
use Runtime.Unit.AssertException;
use Runtime.Serializer.MapType;
use Runtime.Serializer.StringType;
use Runtime.Serializer.TypeError;

Map data = {
	"name": "User",
};

MapType rules = new MapType{
	"name": new StringType(),
};

Map new_data = serializer.filter(data, errors);
if (errors.count() > 0)
{
	string message = rs::join(", ", TypeError::getMessages(error))
	throw new AssertException(message);
}
```


## Проверка Vector

Параметр VectorType используется для проверки векторных структур. Вы определяете одно правило, которое применяется ко всем элементам внутри вектора.

```
use Runtime.Unit.AssertException;
use Runtime.Serializer.MapType;
use Runtime.Serializer.StringType;
use Runtime.Serializer.TypeError;
use Runtime.Serializer.VectorType;

Map data = {
	"name": "User",
	"fruits": ["apple", "banana", "cherry", "grape", "orange", "watermelon"],
};

MapType rules = new MapType{
	"name": new StringType(),
	"fruits": new VectorType(new StringType()),
};

Vector errors = [];
Map new_data = rules.filter(data, errors);
if (errors.count() > 0)
{
	string message = rs::join(", ", TypeError::getMessages(errors));
	throw new AssertException(message);
}
```


## Проверка сложных данных

Для более сложных структур данных, особенно при работе с вложенными объектами или специфическими правилами для разных частей данных, можно использовать вложенные правила.

```
use Runtime.Unit.AssertException;
use Runtime.Serializer.MapType;
use Runtime.Serializer.StringType;
use Runtime.Serializer.TypeError;
use Runtime.Serializer.VectorType;

Map data = {
	"profile": {
		"name": "User",
		"fruits": ["apple", "banana", "cherry", "grape", "orange", "watermelon"],
	},
	"settings": {
		"theme": "dark",
		"lang": "en",
	},
};

MapType rules = new MapType{
	"profile": new MapType{
		"name": new StringType(),
		"fruits": new VectorType(new StringType()),
	},
	"settings": new MapType{
		"theme": new StringType(),
		"lang": new StringType(),
	}
};

Vector errors = [];
Map new_data = serializer.filter(data, errors);
if (errors.count() > 0)
{
	string message = rs::join(", ", TypeError::getMessages(errors));
	throw new AssertException(message);
}
```

## Проверка объектов

Объекты BayLang могут реализовывать интерфейс SerializeInterface для определения собственных правил сериализации.

```
namespace App.Models;

use Runtime.Unit.AssertException;
use Runtime.Serializer.MapType;
use Runtime.Serializer.ObjectType;
use Runtime.Serializer.StringType;
use Runtime.Serializer.TypeError;
use Runtime.Serializer.VectorType;
use Runtime.SerializeInterface;

class User extends BaseObject implements SerializeInterface
{
	string name = "";
	Vector fruits = [];
	
	
	/**
	 * Serialize object
	 */
	static void serialize(ObjectType rules)
	{
		parent(rules);
		rules.addType("name", new StringType());
		rules.addType("fruits", new VectorType(new StringType()));
	}
}

Map data = {
	"name": "User",
	"fruits": ["apple", "banana", "cherry", "grape", "orange", "watermelon"],
};

User user = new User();
Vector errors = [];
Serializer serializer = rtl::assign(user, data, errors);

if (errors.count() > 0)
{
	string message = TypeError::getMessages(errors);
	throw new AssertException(message);
}
```


## Сериализация

Для сериализации используйте rtl::serialize

```
User user = new User();
user.name = "User";

Map data = rtl::serialize(user);
```


## Создание своего типа данных

Вы можете реализовать интерфейс Runtime.Serializer.BaseType для создания собственной логики проверки или преобразования данных.

```
namespace App.Serializer;

use Runtime.Serializer.BaseType;

class CustomType implements BaseType
{
	/**
	 * Filter value
	 */
	var filter(var value, Vector errors)
	{
		return value;
	}
	
	
	/**
	 * Returns data
	 */
	var serialize(var value)
	{
		return value;
	}
}
```