# Поисковая оптимизация

Для того чтобы указать title и description нужно в модели страницы создать функцию buildTitle

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

Также в ModuleDescription можно добавить хук:

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

Этот хук создает SeoModel и добавляет мета теги OpenGraph.

SeoModel это модель для дополнительного управления тегами.

```
use Runtime.Widget.Seo.SeoModel;

void buildTitle(RenderContainer container)
{
    SeoModel seo = this.layout.get("seo");
}
```

Параметры SeoModel:
- favicon
- canonical_url
- article_published_time
- article_modified_time
- robots
- tags
