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
>> after creating your account, [head over to the api documentation](https://pastebin.com/doc_api) and grab your api key under `Your Unique Developer API Key`

## Usage example
```py
from pasteconnect import PasteConn

# Sync Client
pastebin = PasteConn(username, password, api_key)
# Account_status
account_status = pastebin.check_account()
print(account_status)

privacy = 0  # Set the privacy level (0 for public)
title = "My Paste Title"
content = "This is the content of my paste."

paste_url = pastebin.create_paste(privacy, title, content)
print(f"Paste created: {paste_url}")
```

### `client = PasteConn(username, password, api_key)`
as per [Getting Started](#getting-started)
`username` - Your 
`password` -
`api_key` - 

# Made with ❤️ by [Heartlog](https://github.com/heartlog/)