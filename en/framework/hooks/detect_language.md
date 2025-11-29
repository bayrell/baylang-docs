# DetectLanguage

This hook allows automatic language detection by URL. After the detection, the hook sets the `lang` parameter for the Layout.

In ModuleDescription add:
```
/* Languages */
DetectLanguage::hook({
	"default_language": "en",
	"allowed_languages": ["en", "ru"],
})
```

Options:
- allowed_languages - allowed languages
- default_language - This is the default language that will be selected for the site
- route_match_name - A Route parameter that will be responsible for the language. Usually it’s lang

Example Route:
```
new RouteModel
{
	"uri": "/{lang}/page",
	"name": "app:page",
	"model": "App.Components.Pages.CustomPage.CustomPageModel",
}
```