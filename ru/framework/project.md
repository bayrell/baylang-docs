# Настройка проекта

Пример PHP проекта доступен по адресу [https://github.com/bayrell/project_php](https://github.com/bayrell/project_php)

**Структура проекта**

```
files
src
  app
	Components
	  Blocks
		CSS.bay
		Scripts.bay
	  Layout
		DefaultLayout.bay
		DefaultLayoutModel.bay
	  Pages
		IndexPage
		  IndexPage.bay
		  IndexPageModel.bay
	  Routes.bay
	ModuleDescription.bay
  public
	assets
	index.php
  project.json
.dockerignore
build.sh
Dockerfile
```

## ModuleDescription

ModuleDescription - это главный файл модуля. Его задача объявить зависимости и настройки модуля.

Пример:
```
namespace App;

use Runtime.Entity.Hook;
use Runtime.Web.Annotations.Route;
use Runtime.Web.Hooks.PageNotFound;
use Runtime.Web.Hooks.Components;
use Runtime.Web.Hooks.SetupLayout;


class ModuleDescription
{
	/**
	 * Returns module name
	 */
	pure string getModuleName() => "App";
	
	
	/**
	 * Returns module version
	 */
	pure string getModuleVersion() => "0.0.1";
	
	
	/**
	 * Returns required modules
	 * @return Map<string>
	 */
	pure Dict<string> requiredModules() =>
	{
		"Runtime.Web": "*",
		"Runtime.Widget": "*",
	};
	
	
	/**
	 * Returns enities
	 */
	pure Collection<Dict> entities() =>
	[		
		/* Setup layout */
		SetupLayout::hook({
			"default": "App.Components.Layout.DefaultLayoutModel",
		}),
		
		/* Components */
		Components::hook([
			"App.Components.Blocks.CSS",
		]),
		Components::footer([
			"App.Components.Blocks.Script"
		]),
		
		PageNotFound::hook("App.Components.Pages.NotFoundPage.NotFoundPageModel"),
		
		#ifdef BACKEND then
		new Route("App.Components.Pages.Routes"),
		#endif
	];
}
```

Методы:
- getModuleName - Название модуля
- getModuleVersion - Версия модуля
- requiredModules - Модули зависимости
- entities - настройки модуля

Настройки:
- SetupLayout - настройка Layout. Содержит информацию о модели layout, которая должна быть инициирована по layout_name
- Components::hook - добавляет компоненты в зависимости
- Components::footer - добавляет компоненты в footer сайта
- PageNotFound::hook - устанавливает модель для страницы не найдена
- Route - список маршрутов сайта

Более подробно список настроек можно узнать в [Hooks](hooks)


## Настройка project.json

Это файл, который содержит настройки проекта и правила компиляции

```
{
	"name": "Project name",
	"description": "Description",
	"license": "MIT",
	"author": "",
	"languages": ["php", "es6"],
	"modules": [
		{
			"src": "app",
			"type": "module"
		},
		{
			"src": "lib",
			"type": "folder"
		}
	],
	"assets": [
		{
			"type": "js",
			"dest": "public/assets/app.js",
			"modules": [
				"@app"
			]
		}
	],
	"exclude": []
}
```

Параметры:
- name - Название проекта
- description - Описание проекта
- languages - Языки, в которые нужно компилировать проект
- modules - Список модулей проекта
- assets - bundle, которые будут собираться


## Настройка module.json

Этот файл содержит настройки модуля

```
{
	"name": "App",
	"assets": [
		"Components/Blocks/CSS.bay",
		"Components/Blocks/Script.bay",
		"Components/Layout/DefaultLayout.bay",
		"Components/Layout/DefaultLayoutModel.bay",
		"Components/Pages/IndexPage/IndexPage.bay",
		"Components/Pages/IndexPage/IndexPageModel.bay",
		"Components/Pages/NotFoundPage/NotFoundPage.bay",
		"Components/Pages/NotFoundPage/NotFoundPageModel.bay",
		"ModuleDescription.bay"
	],
	"src": "./",
	"dest":
	{
		"php": "../source/php",
		"es6": "../source/es6"
	},
	"groups": [
		"app"
	],
	"exclude": [
		"vendor"
	]
}
```

Параметры:
- name - Название модуля
- assets - Списов файлов, которые нужно включить в bundle
- src - Название папки с исходным кодом на baylang
- dest - Путь, куда компилировать файлы
- groups - Список групп модуля.
- exclude - Какие папки исключить

