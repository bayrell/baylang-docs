# Record

Получить объект из базы
```
Record<Item> item = await this.relation_item.fetchRecord(
    this.relation_item.select().where("id", "=", "1")
);
```

Получить primary key:
```
Map pk = item.getPrimaryKey();
```

Сохранить объект
```
await item.save();
```

Удалить объект:
```
await item.delete();
```

Получить данные объекта:
```
item.all();
```

Получить старые данные объекта:
```
item.old();
```

Получить только определенные поля:
```
item.intersect(["id", "name"]);
```

Установить новые данные:
```
item.assign({
    "name": "Name"
})
```

Проверить изменился ли объект:
```
bool is_changed = item.isChanged();
```

Проверить новый ли объект:
```
bool is_new = item.isNew()
```

Проверить объект был загружен из базы данных:
```
bool is_update = item.isUpdate();
```