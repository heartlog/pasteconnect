import requests
from fake_useragent import UserAgent

def reqsession(url, params=None):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36",
    }
    try:
        response = session.get(url, params=params)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
    return response

def Advreqsession(url, params=None):
    session = requests.Session()
    ua = UserAgent()
    session.headers = {
        "User-Agent": ua.random,
        "Accept-Encoding": "*"
    }
    try:
        response = session.get(url, params=params)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
        
def postsession(url, data=None, files=None):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    try:
        response = session.post(url, data=data, files=files)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
    return response

def Advpostsession(url, data=None, files=None):
    session = requests.Session()
    ua = UserAgent()
    session.headers = {
        "User-Agent": ua.random,
        "Accept-Encoding": "*"
    }
    try:
        response = session.post(url, data=data, files=files)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()