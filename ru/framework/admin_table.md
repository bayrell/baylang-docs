# Создание форм и таблиц в админке

Пример компонента:
```
<class name="App.Admin.Components.Pages.Market.Item">

<use name="Runtime.Widget.Button" component="true" />
<use name="Runtime.Widget.RowButtons" component="true" />
<use name="Runtime.Widget.Table.TableWrap" component="true" />

<template>
	<div class="marketplace_page">
		<TableWrap model={{ this.model.manager }}>
			<slot name="top_buttons">
				<RowButtons>
					<Button class="button--success"
						@event:click="this.model.manager.showAddDialog()"
					>Add</Button>
				</RowButtons>
			</slot>
			<slot name="row_buttons" args="Map item, Map field, int row_number">
				<RowButtons>
					<Button class="button--small"
						@event:click="this.model.manager.showEditDialog(item.copy())"
					>Edit</Button>
					<Button class="button--small button--danger"
						@event:click="this.model.manager.showDeleteDialog(item.copy())"
					>Delete</Button>
				</RowButtons>
			</slot>
		</TableWrap>
	</div>
</template>

</class>
```

Пример модели:
```
namespace App.Admin.Components.Pages.Item;

use Runtime.BaseModel;
use Runtime.Serializer.IntegerType;
use Runtime.Serializer.ObjectType;
use Runtime.Serializer.StringType;
use Runtime.Serializer.VectorType;
use Runtime.Web.RenderContainer;
use Runtime.Widget.Table.TableManager;
use App.Admin.Components.Pages.Item;


class ItemModel extends BaseModel
{
	string component = classof Item;
	TableManager manager = null;
	
	
	/**
	 * Serialize object
	 */
	static void serialize(ObjectType rules)
	{
		parent(rules);
		rules.addType("manager", new ObjectType());
	}
	
	
	/**
	 * Init widget
	 */
	void initWidget(Map params)
	{
		parent(params);
		
		this.manager = this.createWidget(classof TableManager, {
			"autoload": true,
			"api_name": "admin.item",
			"page_name": "p",
			"title": method this.getTableTitle,
			"primary_rules":
			{
				"id": new IntegerType(),
			},
			"item_rules":
			{
				"id": new IntegerType(),
				"type": new StringType(),
				"slug": new StringType(),
				"tags": new VectorType(new StringType()),
				"name": new StringType(),
			},
			"form_fields":
			[
				{
					"name": "slug",
					"label": "Slug",
					"component": "Runtime.Widget.Input",
				},
				{
					"name": "type",
					"label": "Type",
					"component": "Runtime.Widget.Select",
					"props":
					{
						"options":
						[
							{"key": "template", "value": "Template"},
							{"key": "modificator", "value": "Modificator"},
						]
					}
				},
				{
					"name": "tags",
					"label": "Tags",
					"component": "Runtime.Widget.Tag",
				},
				{
					"name": "name",
					"label": "Name",
					"component": "Runtime.Widget.Input",
				},
			],
			"table_fields":
			[
				{
					"name": "row_number",
				},
				{
					"name": "name",
					"label": "Name",
				},
				{
					"name": "type",
					"label": "Type",
					"value": string (Map item)
					{
						string type = item.get("type");
						if (type == "template") return "Template";
						else if (type == "modificator") return "Modificator";
						return "";
					},
				},
				{
					"name": "buttons",
					"slot": "row_buttons",
				}
			],
		});
	}
	
	
	/**
	 * Returns table title
	 */
	string getTableTitle(string action, Map item)
	{
		if (action == "add") return "Add";
		else if (action == "edit") return "Edit";
		else if (action == "delete") return "Delete";
		else if (action == "delete_message") return "Delete";
		return "";
	}
	
	
	/**
	 * Build page title
	 */
	void buildTitle(RenderContainer container)
	{
		this.layout.setPageTitle("Items");
	}
}
```