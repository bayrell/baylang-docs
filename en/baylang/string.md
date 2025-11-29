# Working with Strings

Strings are scalar immutable objects. Strings are declared as follows:

```bay
string message = "Hello";
```

String concatenation:

```bay
string username = "User";
string new_message = message ~ " " ~ username;
```

When concatenating strings, a new object is created. Therefore, if you need to join multiple strings, you should use a Vector:

```bay
Vector messages = [];
string message = rs::join("", messages);
print(message);
```


## String Library

The Runtime.rs library is used for working with strings.

### String Length

To get the length of a string, use strlen:
```
int rs::strlen(string s);
```

### Get a Substring from a String

```
string rs::substr(string s, int start, int len);
```

s – the string

start – starting position

len – length of the new substring

### Get a Character from a String

```
char rs::charAt(string s, string pos);
```

s – the string

pos – index of the character


### Get an ASCII Character

```
int rs::chr(int code);
```

code – ASCII code


### Get an ASCII Code

```
int rs::ord(char ch);
```

ch – character


### Convert String to Lowercase

```
string rs::lower(string s);
```

s – the string


### Convert String to Uppercase

```
string rs::upper(string s);
```

s – the string


### Compare Two Strings

```
int rs::compare(string a, string b);
```

a, b – strings to compare

Example usage:

```
Vector arr = [
    "apple",
    "banana",
    "orange"
];
arr.sort(int (string a, string b) => rs::compare(a, b));
```


### Replace One String with Another

```
int rs::replace(string search, string item, string s);
```

search – string to find

item – replacement string

s – source string


### Repeat a String Multiple Times

```
string rs::str_repeat(string s, int n);
```

s – the string

n – number of repetitions


### Split a String into Multiple Parts

```
string rs::split(string delimiter, string s, int limit = -1)
```

delimiter – separator

s – the string

limit – maximum number of parts


```
Vector<string> rs::splitArr(Vector<string> delimiters, string s, int limit = -1);
```

delimiters – list of separators

s – the string

limit – maximum number of parts


### Join Strings Together

```
string rs::join(string ch, Vector<string> arr);
```

ch – separator

arr – array of strings


### Join URL Path

```
string rs::join_path(Vector arr);
```

arr – array representing path components

Example:
```
string path = rs::join_path(["folder", "name.txt"]);
```


### Trim Extra Characters from Both Sides

```
string rs::trim(string s, string ch = "");
```

s – the string

ch – characters to trim (default removes whitespace)


### Search for a Substring within a String

```
int rs::indexOf(string s, string search, string offset = 0);
```

s – the string to search in

search – substring to find

offset – position to start searching


### Format a String

```
string rs::format(string s, Dict params = null);
```

s – format string

params – parameters dictionary

Example:

```
string message = rs::format("Hello %username%", {"username": "User"});
```