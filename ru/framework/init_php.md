# Инициализаия PHP проекта

Файл init.php содержит настройку контекста

```
<?php

use Runtime\Map;
use Runtime\Vector;
use Runtime\Entity\Provider;

include "vendor/autoload.php";

function createContext($app, $argv = null)
{
	$modules = new Vector("App");
	$params = new Map([
		"base_path" => __DIR__,
		"providers" => new Vector(
			new Provider("app", $app),
		),
		"modules" => $modules
	]);
	
	if ($app == "Runtime.Console.App")
	{
		$modules->push("Runtime.Core");
		$modules->push("Runtime.Console");
		$params->set("cli_args", Vector::create($argv));
	}
	$context = \Runtime\rtl::createContext($params);
	$context->start();
	return $context;
}
```

В этом файле можно добавить модули и дополнительные параметры.

Файл index.php содержит точку входа document root

```
<?php

/* Init */
include dirname(__DIR__) . "/init.php";

/* Run app */
$context = createContext("Runtime.Web.BasePHP");
$context->provider("app")->main();
```

Фай console.php содержит точку входа для терминала

```
#!/usr/bin/env php
<?php

include "init.php";

/* Run app */
$context = createContext("Runtime.Console.App", $argv);
$context->provider("app")->main();
```