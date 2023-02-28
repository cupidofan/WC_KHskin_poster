import requests
from lxml import etree
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'}

hero_list_url='https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url,headers=headers)
# hero_list_resp.encoding='gbk'
# print(hero_list_resp.json())

for h in hero_list_resp.json():
    ename=h.get('ename')
    cname=h.get('cname')

    if not os.path.exists(cname):
        os.makedirs(cname)
    hero_info_url =f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(hero_info_url,headers = headers)
    hero_info_resp.encoding = 'gbk'
    e = etree.HTML(hero_info_resp.text)
    names_f = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    if ename==540 or ename==542 or ename==534:
        names = [name for name in names_f.split('|')]
        print(names_f)
    else:
        names = [name[0:name.index('&')] for name in names_f.split('|')]#这句太屌了，好好学着点
    
        
        # url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg'
        # resp = requests.get(url, headers = headers)
        # e=etree.HTML(resp.content)
        # # 保存图片 
        # with open(f'{cname}/{n}.jpg','wb') as img_file:
        #     img_file.write(resp.content)
        # print(f'已下载：{n}的图片海报')

    # 发送请求
    for i,n in enumerate(names):
        url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg'
        resp = requests.get(url, headers = headers)
        e=etree.HTML(resp.content)
        # 保存图片
        with open(f'{cname}/{n}.jpg','wb') as img_file:
            img_file.write(resp.content)
        print(f'已下载：{n}的图片海报')


# 接收服务器响应的图片

