# Pasteconnect package

PasteConnect is a Python library for interacting with Pastebin. It allows you to check account validity, authenticate, create pastes, delete pastes, and retrieve raw paste content.

[![PyPI](https://img.shields.io/pypi/v/pasteconnect?style=for-the-badge&logo=pypi&label=PYPI&color=blue)](https://pypi.org/project/pasteconnect/)
[![Licence](https://img.shields.io/pypi/l/pasteconnect?style=for-the-badge)](https://github.com/heartlog/pasteconnect/blob/main/LICENSE)

## Installation
**Python 3.7 or higher is required.**
[![Python](https://img.shields.io/pypi/pyversions/pasteconnect?style=flat-square&logo=python&label=PYTHON&color=blue)](https://pypi.org/project/pasteconnect/)

You can install PasteConnect using `pip`:
```diff
+$ pip install pasteconnect
```

Install from source repository
```diff
+$ pip install git+https://github.com/heartlog/pasteconnect.git
```

To use PasteConnect, you need your Pastebin credentials, which include your `username`, `password`, and `api_key`.
If you don't have these, you can obtain them by signing up for a [Pastebin account](https://pastebin.com/signup) and generating an `api_key` from the [Pastebin API documentation](https://pastebin.com/doc_api).


### Usage
```py
from pasteconnect import PasteConn

# Initialize a PasteConnect client
pastebin = PasteConn(username, password, api_key)
# Check account validity
account_status = pastebin.check_account()
print(account_status)

title = "My Paste Title"
content = "This is the content of my paste."

# Create a paste on Pastebin
paste_url = pastebin.create_paste(title, content, privacy=1)
print(f"Paste created: {paste_url}")
```
---

## Initialize client

To interact with PasteConnect, you need to initialize a client with your credentials:
### `pastebin = PasteConn(username, password, api_key)` ![Static Badge](https://img.shields.io/badge/Required-eb2525?style=for-the-badge)
```diff
-required for other methods to work
```

[![Username](https://img.shields.io/badge/Username-blue)](#getting-started)
[![Password](https://img.shields.io/badge/password-blue)](#getting-started)
[![Api_key](https://img.shields.io/badge/api__key-blue)](#getting-started)

Refer [Getting Started](#getting-started)

```py
username = "your_username"
password = "your_password"
api_key = "your_api_key"

# Initialize the client
pastebin = PasteConn(username, password, api_key)
```
Alternatively, you can initialize with [predefined environment variables](https://rentry.co/setenv)
```py
pastebin = PasteConn() # with pre define env var
```

---
## Check account existance
You can check the validity of your Pastebin account using the following method:
#### `pastebin.check_account()`
![dash](https://img.shields.io/badge/-----grey)

```py
result = pastebin.check_account()
print(result)  # Response: '[heartlog] is Valid Account. User key : "user_key"'
```

## Authentication
To authenticate and get your `user_key`, use the `auth()` method:

#### `pastebin.auth()`
![dash](https://img.shields.io/badge/-----grey)

Get `user_key` using give credentials.
```py
result = pastebin.auth()
print(result)  # Response: "user_key"
```

## Creating a Paste

You can create a paste on Pastebin with a title, content, and privacy level. Privacy levels can be 0 (public), 1 (unlisted), or 2 (private):
#### `pastebin.create_paste(title, content, privacy=1)`
![privacy](https://img.shields.io/badge/privacy-green)
![title](https://img.shields.io/badge/title-blue)
![content](https://img.shields.io/badge/content-purple)

```py
privacy = 1 # (default - private)
title = "Title of paste"
content = """
Hello
This is multiline text
"""
pastebin.create_paste(title, content, privacy=1)
```

## Deleting a Paste
To delete a paste, provide its URL or ID using the `delete_paste(url)` method:

#### `pastebin.delete_paste(url)`
![Static Badge](https://img.shields.io/badge/url-blue)

```py
url = "https://pastebin.com/kZATAWhe"
result = pastebin.delete_paste(url)
print(result)  # Response: "Paste Removed"
```

## Get raw content
You can retrieve the raw content of a paste using it's URL or ID:
#### `pastebin.get_raw_content(url)`

![url](https://img.shields.io/badge/url-purple)

```py
from pasteconnect import get_raw

result = get_raw(url)
print(result)
```

Alternatively, you can use the `get_raw` function:

```py
url = "https://pastebin.com/your_paste_id"
result = pastebin.get_raw_content(url)
print(result)  # Response: "Content of paste"
```

---
# Made with ❤️ by [Heartlog](https://github.com/heartlog/)

## Special Thanks 
venaxyt for [pastebinapi](https://github.com/venaxyt/pastebinapi/). Helped a lot in project. 😁