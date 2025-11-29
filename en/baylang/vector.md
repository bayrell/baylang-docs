# Vector

Vector is a data structure for working with collections in BayLang. It is an ordered list of elements that can change its length when adding or removing elements.

Example of creating a vector:
```
Vector arr = [];
```

Get the number of elements:
```
print(arr.count());
```

Get an element by its index:
```
print(arr.get(index));
print(arr.get(index, default_value));
```

Set the value of an element:
```
arr.set(index, value);
```

Get the first element:
```
arr.first();
```

Get the last element:
```
arr.last();
```


## Adding and Removing Elements

To add an element to the end of the list, execute:
```
arr.push(item);
```

Remove an element by its index:
```
arr.remove(index);
```

Insert an element:
```
arr.insert(index, new_item);
```

Merge the vector with another vector:
```
Vector new_arr = arr.concat(["new item"]);
```

Add multiple elements:
```
arr.appendItems(items);
```

Return a new array:
```
arr.slice(offset)
arr.slice(offset, length)
```

offset - start

length - length of the new array. Optional parameter. If it is not specified, the entire array starting from offset is returned.


## Searching for Elements

Find the index of an element by its value:
```
int index = arr.indexOf(value);
```

If the element is not found, the function will return -1

Search for an element using a function:
```
string item = arr.find(bool (string item) => rs::strlen(item) != 0);
```

Similarly, you can find the index of an element:
```
int index = arr.findIndex(bool (string item) => rs::strlen(item) != 0);
```


## Functional Programming

Map function:
```
Vector new_arr = arr.map(int (int item) => item * 2);
```

Reduce function:
```
int sum = arr.reduce(
    int (int sum, int value) => sum + value, 0
);
```

Filter function:
```
Vector new_arr = arr.filter(bool (int item) => item != 0);
```

Each function:
```
int sum = 0;
arr.each(void (int item, int index) use (sum){
    sum += item;
})
```

Transforming from Vector to Map
```
Map items = arr.transition(
    Vector (int value, int index)
    {
        return [index, value];
    }
);
```


## Sorting Arrays

Regular sorting:
```
arr.sort()
```

Sorting with a custom function:
```
arr.sort(int (int a, int b) => a > b);
```


## Vector Manipulation Functions

Reverse the array:
```
arr.reverse();
```

Remove duplicates:
```
arr.removeDuplicates();
```

Flatten nested vectors:
```
arr.flatten();
```