# Pasteconnect package

[![PyPI version](https://badge.fury.io/py/pasteconnect.svg)](https://badge.fury.io/py/pasteconnect)

[![PyPI](https://img.shields.io/pypi/v/pasteconnect?style=flat-square)](https://pypi.org/project/pasteconnect/)
## What can this package do ?
paste code in [pastebin.com]() with api.
Read text of pastebin paste.

## Installation
**Python 3.6 or higher is required.**

Install from PyPI
```shell
$ pip install pasteconnect
```

Install from source
```shell
$ pip install git+https://github.com/heartlog/pasteconnect
```
## Getting Started
> To get(create) your `username`, `password` » login to your [pastebin account](https://pastebin.com/signup)
>> after creating your account, [head over to the api documentation](https://pastebin.com/doc_api) and grab your `api_key` under __Your Unique Developer API Key__

## Usage example
```py
from pasteconnect import PasteConn

# Sync Client
pastebin = PasteConn(username, password, api_key)
# Account_status(check validity of account)
account_status = pastebin.check_account()
print(account_status)

privacy = 0  # Set the privacy level (0 for public)
title = "My Paste Title"
content = "This is the content of my paste."

# Paste text to pastebin
paste_url = pastebin.create_paste(privacy, title, content)
print(f"Paste created: {paste_url}")
```

### `pastebin = PasteConn(username, password, api_key)` ![Static Badge](https://img.shields.io/badge/Required-eb2525)
 *required for other modules to work
![Username](https://img.shields.io/badge/Username-blue)
![Password](https://img.shields.io/badge/password-blue)
![Api_key](https://img.shields.io/badge/api__key-blue)

Refer [Getting Started](#getting-started)

#### `pastebin.check_account()`
Check validity of pastebin.com account.

#### `pastebin.authenticate()`
--

#### `pastebin.create_paste(privacy, title, content)`
![privacy](https://img.shields.io/badge/privacy-pink)
![title](https://img.shields.io/badge/title-blue)
![content](https://img.shields.io/badge/content-purple)

#### `pastebin.delete_paste(url)`
![Static Badge](https://img.shields.io/badge/url-blue)

#### `pastebin.get_raw_content(url)`

![url](https://img.shields.io/badge/url-purple)

# Made with ❤️ by [Heartlog](https://github.com/heartlog/)