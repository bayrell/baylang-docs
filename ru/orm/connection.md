# Connection

## Подключение к базе данных

```
namespace App.Database;

use Runtime.ORM.Database.ConnectionFactory;
use Runtime.ORM.MySQL.ConnectionMySQL;

class DatabaseConnection extends ConnectionFactory
{
	async ConnectionMySQL createConnection()
	{
		ConnectionMySQL conn = new ConnectionMySQL();
		conn.host = @.env("MYSQL_HOST");
		conn.port = @.env("MYSQL_PORT");
		conn.login = @.env("MYSQL_LOGIN");
		conn.password = @.env("MYSQL_PASSWORD);
		conn.database = @.env("MYSQL_DATABASE");
		return conn;
	}
}
```

Регистрация DatabaseConnection:
```
namespace App;

use Runtime.Entity.Entity;

class ModuleDescription
{
	pure string getModuleName() => "App";
	pure string getModuleVersion() = "1";
	pure Map<string> requiredModules() => {
		"Runtime": "*",
	};
	pure Vector<Entity> enities() => [
		new DatabaseConnection(),
	];
}
```