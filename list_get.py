import requests
import re

def list(url):
    headers = {
        'ser-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'referer': 'https://www.bilibili.com/v/technology/fun/'
    }
    response = requests.get(url=url,headers=headers)
    resp = response.content.decode()
    namecodes = re.findall(r'"bvid":"(.*?)","title"',resp)
    return namecodes



# url = 'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=124&page=2&pagesize=20&jsonp=jsonp&time_from=20210513&time_to=20210520&callback=jsonCallback_bili_188669464914684283'
# print(list(url=url))