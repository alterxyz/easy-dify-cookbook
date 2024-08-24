<Instructions>
You are tasked with writing a simple Python script based on the following requirements:

Follow these guidelines to create the Python script:

1. Use Python version 3.10

2. Library usage priority (from most preferred to least preferred):
   a. No imports (preferred)
   b. Built-in libraries available in Python 3.10
   c. Only if absolutely necessary: jinja2, httpx

3. The script should contain only one function named `main`.

4. The `main` function must return a dictionary (dict).

5. Input and output data type priority (from most preferred to least preferred):
   a. String, Number (preferred)
   b. Array[Number], Array[String]
   c. Only if absolutely necessary: Array[Object], Object (use cautiously for nested structures)
   d. No Boolean, nothing else is allowed except the above.
   e. For output - return value, if you not sure what form it is, wrap it with str() is good practice

6. Keep the code as simple as possible.

7. At the top of the script, include a multi-line comment describing the input and output parameters of the `main` function. Use the following format:

```python
"""
Input Variables:
arg1: String, arg2: Number, something: Array[Number], x: Array[String], y: Array[Object], z: Object
Output Variables:
arg1: String, arg2: Number, something: Array[Number], x: Array[String], y: Array[Object], z: Object
"""
```

8. Here's an example of a simple `main` function that adheres to the requirements:

```python
import httpx

def main(auth_bearer: str, account_id: str, namespace_id: str, key_name: str) -> dict:
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_bearer}"
    }
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
    return {
        "full": response.text,
        "type": str(type(response))
    }
```

9. Remember to use "\n" for newline characters in string literals if needed.

10. There must be one return, and the only return in dict, and no `print`.

11. Wrap your entire Python script in a markdown code block, using three backticks (```) at the beginning and end of the code.

Now, write a Python script that meets these requirements. The script should be simple and demonstrate the use of the specified input and output types, prioritizing the use of String and Number types, and avoiding imports if possible. You can choose any simple task or calculation to implement in the `main` function, as long as it adheres to the given constraints and priorities.

Provide your complete Python script, including the input/output comment and wrapped in a markdown code block, as your response.
</Instructions>
