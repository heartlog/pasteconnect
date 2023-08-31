import requests

class PastebinAPI:
    def __init__(self, username, password, api_key):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.user_key = self.authenticate()

    def authenticate(self):
        if not all((self.username, self.password, self.api_key)):
            raise ValueError("Username, password, and API key must be specified.")

        login_data = {
            "api_dev_key": self.api_key,
            "api_user_name": self.username,
            "api_user_password": self.password,
        }
        login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)

        if login.status_code == 200:
            return login.text
        else:
            return None

    def create_paste(self, privacy, title, content):
        if not all((self.api_key, self.user_key, privacy, title, content)):
            raise ValueError("API key, user key, privacy, title, and content must be specified.")

        data = {
            "api_option": "paste",
            "api_dev_key": self.api_key,
            "api_user_key": self.user_key,
            "api_paste_code": content,
            "api_paste_name": title,
            "api_paste_expire_date": "N",
            "api_paste_format": "php",
            "api_paste_private": privacy
        }
        paste = requests.post("https://pastebin.com/api/api_post.php", data=data)

        if "https://pastebin.com" in paste.text:
            return paste.text
        else:
            return f"An error occurred: {paste.text}"

    def create_paste_adv(self, privacy, title, content, expire="N", format="php"):
        if not all((self.api_key, self.user_key, privacy, title, content)):
            raise ValueError("API key, user key, privacy, title, and content must be specified.")
        data = {
            "api_option": "paste",
            "api_dev_key": self.api_key,
            "api_user_key": self.user_key,
            "api_paste_code": content,
            "api_paste_name": title,
            "api_paste_expire_date": expire,
            "api_paste_format": format,
            "api_paste_private": privacy
        }
        paste = requests.post("https://pastebin.com/api/api_post.php", data=data)

        if "https://pastebin.com" in paste.text:
            return paste.text
        else:
            return f"An error occurred: {paste.text}"

    def check_account(self):
        if self.user_key:
            return f"[{self.username}] Valid account. User key: {self.user_key}"
        else:
            return f"[{self.username}] Invalid account."
    
    def delete_paste(self, url):
        if not all((self.api_key, self.user_key, url)):
            raise ValueError("API key, user key and deleteURL must be specified.")
        pastekey = get_paste_key(url)
        data = {
            "api_option": "delete",
            "api_dev_key": self.api_key,
            "api_user_key": self.user_key,
            "api_paste_key": pastekey
        }
        paste = requests.post("https://pastebin.com/api/api_post.php", data=data)
        if "Paste Removed" in paste.text:
            return paste.text
        else:
            return f"An error occurred: {paste.text}"
    
    
    def get_raw_content(url):
        if 'pastebin.com' in url:
            parts = url.split('/')
            if len(parts) >= 4:
                new_url = f"https://pastebin.com/raw/{parts[-1]}"
                response = requests.get(new_url)
                if response.status_code == 200:
                    return response.text
                else:
                    return f"Failed to retrieve content from {new_url} (HTTP {response.status_code})"
            else:
                return "Invalid pastebin URL"
        else:
            return "Invalid URL"

def get_paste_key(url):
    parts = url.split("/")
    return parts[-1]

if __name__ == "__main__":

"""
username = "your_username"
password = "your_password"
api_key = "your_api_key"

pastebin = PastebinAPI(username, password, api_key)
account_status = pastebin.check_account()
print(account_status)

privacy = 0  # Set the privacy level (0 for public)
title = "My Paste Title"
content = "This is the content of my paste."

paste_url = pastebin.create_paste(privacy, title, content)
print(f"Paste created: {paste_url}
"""