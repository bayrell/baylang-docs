# Настройка PHP проекта

BayLang это технология создания FullStack приложений. Она позволяет компилировать фронтенд компоненты нативно, используя PHP.

Гитхаб: [https://github.com/bayrell/project_php](https://github.com/bayrell/project_php)

Создайте проект через composer
```
wget https://github.com/bayrell/project_php/archive/refs/heads/main.zip -O "project.zip"
unzip project.zip
```

Зайдите в проект:
```
mv project_php-main project
cd project
```


## Docker container для разработки

Соберите докер контейнер:
```
./build.sh test
```

Запустите докер контейнер:
```
docker run -d -p 8000:80 -v ./src:/var/www/html --name app_project app/project:1.0
```


## Сборка проекта

Зайдите в докер контейнер:
```
docker exec -it app_project bash
```

Скомпилируйте проект:
```
cd /var/www/html
composer install
baylang-php make_all
./console.php core:install
```

Автоматическая компиляция проекта после изменения файлов:
```
baylang-php watch
```


## Остановка контейнера

Выполните комадны
```
docker stop app_project
docker rm app_project
```


## Сборка контейнера для продакшн

Версия для продакшн:
```
./build.sh docker
```


## Структура проекта

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