# Components

Registers components in the system. Sometimes it is necessary to add additional components to the system.

Adding components to CSS styles:
```
/* Components */
Components::hook([
	"App.Components.Blocks.CSS",
	"App.Components.Pages.IndexPage.IndexPage",
	"App.Components.Pages.NotFoundPage.NotFoundPage",
])
```

Adding components to the header block:
```
/* Header */
Components::header([
	"App.Components.Blocks.CSS",
	"App.Components.Blocks.Seo",
])
```

Adding components to the footer:
```
/* Footer */
Components::footer([
	"App.Components.Blocks.Metrika",
])
```