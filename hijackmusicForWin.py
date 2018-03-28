#-*- coding:utf-8 -*-
#author = 'hijacklinux'

import re
import requests
import sys
type=sys.getfilesystemencoding()
print(("""
网易云音乐下载器
作者：万事屋小贱
""").decode('utf-8').encode(type))
def download():
    filename =raw_input("随便起个文件名（如：hijackmusic.mp3）：".decode('utf-8').encode(type))
    filename = "downloads\\"+filename
    url_in = raw_input("请输入网易云音乐的付费下载链接：".decode('utf-8').encode(type))
    patt = r".*id=(\d+)"
    musicid = re.match(patt,url_in).group(1)
    url_pre = 'http://music.163.com/song/media/outer/url?id='
    url_wget= url_pre+musicid+'.mp3'
    r = requests.get(url_wget)
    with open(filename, "wb") as code:
        code.write(r.content)
    print((filename+'下载结束').decode('utf-8').encode(type))
    print(("=======可以继续下载或直接关闭程序========").decode('utf-8').encode(type))
if __name__ == "__main__":
    while True:
        download()
