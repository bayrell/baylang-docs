# BayLang Programming Language

BayLang is an innovative FullStack programming language with unique functionality for automatically converting program code into backend and frontend without the need to develop separate code for server and client parts.

The main idea is compilation into PHP and JavaScript through a compiler. This allows creating programs with a single codebase for different platforms (websites, PHP, WordPress, JS, Python, mobile applications, Windows desktop).

This eliminates the need to constantly switch between different programming languages and significantly increases the speed of web application development.

BayLang allows maintaining a single codebase and, if necessary, changing the technological platform on which the program will run.

This is a full-fledged programming language for creating various programs for different platforms.

**BayLang Features:**
- Cross-platform application development (websites, CRM and ERP systems, mobile and desktop applications)
- Reactivity: automatic page update when data model changes
- MVC architecture implementation
- Server-side rendering (SSR) support
- Website builder support
- MySQL and SQLite support, with the possibility of adding other DBMS
- Python support is planned

BayLang also has AI integration.


## Example program in BayLang

```bay
namespace Main;

class App
{
    static int main()
    {
        print("Hello world!");
        return 0;
    }
}
```

Component:
```bay
<class name="App.Components.IndexPage.IndexPage">

<style>
.index_page{
    padding: 5px;
}
</style>

<template>
    <div class="index_page">
        Hello, {{ this.model.username }}!
    </div>
</template>

</class>
```

Model:
```bay
namespace App.Components.IndexPage;

use Runtime.BaseModel;
use App.Components.IndexPage.IndexPage;

class IndexPageModel extends BaseModel
{
    string component = classof IndexPage;
    string username = "";
    
    
    /**
     * Build title
     */
    void buildTitle(RenderContainer container)
    {
        this.layout.setPageTitle("Index page");
    }
}
```

## History of Creation

[27 Dec 2025] Release 1.0 version. Language and framework

[15 May 2025] Start 1.0 version

[05 Feb 2024] 0.12.4 - Added support for line breaks in HTML components, higher-order functions for expressions, fixed CSS media query operation.

[27 Dec 2024] 0.12.3 - Release of BayLang Constructor for WordPress.

[29 Jun 2024] 0.12.2 - Added submodules, make_all command, OpNegative opcode, module.json reloading, BayLang translator, slot and style support, tests. First version of website constructor 0.1.

[07 Apr 2024] 0.12.1 - Nested CSS styles

[29 Dec 2023] 0.12.0 - VueJS support

[02 Aug 2023] 0.11.6 - Created first website on BayLang. Completely redesigned Runtime.Web framework.

[20 Feb 2023] 0.11.5 - Fourth beta release. Version 0.11.

[25 Dec 2022] 0.11.0 - Started work on stable release 0.11 version.

[21 Feb 2021] 0.10.9 - Add declare, annotations to ui, add watch model

[02 Feb 2021] 0.10.8 - New render function, add svg support. Remove AssignObject, AssignValue, takeValue

[05 Dec 2020] 0.10.7 - Add meta information to ui

[28 Nov 2020] 0.10.6 - Fix php pipe try catch fix

[15 Oct 2020] 0.10.5 - Added enable_check_types flag

[30 Sep 2020] 0.10.4 - Fixed pipes, added render to ui command, added spreads, tested PHP translator

[02 Sep 2020] 0.10.3 - Third beta release.

[28 Aug 2020] 0.10.2 - Ability to develop components in ui templates

[21 Aug 2020] 0.10.2 - Added %if, %for, %while template tags

[07 Aug 2020] 0.10.0 - Moved Context to Runtime.Core, Cleaned Runtime library, Async/Await in NodeJS, Fixed pipes, |> as pipe

[25 Apr 2020] 0.9.1 - Launched BayLang on Raspberry PI

[21 Apr 2020] 0.9.0 - Pipes and monads.

[01 Mar 2020] 0.8.3 - Fixed CSS html bugfix, media nesting

[24 Feb 2020] 0.8.2 - New version, Optimization CoreStruct and compiler

[25 Nov 2019] 0.8.0 - Second Alpha version. BayLang rewritten in functional style with pure functions and immutable data types. (As it turned out later, functional style works slowly)

[29 Apr 2019] 0.7.2 - Bug fixes in lambda, pure, async bugfix

[25 Mar 2019] 0.7.1 - Added memorize, Dict, Collection, rtl::method, UIStruct normalization, DateTime as Struct

[27 Jan 2019] 0.7.0-alpha - Merged Bayrell Template and Lang. Added lambda and pure functions

[16 Dec 2018] 0.6.0 - Added structures and annotations

[05 Nov 2018] 0.5.1 - Added async/await

[15 Jun 2018] 0.3.0 - First alpha working version

Summer 2016 - Start of work