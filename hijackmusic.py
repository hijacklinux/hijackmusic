#!/usr/bin/python
#-*- coding:utf-8 -*-
#author = 'hijacklinux'
#useage:python hijacklinux.py filename.mp3 link

import sys
import re
import os

filename = 'downloadmusic/'+sys.argv[1]
url_in = sys.argv[2]
patt = r".*id=(\d+)"
musicid = re.match(patt,url_in).group(1)
url_pre = 'http://music.163.com/song/media/outer/url?id='
url_wget= url_pre+musicid+'.mp3'
cmd = 'wget -O '+filename+' '+url_wget
os.system(cmd)
print('作者：hijacklinux')
