# Dark Theme

To enable the dark theme, you should set the theme_dark class for the body element.

Alternatively, you can set the dark theme via the model:
```
this.layout.theme = "dark";
```

In your CSS, add:
```
/* Smooth transition when switching themes */
transition: background-color var(--transition) var(--transition-type),
		border-color var(--transition) var(--transition-type),
		color var(--transition) var(--transition-type);
```

Or:
```
/* Smooth transition when switching themes */
transition: var(--transition-background);
```

This ensures a smooth theme switch for all interface elements.

The dark theme is determined based on the cookies set. The toggle should set the theme parameter as follows:
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

To enable automatic theme detection, add the following hook to your ModuleDescription:
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