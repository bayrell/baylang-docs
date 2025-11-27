# Components

Регистрирует компоненты в системе. Иногда нужно добавить дополнительные компоненты в системе.

Добавление компонентов в CSS стили:
```
/* Components */
Components::hook([
	"App.Components.Blocks.CSS",
	"App.Components.Pages.IndexPage.IndexPage",
	"App.Components.Pages.NotFoundPage.NotFoundPage",
])
```

Добавление компонентов в блок header:
```
/* Header */
Components::header([
	"App.Components.Blocks.CSS",
	"App.Components.Blocks.Seo",
])
```

Добавление компонентов в футер:
```
/* Footer */
Components::footer([
	"App.Components.Blocks.Metrika",
])
```