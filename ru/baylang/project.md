# Настройка проекта

Структура проекта:

```
files
src
  modules
    App
    Runtime
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
```
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