# DetectLanguage

Этот хук позволяет автоматически определяеть язык по URL. После определения хук устанавливает параметр `lang` для Layout.

В ModuleDescription добавьте:
```
/* Languages */
DetectLanguage::hook({
	"default_language": "en",
	"allowed_languages": ["en", "ru"],
})
```

Опции:
- allowed_languages - разрешенные языки
- default_language - Это язык по умолчанию, который будет выбран для сайта
- route_match_name - Параметр для Route, который будет отвечать за язык. Обычно это lang

Пример Route:
```
new RouteModel
{
	"uri": "/{lang}/page",
	"name": "app:page",
	"model": "App.Components.Pages.CustomPage.CustomPageModel",
}
```