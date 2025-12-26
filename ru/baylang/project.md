# Настройка проекта

Структура проекта:

```
files
src
  app
    Components
    Pages
      IndexPage
        IndexPage.bay
        IndexPageModel.bay
    Routes.bay
    ModuleDescription.bay
  public
    dist
    index.php
.dockerignore
build.sh
dockerfile
project.json
```

- files содержит файлы для Docker контейнера
- src - исходный код проекта
- src/modules - модули проекта
- src/public - document root

Файл project.json
```json
{
    "name": "Project name",
    "description": "Description",
    "license": "MIT",
    "author": "",
    "languages": ["php", "es6"],
    "modules": [
        {
            "src": "src/modules",
            "type": "lib"
        }
    ],
    "assets": [
        {
            "type": "js",
            "dest": "src/public/dist/app.js",
            "modules": [
                "@app"
            ]
        },
        {
            "type": "js",
            "dest": "src/public/dist/runtime.js",
            "modules": [
                "@runtime"
            ]
        }
    ],
    "exclude": [
        "src/vendor"
    ]
}
```

File index.php
```php
<?php

use Runtime\rs;
use Runtime\rtl;
use Runtime\BaseLayout;
use Runtime\Loader;
use Runtime\RenderContainer;
use Runtime\Vector;
use Runtime\Map;

define('BASE_PATH', dirname(__DIR__));
ini_set('display_errors', 'on');
ini_set('html_errors', 'on');
set_time_limit(30);

/* Create loader */
require_once BASE_PATH . "/lib/Runtime/bay/Loader.php";
Loader::add("App", BASE_PATH . "/lib/App/php");
Loader::add("Runtime", BASE_PATH . "/lib/Runtime/php");
Loader::add("Runtime.Widget", BASE_PATH . "/lib/Runtime.Widget/php");
Loader::init();

/* Create context */
rtl::createContext(new Map(["modules"=>new Vector("App")]));

/* Create container and layout */
$container = new RenderContainer();
$layout = $container->createLayout("default");

/* Setup page model */
$layout->setPageModel("App.Components.IndexPage.IndexPageModel");

/* Load data */
$layout->loadData($container);

/* HTML */
?><html lang='<?= rs::escapeHtml($layout->lang) ?>'>
<head>
<title><?= rs::escapeHtml($layout->title) ?></title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style><?= $layout->getStyle() ?></style>
</head>
<body>
<div class="root_container"><?= $container->render() ?></div>
<script src="/assets/vue.runtime.global.js"></script>
<script src="/assets/runtime.js"></script>
<script src="/assets/app.js"></script>
<script>
var app_data = <?= json_encode($container->getData()); ?>;
Runtime.rtl.mount(app_data, document.querySelector(".root_container"), function (result){
    window["app"] = result.get("app");
	window["app_layout"] = result.get("layout");
});
</script>
</body>
</html>
```