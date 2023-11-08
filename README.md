# Pasteconnect package

[![PyPI](https://img.shields.io/pypi/v/pasteconnect?style=for-the-badge&logo=pypi&label=PYPI&color=blue)](https://pypi.org/project/pasteconnect/)
## What can this package do ?
paste code in [pastebin.com]() with api.
Read text of pastebin paste.

[![Licence](https://img.shields.io/pypi/l/pasteconnect)]()
## Installation
**Python 3.7 or higher is required.**
[![Python](https://img.shields.io/pypi/pyversions/pasteconnect?style=flat-square&logo=python&label=PYTHON&color=blue)](https://pypi.org/project/pasteconnect/)

Install from PyPI
```shell
$ pip install pasteconnect
```

Install from source
```shell
$ pip install git+https://github.com/heartlog/pasteconnect.git
```
## Getting Started
> To get(create) your `username`, `password` » login to your [pastebin account](https://pastebin.com/signup)
>> after creating your account, [head over to the api documentation](https://pastebin.com/doc_api) and grab your `api_key` under __Your Unique Developer API Key__

## Client Example
```py
from pasteconnect import PasteConn 
pastebin = PasteConn(username, password, api_key)
```
> or 
### [Set env varible](https://rentry.co/setenv) -› username, password, api_key
```py
pastebin = PasteConn()
```

### Usage
```py
from pasteconnect import PasteConn

# Sync Client
pastebin = PasteConn(username, password, api_key)
# Account_status(check validity of account)
account_status = pastebin.check_account()
print(account_status)

title = "My Paste Title"
content = "This is the content of my paste."

# Paste text to pastebin
paste_url = pastebin.create_paste(title, content, privacy=1)
print(f"Paste created: {paste_url}")
```

### `pastebin = PasteConn(username, password, api_key)` ![Static Badge](https://img.shields.io/badge/Required-eb2525?style=for-the-badge)
 *required for other modules to work
 
[![Username](https://img.shields.io/badge/Username-blue)](#getting-started)
[![Password](https://img.shields.io/badge/password-blue)](#getting-started)
[![Api_key](https://img.shields.io/badge/api__key-blue)](#getting-started)

Refer [Getting Started](#getting-started)

```py
username = "username"
password = "*******"
api_key = "123456abcdefg"
# Define Client
pastebin = PasteConn(username, password, api_key)
# OR 
pastebin = PasteConn() # with pre define env var
```


#### `pastebin.check_account()`
![dash](https://img.shields.io/badge/-----grey)

Check validity of pastebin.com account.
```py
result = pastebin.check_account()
print(result)  # Response: '[heartlog] is Valid Account. User key : "user_key"'
```
#### `pastebin.auth()`
![dash](https://img.shields.io/badge/-----grey)

Get `user_key` using give credentials.
```py
result = pastebin.auth()
print(result)  # Response: "user_key"
```

#### `pastebin.create_paste(title, content, privacy=1)`
![privacy](https://img.shields.io/badge/privacy-pink)
![title](https://img.shields.io/badge/title-blue)
![content](https://img.shields.io/badge/content-purple)

```py
# 0 : public | 1 : unlisted | 2 : private
privacy = 1 # (default - private)
title = "Title of paste"
content = """
Hello
This is multiline text
"""
pastebin.create_paste(title, content, privacy=1)
```

#### `pastebin.delete_paste(url)`
![Static Badge](https://img.shields.io/badge/url-blue)

```py
url = "https://pastebin.com/kZATAWhe"
result = pastebin.delete_paste(url)
print(result)  # Response: "Paste Removed"
```

#### `pastebin.get_raw_content(url)`

![url](https://img.shields.io/badge/url-purple)

```py
from pasteconnect import get_raw

result = get_raw(url)
print(result)
```
### optional
```py
url = "https://pastebin.com/kZATAWhe"
result = pastebin.get_raw_content(url)
print(result)  # Response: "Content of paste"
```

---
# Made with ❤️ by [Heartlog](https://github.com/heartlog/)

## Special Thanks 
venaxyt for [pastebinapi](https://github.com/venaxyt/pastebinapi/). Helped a lot in project. 😁