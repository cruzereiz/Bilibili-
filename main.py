# -*- coding: UTF-8 -*-
from list_get import list
from folder_name_get import folder_name
from judge_only import judge
from address_get import address
from file_download import download



# name_code = 'BV17y4y127ZV' #视频列表含有一个视频
# name_code = 'BV1Ft411s7Xa' #视频列表含有多个视频
url = 'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click&copy_right=-1&cate_id=124&page=2&pagesize=20&jsonp=jsonp&time_from=20210513&time_to=20210520&callback=jsonCallback_bili_188669464914684283'
name_codes = list(url=url)
for name_code in name_codes:
    # # 根据视频列表名称创建文件目录
    # name_code = input('请输入视频码：')
    folder = folder_name(name_code)
    video_list = judge(name_code)
    # #如果视频列表只有一个视频
    if len(video_list) == 1:
        urls = address(name_code + '?p=1')
        download(folder,urls[0][0].replace(' ',''),urls[1],urls[2])
    # 如果视频列表有多个视频
    else:
        for i in video_list:
            urls = address(name_code + '?p=' + str(video_list.index(i)+1))
            download(folder,i.replace(' ',''),urls[1],urls[2])






