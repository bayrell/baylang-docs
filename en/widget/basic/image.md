# Runtime.Widget.Image

Component for working with images

Usage examples:
```
<class name="App.Example">

<use name="Runtime.Widget.Image" component="true" />

<template>
    <Image src={{ this.layout.assets("image.png") }} />
</template>

</class>
```

If the image src value is not specified, the message “No image” will be displayed


## Component Override

You can also change the behavior and create your own component:
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

Create a hook:
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

Register the hook in ModuleDescription:
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