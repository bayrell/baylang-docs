# Модели

Модели в BayLang хранят состояние проекта и бизнес логику работы приложения. Важно понимать, что модели это часть фронтенд. Они отвечают как будут храниться данные на клиенте.

Data Transfer Object (DTO) тоже являются моделями.

Очень важно в моделях обеспечивать сериализацию. Сериализация позволяет передавать данные из бэкенд на фронтенд.

Пример модели:
```
namespace App;

use Runtime.BaseModel;
use Runtime.RenderContainer;
use Runtime.Serializer;
use App.ExamplePage;

class PageModel extends BaseModel
{
    string component = classof ExamplePage;
    string name = "";
    
    
    /**
     * Init params
     */
    void initParams(Map params)
    {
        parent(params);
    }
    
    
    /**
     * Init widget
     */
    void initWidget(Map params)
    {
        parent(params);
    }
    
    
    /**
     * Serialize model
     */
    void serialize(Serializer serializer, Map data)
    {
        parent(serializer, data);
        serializer.process(this, "name", data);
    }
    
    
    /**
     * Load data
     */
    async void loadData(RenderContainer container)
    {
        parent(container);
    }
    
    
    /**
     * Build title
     */
    void buildTitle(RenderContainer container)
    {
        this.layout.setPageTitle("Page");
    }
}
```

Когда модель создается, ей передаются параметры. Существуют две функции, которые вызываются в момент создания модели:
- initParams - используется для инициализации параметров модели. Используется для инициализации переменных модели.
- initWidget - инициализация виджетов модели. Обычно используется, чтобы создать другие модели и их настроить.

Функция serialize отвечает за сериализацию данных модели. Сериализация это процесс преобразования класса модели в объект, который готов к передаче. Обычно данные модели передаются из бэкенд во фронтенд. Но это необязательно. Можно также сохранять данные модели в базу данных.

Если модель загружает какие либо данные, то эти данные нужно добавить в функцию сериализации.

Функция loadData загружает данные из бэкенд по api. Вызывается, когда RenderContainer рендерит страницу.

Функция buildTitle устанавливается заголовок страницы.

RenderContainer - это контейнер, который используется приложением в момент инициализации страницы. Он отвечает за поиск маршрута Route и загрузку данных модели.

Переменная component указывает на то, какой компонет должен отображаться вместо с этой моделью.

## Layout

Layout - это глобальная модель всего приложения. Обычно она доступна из модели и шаблона. Обратиться к ней можно через переменную this.layout.

Layout содержит функции такие, как:
- Заголовок страницы
- Текущий роут
- Модели страницы и виджеты
- Список компонентов, используемых в приложении.