# simple pasteconnect package

## what can this do ?
paste code in pastebin.com with api.

## Usage example
```py
pastebin = PastebinAPI(username, password, api_key)
account_status = pastebin.check_account()
print(account_status)

privacy = 0  # Set the privacy level (0 for public)
title = "My Paste Title"
content = "This is the content of my paste."

paste_url = pastebin.create_paste(privacy, title, content)
print(f"Paste created: {paste_url}")
```

made with ❤️ by [Heartlog](https://github.com/heartlog/)