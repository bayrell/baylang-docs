# Query

An object that allows you to send SQL queries to the database.

Example request:
```
Query q = new Query()
    .select(["id", "name"])
    .from("items")
    .where("item", "=", "1")
;

Connection conn = Connection::get();
QueryResult<Map> rows = await conn.fetchAll();
```

## Creating queries

Get Raw SQL Query
```
Query raw(string sql, Map data);
```

Count the found lines
```
Query calcFoundRows(bool value = true);
```

Remove duplicates from the answer
```
Query distinct(bool value = true)
```

Enable query debugging
```
Query debug(bool value = true)
```

Execute a select query
```
Query select(Vector fields = null)
```

Specify the table name and its synonym
```
Query table(string table_name = "", string alias_name = "")
Query from(string table_name = "", string alias_name = "")
```

Run a query to insert data
```
Query insert(string table_name = "")
```

Example:
```
Query q = new Query()
    .insert("items")
    .values({
        "name": "item",
    });

Connection conn = Connection::get();
await conn.execute(q);
```

Run a data update query
```
Query update(string table_name = "")
```

Example:
```
Query q = new Query()
    .update("items")
    .where("id", "=", 1)
    .values({
        "name": "item",
    })
;

Connection conn = Connection::get();
await conn.execute(q);
```

Perform a data deletion request
```
Query delete(string table_name = "")
```

Example:
```
Query q = new Query()
    .delete("items")
    .where("id", "=", 1)
;

Connection conn = Connection::get();
await conn.execute(q);
```

Get the query type (select, insert, update, delete, raw)
```
Query kind(string kind)
```


## List of request fields

Clear fields
```
Query clearFields()
```

Replace query fields with others
```
Query fields(Vector<string> fields)
```

Add a query field
```
Query addField(string field)
```

Add a raw query field. This is needed for queries like `count(*) as c` or full-text queries.
```
Query addRawField(string field_name)
```

Add a field list
```
Query addFields(Collection<string> fields)
```


## Request values

Add value
```
Query value(string key, string value)
```

Add a list of values
```
Query values(Dict data)
Query data(Dict data)
```


## Pagination

Set page number. Page starts at zero.
```
Query page(int page, int limit = null)
```

Set the offset
```
Query offset(int start)
Query start(int start)
```

Set line limit
```
Query limit(int limit)
```

Get the current page number. Calculated as offset / limit
```
int getPage()
```

Get list of pages
```
int getPages(int rows)
```


## Sort

Clear sort
```
Query clearOrder()
```

Sort by field name
```
Query orderBy(string name, string sort)
```


## Filter

Search by field value
```
Query where(string key, string op, var value)
```

Setup new filter
```
Query setFilter(Collection<QueryFilter> filter)
```

Add filter
```
Query addFilter(var filter)
```

Add or
```
Query addOrFilter(Collection filter)
```

Clear filter
```
Query clearFilter()
```


## Inner join

```
Query innerJoin(string table_name, Collection filter, string alias_name = "")
Query leftJoin(string table_name, Collection filter, string alias_name = "")
```