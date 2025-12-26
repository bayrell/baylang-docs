# Record

Get object from database
```
Record<Item> item = await this.relation_item.fetchRecord(
    this.relation_item.select().where("id", "=", "1")
);
```

Get primary key:
```
Map pk = item.getPrimaryKey();
```

Save item:
```
await item.save();
```

Delete item:
```
await item.delete();
```

Get objet data:
```
item.all();
```

Get old object data:
```
item.old();
```

Get only specific fields:
```
item.intersect(["id", "name"]);
```

Assign new data:
```
item.assign({
    "name": "Name"
})
```

Returns true if object is changed:
```
bool is_changed = item.isChanged();
```

Check if object is new:
```
bool is_new = item.isNew()
```

Check if object is loaded from database:
```
bool is_update = item.isUpdate();
```