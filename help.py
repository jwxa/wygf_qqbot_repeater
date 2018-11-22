# -*- coding: utf-8 -*-
import random
import time
import re
from qqbot.utf8logger import DEBUG


def onQQMessage(bot, contact, member, content):
    if ('@ME' in content and not bot.isMe(contact, member)) and  ("help" in content):
        strx =""
        strx += "辉夜自动bot系统 帮助\n"
        strx += "Ver 1.1451472\n "
        strx += "————————————\n "
        strx += "基本功能：复读\n "
        strx += "基本复读率：3%\n "
        strx += "特殊发言可以提高复读成功率\n "
        strx += "若群内发生复读，则100%跟着复读\n "
        strx += "复读被打断时有3%的几率……\n "
        strx += "————————————\n "
        strx += "模拟扭蛋功能\n "
        strx += "目前支持cgss和mltd的模拟扭蛋功能\n "
        strx += "使用方法是@本bot，然后提及cgss或者mltd\n" 
        strx += "最后加上 抽卡 即可\n "
        strx += "若最后追加 十连 可以进行十连抽卡\n "
        strx += "————————————\n"
        strx += "@本bot 支持的帮助有 Repeater\n"
        strx += "————————————"
        bot.SendTo(contact,strx)
    if ('@ME' in content and not bot.isMe(contact, member)) and  ("Repeater" in content):
        strx =""
        strx += "辉夜自动bot系统 帮助\n"
        strx += "Ver 1.1451472\n "
        strx += "————————————\n "
        strx += "复读详细帮助\n "
        strx += "基本复读率：3%\n "
        strx += "出现数字时，增加复读率5%\n "
        strx += "并且有几率将数字更变成72或者淫梦相关数字\n "
        strx += "出现‘我’时，增加复读率10% "
        strx += "并且会将我改成你 你改成他\n "
        strx += "出现索尼时\n "
        strx += "固定10%的几率回复索尼大法好\n "
        strx += "复读被中断时\n" 
        strx += "固定3%的几率回复打断复读死路一条\n "
        strx += "出现千早相关发言时30%的几率回复随机特殊内容。\n"
        strx += "还有其他内容不一一列举。\n"
        strx += "@本bot并输入startRepeat可以启用复读\n "
        strx += "@本bot并输入stopRepeat可以停止复读\n "
        strx += "———————————— "
        bot.SendTo(contact,strx)

def clear(arr):
        for i in range(len(arr)):
                arr[i]=arr[i].replace("\n",'')

def filePath(str):
    return 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\' + str



def filePath2(str, contact):
    m2=hashlib.md5()
    m2.update(contact.nick)
    strx=m2.hexdigest()
    return 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\' + strx + str
