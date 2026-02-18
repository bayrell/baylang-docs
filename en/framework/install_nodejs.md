# Install BayLang on NodeJS

Install
```
cd ~
npm install --save bay-lang@latest
```

Check verson:
```
baylang-nodejs version
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

## Compile project

Build all project:
```bash
baylang-nodejs make_all
```

Run command to watch changes and automatic build project:
```bash
baylang-nodejs watch
```