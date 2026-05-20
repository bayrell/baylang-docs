# Миграции базы данных

Пример миграции:
```
namespace App.Database.Migrations;

use Runtime.ORM.BaseMigration;
use Runtime.ORM.Query;

class App extends BaseMigration
{
	/**
	 * Returns migration name
	 */
	string name = "app_2026";
	
	
	/**
	 * Returns required
	 */
	Vector<string> required = [];
	
	
	/**
	 * Register migration
	 */
	Vector<string> migrations =
	[
		"create_products",
	];
	
	
	/**
	 * Create products migration
	 */
	BaseMigration create_products() => new BaseMigration
	{
		"up": async void ()
		{
			string table_name = this.connection.getTableName("products");
			this.comment("Create table " ~ table_name);
			await this.executeSQL(
				"CREATE TABLE `" ~ table_name ~ "` (
					`id` BIGINT NOT NULL AUTO_INCREMENT,
					`type` VARCHAR(255) NOT NULL DEFAULT '',
					`uid` VARCHAR(255) NOT NULL DEFAULT '',
					`name` VARCHAR(255) NOT NULL DEFAULT '',
					`gmtime_add` DATETIME NOT NULL,
					`gmtime_edit` DATETIME NOT NULL,
					PRIMARY KEY (`id`),
					UNIQUE KEY `uid` (`uid`),
					FULLTEXT `search` (`search`)
				) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"
			);
		},
		"down": async void ()
		{
			string table_name = this.connection.getTableName("products");
			this.comment("Drop table " ~ table_name);
			await this.executeSQL(
				"DROP TABLE IF EXISTS `" ~ table_name ~ "`"
			);
		},
	};
}
```

Зарегистрируйте миграцию в ModuleDescription:

```
use Runtime.ORM.Annotations.Migration;

class ModuleDescription
{
	void entities() =>
	[
		new Migration("App.Database.Migrations.App"),
	];
}
```