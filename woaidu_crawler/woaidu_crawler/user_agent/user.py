import requests
import random

# User-Agent列表
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    # 更多User-Agent
]

# 从代理池管理器获取代理IP
def get_proxy():
    response = requests.get("http://proxy_pool_manager/get_proxy")
    if response.status_code == 200:
        return response.json().get("proxy")
    
# 发送请求
def fetch_url(url):
    headers = {"User-Agent": random.choice(user_agent_list)}
    proxy = get_proxy()
    proxies = {
        "http": "http://{}".format(proxy),
        "https": "https://{}".format(proxy),
    }
    response = requests.get(url, headers=headers, proxies=proxies)
    return response.content
