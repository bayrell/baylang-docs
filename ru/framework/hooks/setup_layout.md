# SetupLayout

Установка Layout для всего сайта. Позволяет зарегистрировать имена layout и определить для каждого из них модель.

Пример:
```
/* Setup layout */
SetupLayout::hook({
	"default": "App.Components.Layout.DefaultLayoutModel",
}),
```