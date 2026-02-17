# Data serialization

The web framework allows you to transfer data from the frontend to the backend and validate it according to defined rules.


## Checking maps

The MapType is used for validating Map structures. You can define rules for each expected key.

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


## Checking vectors

The VectorType is used for validating Vector structures. You define one rule that applies to all elements within the vector.

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


## Checking complex data

For more complex data structures, especially when dealing with nested objects or specific rules for different parts of your data, you can use nested rules.

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

## Checking objects

BayLang objects can implement SerializeInterface to define their own serialization rules.

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


## Serialization

To serialize object use rtl::serialize.

```
User user = new User();
user.name = "User";

Map data = rtl::serialize(user);
```


## Creating own data type

You can implements Runtime.Serializer.BaseType to create custom validation or transformation logic.

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