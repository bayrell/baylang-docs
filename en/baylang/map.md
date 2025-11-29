# Map

Map is a data structure for working with key-value hash tables. Strings are used as keys. To store objects, the user must define a hash function themselves or use ready-made ones from the library.

Alternative names: map, hash table, dictionary.

Example of creating a hash table:
```
Map items = {};
```

Setting a value:
```
items.set(key, value);
```

Getting a value by key:
```
items.get(key);
```

Merging the dictionary with another dictionary:
```
items.concat({"key": "value"});
```


## Functional Programming

The map function allows changing the values of the dictionary:
```
Map new_map = items.map(int (int value, string key) => value * 2);
```

The map function allows changing both values and keys:
```
Map new_map = items.mapWithKeys(Vector (int value, string key) => [key, value * 2]);
```

The reduce function:
```
int sum = items.reduce(
    int (int sum, int value, string key) => sum + value, 0
);
```

The filter function:
```
Map new_map = items.filter(bool (int value, string key) => value != 0);
```

The each function:
```
int sum = 0;
items.each(
    void (int value, string key) use (sum)
    {
        sum += value;
    }
);
```

The transition function. Allows converting a Map to a Vector:
```
Vector arr = items.transition(
    int (int value, string key) => value
)
```