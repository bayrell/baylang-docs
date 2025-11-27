# Темная тема

Для темной темы следует установить для body класс theme_dark.

Либо установить темную тему, через модель:
```
this.layout.theme = "dark";
```

В CSS добавьте:
```
/* Плавный переход при смене темы */
transition: background-color var(--transition) var(--transition-type),
		border-color var(--transition) var(--transition-type),
		color var(--transition) var(--transition-type);
```

Либо:
```
/* Плавный переход при смене темы */
transition: var(--transition-background);
```

Это нужно для плавного переключение темы для всех элементов интерфейса.

Темная тема определяется в зависимости от установленных кук. Переключатель должен установить параметр темы:
```
void setTheme(string theme)
{
    this.layout.theme = theme;
    if (theme == "dark")
	{
		document.body.classList.add("theme_dark");
		document.body.classList.remove("theme_light");
	}
	else
	{
		document.body.classList.add("theme_light");
		document.body.classList.remove("theme_dark");
	}
    document.cookie = "theme=" ~ theme ~ "; path=/; max-age=31536000";
}
void toggleTheme()
{
    bool is_light = this.layout.theme == "light";
    string theme_name = not is_light ? "light" : "dark";
    this.setTheme(theme_name);
}
```

Чтобы включить автоматическое определение темы, добавьте в ModuleDescription хук:
```
class ModuleDescription
{
    pure Collection<Dict> entities() =>
    [
        #ifdef BACKEND then
        new Hook("Runtime.Web.Hooks.ThemeDetect"),
        #endif
    ];
}
```