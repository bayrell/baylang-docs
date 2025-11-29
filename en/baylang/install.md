# BayLang install

Install
```
cd ~
npm install --save bay-lang@latest
```

Check verson:
```
bay-lang-nodejs version
```

## Project settings

Create file project.json in the root of the project
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

Build all project:
```bash
bay-lang-nodejs make_all
```

Run command to watch changes and automatic build project:
```bash
bay-lang-nodejs watch
```