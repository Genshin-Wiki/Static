import requests
import os

x = input()

url = "https://upload-bbs.mihoyo.com/game_record/genshin/equip/UI_RelicIcon_" + x + "_1.png"
d = 'C:\\Users\\Lenovo\\Desktop\\genshin_icons\\reliquaries\\'
path = d + url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")
url = "https://upload-bbs.mihoyo.com/game_record/genshin/equip/UI_RelicIcon_" + x + "_2.png"
d = 'C:\\Users\\Lenovo\\Desktop\\genshin_icons\\reliquaries\\'
path = d + url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")
url = "https://upload-bbs.mihoyo.com/game_record/genshin/equip/UI_RelicIcon_" + x + "_3.png"
d = 'C:\\Users\\Lenovo\\Desktop\\genshin_icons\\reliquaries\\'
path = d + url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")
url = "https://upload-bbs.mihoyo.com/game_record/genshin/equip/UI_RelicIcon_" + x + "_4.png"
d = 'C:\\Users\\Lenovo\\Desktop\\genshin_icons\\reliquaries\\'
path = d + url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")
url = "https://upload-bbs.mihoyo.com/game_record/genshin/equip/UI_RelicIcon_" + x + "_5.png"
d = 'C:\\Users\\Lenovo\\Desktop\\genshin_icons\\reliquaries\\'
path = d + url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:
        print("图片已存在")
except:
    print("图片获取失败")
