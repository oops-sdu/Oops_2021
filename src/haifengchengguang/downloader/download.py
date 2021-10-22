# -*- coding:utf-8 -*-
import requests



# 下载源代码
def download_page(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Cookie':'ll="118220"; bid=prHoQKxswFs; ap_v=0,6.0; dbcl2="177972734:32HQ2fYXHbE"; ck=ulvM; push_noty_num=0; push_doumail_num=0'
            }
    html=requests.get(url,headers=header).content
    return html

