# JSON
This tutorial will teach you the uses and formatting of JSON files as well as how to create, edit, and implement JSON files into your own projects.

## What is JSON?
- JavaScript Object Notation (not only used for JavaScript)
- Used to pass data between platforms such as API calls between clients and servers.
- Used to store data in a human-readable way for application data as well as database content.

## Structure
- Curly braces `{}` are used to define an object, and square brackets `[]` are used to define arrays.
- Uses key-value pairs `{"key":"value"}` where the key can be used as an index to return the value.
- Key indexes must be strings, and values can contain any data including strings, integers, floats, booleans, and nested objects.
- Self describing names and structure that are easy for humans to read and for programs to parse.

## Examples
### One object JSON file for storing a user account:
```json
{
    "id": 0,
    "username": "some-name",
    "join_date": "2025-08-05",
    "is_deleted": false,
    "deletion_date": null
}
```
When loading the content of this file into an object such as `user`, you can index into this object to retrieve the data you want. For example in Python `user.get("username")` will return the string `"some-name"`. Note that using `user["username"]` is valid syntax but will throw an error if the key can not be found in the JSON object so it is recommended to use the `.get()` function which will handle the error and return `None` instead.


### Nested JSON used to store the employees at a company:
```json
{
    "branch_id":"a3a0c48f-9dd0-41cb-9568-9e758b1f129a",
    "branch_name":"Horsham",
    "employees": [
        {"first_name": "Joe", "last_name": "Michael", "dob": "1997-06-10"},
        {"first_name": "Jacob", "last_name": "Smith", "dob": "2001-11-21"},
        {"first_name": "Sam", "last_name": "Thomas", "dob": "2002-09-13"}
    ]
}
```

## Further Practice
The [`/Resources`](/Tutorials/JSON/Resources/) folder contains another JSON file, with additional Python files to help you get started with implementing the use of JSON within Python projects.