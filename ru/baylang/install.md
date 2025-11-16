# Установка BayLang

Установка
```
cd ~
npm install --save bay-lang@latest
```

Проверка установленной версии:
```
bay-lang-nodejs version
```

## Настройки проекта

Создайте файл project.json в корне проекта

```
{
    "name": "Project name",
    "description": "Description",
    "license": "MIT",
    "author": "",
    "languages": ["php", "es6"],
    "modules": [],
    "assets": [],
    "exclude": []
}
```

## Компиляция проекта

Сборка всего проекта:
```bash
bay-lang-nodejs make_all
```

Для того, чтобы запустить автоматическую сборку проекта, при изменении файлов, выполните команду:
```bash
bay-lang-nodejs watch
```