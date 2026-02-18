# Setup project

An example PHP project is available at [https://github.com/bayrell/project_php](https://github.com/bayrell/project_php)

**Project Structure**

```
files
src
  app
    Components
      Blocks
        CSS.bay
        Scripts.bay
      Layout
        DefaultLayout.bay
        DefaultLayoutModel.bay
      Pages
        IndexPage
          IndexPage.bay
          IndexPageModel.bay
      Routes.bay
    ModuleDescription.bay
  public
    assets
    index.php
  project.json
.dockerignore
build.sh
Dockerfile
```

## ModuleDescription

ModuleDescription is the main file of a module. Its purpose is to declare dependencies and module settings.

Example:
```
namespace App;

use Runtime.Entity.Hook;
use Runtime.Web.Annotations.Route;
use Runtime.Web.Hooks.PageNotFound;
use Runtime.Web.Hooks.Components;
use Runtime.Web.Hooks.SetupLayout;


class ModuleDescription
{
    /**
     * Returns module name
     */
    pure string getModuleName() => "App";
    
    
    /**
     * Returns module version
     */
    pure string getModuleVersion() => "0.0.1";
    
    
    /**
     * Returns required modules
     * @return Map<string>
     */
    pure Dict<string> requiredModules() =>
    {
        "Runtime.Web": "*",
        "Runtime.Widget": "*",
    };
    
    
    /**
     * Returns enities
     */
    pure Collection<Dict> entities() =>
    [		
        /* Setup layout */
        SetupLayout::hook({
            "default": "App.Components.Layout.DefaultLayoutModel",
        }),
        
        /* Components */
        Components::hook([
            "App.Components.Blocks.CSS",
        ]),
        Components::footer([
            "App.Components.Blocks.Script"
        ]),
        
        PageNotFound::hook("App.Components.Pages.NotFoundPage.NotFoundPageModel"),
        
        #ifdef BACKEND then
        new Route("App.Components.Pages.Routes"),
        #endif
    ];
}
```

Methods:
- getModuleName - Module name
- getModuleVersion - Module version
- requiredModules - Module dependencies
- entities - Module settings

Settings:
- SetupLayout - Layout configuration. Contains information about the layout model that should be initialized by `layout_name`.
- Components::hook - Adds components as dependencies (to the header/body).
- Components::footer - Adds components to the website's footer.
- PageNotFound::hook - Sets the model for the "page not found" error.
- Route - List of website routes.

More details on the list of settings can be found in [Hooks](hooks).


## project.json Configuration

This file contains project settings and compilation rules.

```
{
    "name": "Project name",
    "description": "Description",
    "license": "MIT",
    "author": "",
    "languages": ["php", "es6"],
    "modules": [
        {
            "src": "app",
            "type": "module"
        },
        {
            "src": "lib",
            "type": "folder"
        }
    ],
    "assets": [
        {
            "type": "js",
            "dest": "public/assets/app.js",
            "modules": [
                "@app"
            ]
        }
    ],
    "exclude": []
}
```

Parameters:
- name - Project name
- description - Project description
- languages - Languages into which the project should be compiled
- modules - List of project modules
- assets - Bundles that will be assembled


## module.json Configuration

This file contains module settings.

```
{
    "name": "App",
    "assets": [
        "Components/Blocks/CSS.bay",
        "Components/Blocks/Script.bay",
        "Components/Layout/DefaultLayout.bay",
        "Components/Layout/DefaultLayoutModel.bay",
        "Components/Pages/IndexPage/IndexPage.bay",
        "Components/Pages/IndexPage/IndexPageModel.bay",
        "Components/Pages/NotFoundPage/NotFoundPage.bay",
        "Components/Pages/NotFoundPage/NotFoundPageModel.bay",
        "ModuleDescription.bay"
    ],
    "src": "./",
    "dest":
    {
        "php": "../source/php",
        "es6": "../source/es6"
    },
    "groups": [
        "app"
    ],
    "exclude": [
        "vendor"
    ]
}
```

Parameters:
- name - Module name
- assets - List of files to include in the bundle
- src - Name of the folder with Baylang source code
- dest - Path where files should be compiled
- groups - List of module groups
- exclude - Which folders to exclude

