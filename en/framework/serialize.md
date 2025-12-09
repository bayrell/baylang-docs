# Data serialization

Web framework allows you to transfer data from the frontend to the backend.


## Checking strings

```
use Runtime.Serializer;
use Runtime.Serializer.StringType;

Map data = {
	"name": "User",
};

Serializer serializer = new Serializer();
serializer.addType(new StringType());

Map new_data = serializer.filter(data);
if (not serializer.correct())
{
	throw new AssertException(serializer.getErrorMessage());
}
```


## Checking vectors

```
use Runtime.Serializer;
use Runtime.Serializer.StringType;
use Runtime.Serializer.VectorType;

Map data = {
	"name": "User",
	"fruits": ["apple", "banana", "cherry", "grape", "orange", "watermelon"],
};

Serializer serializer = new Serializer();
serializer.addType("name", new StringType());
serializer.addType("fruits", new VectorType(new StringType()));

Map new_data = serializer.filter(data);
if (not serializer.correct())
{
	throw new AssertException(serializer.getErrorMessage());
}
```


## Checking complex data

```
use Runtime.Serializer;
use Runtime.Serializer.MapType;
use Runtime.Serializer.StringType;
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

Serializer serializer = new Serializer();
serializer.addType("profile", new MapType{
	"name": new StringType(),
	"fruits": new VectorType(new StringType()),
});
serializer.addType("settings", new MapType{
	"theme": new StringType(),
	"lang": new StringType(),
});

Map new_data = serializer.filter(data);
if (not serializer.correct())
{
	throw new AssertException(serializer.getErrorMessage());
}
```

## Checking objects

```
namespace App.Models;

use Runtime.SerializeInterface;
use Runtime.Serializer;

class User extends BaseObject implements SerializeInterface
{
	string name = "";
	Vector fruits = [];
	
	
	/**
	 * Serialize object
	 */
	void serialize(Serializer serializer)
	{
		parent(serialize);
		serializer.addType("name", new StringType());
		serializer.addType("fruits", new VectorType(new StringType()));
	}
}

Map data = {
	"name": "User",
	"fruits": ["apple", "banana", "cherry", "grape", "orange", "watermelon"],
};

User user = new User();
Serializer serializer = rtl::apply(user, data);

if (not serializer.correct())
{
	throw new AssertException(serializer.getErrorMessage());
}
```


## Serialization

```
User user = new User();
user.name = "User";

Map data = rtl::serialize(user);
```


## Creating own data type

```
namespace App.Serializer;

use Runtime.Serializer.BaseType;

class CustomType extends BaseType
{
	/**
	 * Filter value
	 */
	var filter(var value, Vector errors, var old_value)
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