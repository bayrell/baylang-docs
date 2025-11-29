# Models

Models in BayLang store the state of the project and the business logic of the application. It is important to understand that models are part of the frontend. They determine how data will be stored on the client.

Data Transfer Objects (DTOs) are also considered models.

It is very important to ensure serialization in models. Serialization allows data transfer from the backend to the frontend.

Example of a model:
```
namespace App;

use Runtime.BaseModel;
use Runtime.RenderContainer;
use Runtime.Serializer;
use App.ExamplePage;

class PageModel extends BaseModel
{
    string component = classof ExamplePage;
    string name = "";
    
    
    /**
     * Init params
     */
    void initParams(Map params)
    {
        parent(params);
    }
    
    
    /**
     * Init widget
     */
    void initWidget(Map params)
    {
        parent(params);
    }
    
    
    /**
     * Serialize model
     */
    void serialize(Serializer serializer, Map data)
    {
        parent(serializer, data);
        serializer.process(this, "name", data);
    }
    
    
    /**
     * Load data
     */
    async void loadData(RenderContainer container)
    {
        parent(container);
    }
    
    
    /**
     * Build title
     */
    void buildTitle(RenderContainer container)
    {
        this.layout.setPageTitle("Page");
    }
}
```

When a model is created, parameters are passed to it. There are two functions that are called when creating a model:
- initParams – used to initialize model parameters. Used to initialize model variables.
- initWidget – initializes model widgets. Usually used to create other models and configure them.

The serialize function is responsible for model data serialization. Serialization is the process of converting a model class into an object ready for transmission. Typically, model data is transferred from backend to frontend, but this is not mandatory. You can also save model data to a database.

If the model loads any data, these data should be added to the serialize function.

The loadData function loads data via API from the backend. It’s called when RenderContainer renders the page.

The buildTitle function sets the page title.

RenderContainer – is a container used by the application during page initialization. It handles route lookup (Route) and model data loading.

The component variable specifies which component should be displayed along with this model.

## Layout

Layout is the global model of the entire application. It is usually accessible from both model and template. It can be accessed via the variable this.layout.

Layout includes functions such as:
- Page title
- Current route
- Page models and widgets
- List of components used in the application.