# Setup PHP project

BayLang Technology allows you to create FullStack projects and compile frontend components using native PHP.

Github: [https://github.com/bayrell/project_php](https://github.com/bayrell/project_php)

Create a project using composer
```
wget https://github.com/bayrell/project_php/archive/refs/heads/main.zip -O "project.zip"
unzip project.zip
```

Change folder:
```
mv project_php-main project
cd project
```


## Docker container for developer

Build test docker container:
```
./build.sh test
```

Run docker container:
```
docker run -d -p 8000:80 -v ./src:/var/www/html --name app_project app/project:1.0
```


## Compile project

Enter to docker container:
```
docker exec -it app_project bash
```

Run commands:
```
cd /var/www/html
composer install
baylang-php make_all
./console.php core:install
```

Watch project changes:
```
baylang-php watch
```

## Stop container

Run command
```
docker stop app_project
docker rm app_project
```


## Build prod docker container

Run command:
```
./build.sh docker
```


## Project structure

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
    dist
    index.php
.dockerignore
build.sh
dockerfile
project.json
```

- files contains files for the Docker container
- src - project source code
- src/modules - project modules
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
