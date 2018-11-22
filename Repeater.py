# -*- coding: utf-8 -*-
import random
import time
import re
import hashlib  
from qqbot.utf8logger import DEBUG


def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):
        return 0
    f=open(filePath('RepeatSettings',contact),'a')
    f.close()
    f=open(filePath('RepeatSettings',contact),'r')
    repeatOrNot=f.readline()
    f.close()
    if  not (bot.isMe(contact, member)) and ("startRepeat" in content):
        f=open(filePath('RepeatSettings',contact),'w')
        f.write('True')
        bot.SendTo(contact,"复读开始")
        return 0
    if  not (bot.isMe(contact, member)) and ("stopRepeat" in content):
        f=open(filePath('RepeatSettings',contact),'w')
        f.write('False')
        bot.SendTo(contact,"复读停止")
        return 0
    if repeatOrNot=='False' :
        return 0
    if ('http'in content) or ('www' in content) or ('.com' in content) or ('.cn' in content) or ('.org' in content):
        return 0
    f=open(filePath('Repeated',contact),'a')
    f.close()
    f=open(filePath('Repeated',contact),'r')
    strxx=f.readline()
    if strxx==content:
        f.close()
        return 0
    f.close()
    f=open(filePath('Before',contact),'a')
    f.close()
    f=open(filePath('Before',contact),'r')
    beforeStr=f.readline()
    f.close()
    specialRepeat=specialR(bot, contact, member, content)
    if correctcontact(contact)is True and specialRepeat is False and not ('@ME' in content):
        str = content
        keyword = ["我", "你"]
        replace_str = ["你", "他"]
        replace_num = ["114514", "810", "364", "1919", "72"]
        repeat_rate = 3
        num_arr = re.findall(r"\d+\.?\d*", str)
        num_len = len(num_arr)
        strRe = False
        if num_len > 0:
            DEBUG("rate20")
            repeat_rate += 5
        if str.find(keyword[0]) > -1:
            repeat_rate += 10
            DEBUG("rate50")
            strRe = True
        if str==beforeStr:
            repeat_rate += 100
        if rate(repeat_rate) is True:
            #if strRe is True : str = str.replace(keyword[1], replace_str[1]).replace(keyword[0], replace_str[0])
            #DEBUG(str)
            #for i in num_arr:
            #    if i in replace_num:
            #        DEBUG("已经存在关键数字 ，不操作")
            #    else:
            #        if len(i) > 8:
            #            str = str.replace(i, "1145141919")
            #        elif len(i) > 6:
            #            str = str.replace(i, "114514")
            #        else:
            #            rnd2 = random.randint(1,100)
            #            if rnd2 > 50 :
            #                str = str.replace(i, replace_num[random.randint(0, 4)])
            #DEBUG(str)
            if strRe is True : str = str.replace(keyword[1], replace_str[1]).replace(keyword[0], replace_str[0])
            split_arr = re.split(r"\d+\.?\d*", str)
            new_content = split_arr[0]
            for index, num_str in enumerate(num_arr):
                print index
                print num_str
                if num_str in replace_num:
                    print("已经存在关键数字 ，不操作")
                    new_content += num_str
                else:
                    if len(num_str) > 8:
                        new_content += "1145141919"
                    elif len(num_str) > 6:
                        new_content += "114514"
                    else:
                        new_content += replace_num[random.randint(0, 4)]
                new_content += split_arr[index+1]
            time.sleep(3)
            f=open(filePath('Repeated',contact),'w')
            f.write(new_content)
            f.close()
            bot.SendTo(contact,new_content)


def rate(rate_num):
        rnd_num = random.randint(1, 100)
        if rnd_num <= rate_num:
            return True
        else:
            return False

def specialR(bot, contact, member, content):
    if correctcontact(contact) is True and not bot.isMe(contact, member):
        str=content
        f=open(filePath('Before',contact),'a')
        f.close()
        f=open(filePath('Before',contact),'r')
        beforeStr=f.readline()
        f.close()
        f=open(filePath('Before',contact),'w')
        f.write(content)
        sony_key=str.find('索尼')
        f=open(filePath('Combo',contact),'a')
        f.close()
        f=open(filePath('Combo',contact),'r')
        combo=f.readline()
        f.close()
        f=open(filePath('Combo',contact),'w')
        if beforeStr==str:
            f.write('True')
        else:
            f.write('False')
        f.close()
        if (("如月" in content) or ("缺德" in content) or ("千早" in content) or ("72" in content) or ("7.2" in content))and rate(30):
            time.sleep(1)
            rnd2 = random.randint(1,5)
            if rnd2 == 1:
                bot.SendTo(contact,'啥72啊')
            if rnd2 == 2:
                bot.SendTo(contact,'胸不平何以平天下')
            if rnd2 == 3:
                bot.SendTo(contact,'那咋72啊')
            if rnd2 == 4:
                bot.SendTo(contact,'太平公主')
            if rnd2 == 5:
                bot.SendTo(contact,'雾雨工坊天天72在线')
            return True
        if ("色图" in content)and rate(30):
            time.sleep(1)
            rnd2 = random.randint(1,10)
            if rnd2 <= 7:
                bot.SendTo(contact,'我要1份色图')
            if rnd2 == 8:
                bot.SendTo(contact,'我要2份色图')
            if rnd2 == 9:
                bot.SendTo(contact,'我要3份色图')
            if rnd2 == 10:
                bot.SendTo(contact,'我要72份色图')
            return True
        if ("新宝岛" in content)and rate(15):
            bot.SendTo(contact,'股 间 强 打')
            return True
        if (("恶臭" in content) or ("野兽" in content) or ("田所" in content) or ("114514" in content) or ("先辈" in content) or ("红茶" in content)):
            time.sleep(1)
            rnd2 = random.randint(1,4)
            if rnd2 == 1:
                bot.SendTo(contact,'这个可以有（赞赏）')
            if rnd2 == 2:
                bot.SendTo(contact,'こ↑こ↓')
            if rnd2 == 3:
                bot.SendTo(contact,'先辈的红茶（100%昏睡）')
            if rnd2 == 4:
                bot.SendTo(contact,'ファッ！？')
            return True
        if (("便乘" in content)and rate(15)):
            time.sleep(1)
            bot.SendTo(contact,'そうだよ')
            return True
        if (("龙" in content)and rate(15)):
            time.sleep(1)
            bot.SendTo(contact,'你舍得打破这份宁静吗')
            return True
        if (sony_key > -1) and rate(10) :
            time.sleep(2)
            bot.SendTo(contact,'索尼大法好')
            return True
        if combo== 'True' and beforeStr!=str and rate(3):
            time.sleep(2)
            bot.SendTo(contact,'打断复读死路一条')
            f=open(filePath('Combo',contact),'w')
            f.write('False')
            f.close()
            return True
    return False


def clear(arr):
        for i in range(len(arr)):
                arr[i]=arr[i].replace("\n",'')

def filePath(str, contact):
    m2=hashlib.md5()
    m2.update(contact.nick)
    strx=m2.hexdigest()
    return 'C:\\Users\\Administrator\\.qqbot-tmp\\plugins\\' + strx + str 

def correctcontact(contact):
    if contact.nick=='GGA蝗虫':return True
    if contact.nick=='雾雨工坊🐍豹群':return True
    if contact.nick=='戯れ天使の楽園':return True
    return False
    
