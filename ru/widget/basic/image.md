# Runtime.Widget.Image

Компонент работы с картинкой

Примеры использования:
```
<class name="App.Example">

<use name="Runtime.Widget.Image" component="true" />

<template>
    <Image src={{ this.layout.assets("image.png") }} />
</template>

</class>
```

Если значение src картинки не указано, то будет отображено сообщение No image


## Переопределение компонента

Вы также можете изменить поведение и создать свой компонент:
```
<class name="App.Components.Image" extends="Runtime.Widget.Image">

<style>
.image__no_image{
    max-width: 100px;
    max-height: 100px;
}
</style>

<template name="renderNoImage">
    <div class="image__no_image">Image not found</div>
</template>

</class>
```

Создайте хук:
```
namespace App.Hooks;

use Runtime.Hooks.RuntimeHook;
use Runtime.Providers.RenderProvider;

class AppHook extends RuntimeHook
{
    void register_hooks()
    {
        this.register(RuntimeHook::START, "start");
    }
    
    
    /**
     * Start app
     */
    void start()
    {
        RenderProvider render = @.provider("render");
        render.addComponent("Runtime.Widget.Image", "App.Components.Image");
    }
}
```

Зарегистрируйте хук в ModuleDescription:
```
namespace App;

use Runtime.Annotations.Hook;

class ModuleDescription
{
    pure Vector getEntities() =>
    [
        new Hook("App.Hooks.AppHook"),
    ];
}
```