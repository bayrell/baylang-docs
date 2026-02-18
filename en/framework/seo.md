# Search engine optimization

To specify the title and description, you need to create a `buildTitle` function in your page model:

```
/**
 * Build title
 */
void buildTitle(RenderContainer container)
{
	string title = "Page title";
	string description = "Page description";
	if (this.layout.lang == "ru")
	{
		title = "Заголовок страницы";
		description = "Главная страница";
	}
	this.layout.setPageTitle(title);
	this.layout.setDescription(description);
}
```

You can also add a hook to `ModuleDescription`:

```
namespace App;

use Runtime.Widget.Seo.Seo;

class ModuleDescription
{
    pure Vector<Entity> entities() =>
    [
        Seo::hook(),
    ];
}
```

This hook creates a `SeoModel` and adds OpenGraph meta tags.

`SeoModel` is a model for additional tag management.

```
use Runtime.Widget.Seo.SeoModel;

void buildTitle(RenderContainer container)
{
    SeoModel seo = this.layout.get("seo");
}
```

`SeoModel` parameters:
- `favicon`
- `canonical_url`
- `article_published_time`
- `article_modified_time`
- `robots`
- `tags`
