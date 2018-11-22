# -*- coding: utf-8 -*-
import random
import time
import re
from qqbot.utf8logger import DEBUG


def onQQMessage(bot, contact, member, content):
    if (('@ME' in content and not bot.isMe(contact, member))or contact.ctype=='buddy') and '抽卡'in content and 'mltd' in content:
        if '十连' in content :
            get10card_single_stable(['SSR','SR','R'],bot,contact,member,'mltd')
        else:
            get1card_single(['SSR','SR','R'],bot,contact,member,'mltd')
        return 0
    if (('@ME' in content and not bot.isMe(contact, member))or contact.ctype=='buddy') and '抽卡'in content and 'cgss' in content:
        if '十连' in content :
            get10card_single_stable(['SSR','SR','R'],bot,contact,member,'cgss')
        else:
            get1card_single(['SSR','SR','R'],bot,contact,member,'cgss')
        return 0
    if (('@ME' in content and not bot.isMe(contact, member))or contact.ctype=='buddy') and '抽卡'in content and 'wygf' in content and (contact.nick=="雾雨工坊🐍豹群"):
        if '十连' in content :
            get10card_single_stable(['★5','★4','★3'],bot,contact,member,'wygf')
        else:
            get1card_single(['★5','★4','★3'],bot,contact,member,'wygf')
        return 0
    if (('@ME' in content and not bot.isMe(contact, member))or contact.ctype=='buddy') and '抽卡'in content and 'sc' in content:
        if '十连' in content :
            get10card_excellent_stable(bot,contact,member,'sc')
        else:
            get1card_excellent(bot,contact,member,'sc')
        return 0
    
def getcard_excellent(kind,gameStr):
    f=open(filePath(gameStr+'kind.txt'),'r')
    karr=f.readlines()
    clear(karr)
    f.close()
    print (gameStr+kind+'rate.txt')
    f=open(filePath(gameStr+kind+'rate.txt'),'r')
    rarr=f.readlines()
    clear(rarr)
    f.close()
    allRate=0
    for i in range(len(rarr)):
        rarr[i]=int(rarr[i])
        allRate+=rarr[i]
    rnd_c=random.randint(1,allRate)
    now_c = 0
    k = 0
    while now_c+rarr[k]<rnd_c :
        k+=1
        now_c+=rarr[k]
    f=open(filePath(gameStr+karr[k]+'.txt'),'r')
    carr=f.readlines()
    clear(carr)
    f.close()
    return (karr[k]+' '+carr[random.randint(0,len(carr)-1)])
    
    

def get1card_excellent(bot,contact,member,gameStr):
    List=getcard_excellent('',gameStr)
    f=open(filePath(gameStr+'name.txt'),'r')
    ex=f.readline()
    f.close()
    if contact.ctype=='buddy':
        ex2="你"
    else:
        ex2="@"+member.nick
    ex2=ex2+"抽了1次"
    List=exchange(List,gameStr)
    bot.SendTo(contact,ex2+ex+" ，获得了\n"+List)
    return 0

def get10card_excellent_stable(bot,contact,member,gameStr):
    List=''
    for i in range(9):
        List=List+"\n"+getcard_excellent('',gameStr)
    List=List+"\n"+getcard_excellent('SR',gameStr)
    f=open(filePath(gameStr+'name.txt'),'r')
    ex=f.readline()
    f.close()
    if contact.ctype=='buddy':
        ex2="你"
    else:
        ex2="@"+member.nick
    ex2=ex2+"抽了10次卡"
    List=exchange(List,gameStr)
    bot.SendTo(contact,ex2+ex+" ，获得了\n"+List)

def get10card_excellent_flexible(bot,contact,member,gameStr):
    List=''
    SR=False
    for i in range(9):
        Temp=getcard_excellent('',gameStr)
        if SR_include(Temp,gameStr):
            SR=True
        List=List+"\n"+Temp
    if SR==False:
        List=List+"\n"+getcard_excellent('SR',gameStr)
    else:
        List=List+"\n"+getcard_excellent('',gameStr)
    f=open(filePath(gameStr+'name.txt'),'r')
    ex=f.readline()
    f.close()
    if contact.ctype=='buddy':
        ex2="你"
    else:
        ex2="@"+member.nick
    ex2=ex2+"抽了1次卡"
    List=exchange(List,gameStr)
    bot.SendTo(contact,ex2+ex+" ，获得了\n"+List)

def SR_include(card,gameStr):
    f=open(filePath(gameStr+'SRkind.txt'),'r')
    arr=f.readlines()
    clear(arr)
    f.close()
    for i in arr:
        if (i in card) : return True
    return False

def exchange(List,gameStr):
    f=open(filePath(gameStr+'kind.txt'),'r')
    arr1=f.readlines()
    clear(arr1)
    f.close()
    f=open(filePath(gameStr+'kname.txt'),'r')
    arr2=f.readlines()
    clear(arr2)
    f.close()
    Temp=List
    Temp=Temp.replace('pickup','')
    for i in range(len(arr1)):
        Temp=Temp.replace(arr1[i],arr2[i])
    return Temp
    
def get1card_single(sar,bot,contact,member,gameStr):
    List=getcard_single(sar,gameStr)
    f=open(filePath(gameStr+'name.txt'),'r')
    ex=f.readline()
    f.close()
    if contact.ctype=='buddy':
        ex2="你"
    else:
        ex2="@"+member.nick
    ex2=ex2+"抽了1次"
    bot.SendTo(contact,ex2+ex+" ，获得了\n"+List)
    return 0

def get10card_single_stable(sar,bot,contact,member,gameStr):
    List=''
    for i in range(9):
        List=List+"\n"+getcard_single(sar,gameStr)
    List=List+"\n"+getSRcard_single(sar,gameStr)
    f=open(filePath(gameStr+'name.txt'),'r')
    ex=f.readline()
    f.close()
    if contact.ctype=='buddy':
        ex2="你"
    else:
        ex2="@"+member.nick
    ex2=ex2+"抽了1次卡"
    bot.SendTo(contact,ex2+ex+" ，获得了\n"+List)


def getcard_single(sar,gameStr):
    f=open(filePath(gameStr+'Rate.txt'),'r')
    SSR_rate=int(f.readline())
    SR_rate=int(f.readline())
    R_rate=int(f.readline())
    SSR_prate=0
    SR_prate=0
    R_prate=0
    f.close
    rnd_num = random.randint(1, SSR_rate+SR_rate+R_rate)
    if rnd_num<=SSR_rate:
        f=open(filePath(gameStr+'SSRpickupList.txt'),'r')
        x=f.readline()
        SSR_prate=int(f.readline())
        if rnd_num<=SSR_prate:
            x=f.readline()
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[0]+' '+arr[rnd_2-1]
        else:
            f.close()
            f=open(filePath(gameStr+'SSRList.txt'),'r')
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[0]+' '+arr[rnd_2-1]
    if rnd_num<=SSR_rate+SR_rate:
        f=open(filePath(gameStr+'SRpickupList.txt'),'r')
        x=f.readline()
        SR_prate=int(f.readline())
        if rnd_num<=SSR_rate+SR_prate:
            x=f.readline()
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[1]+' '+arr[rnd_2-1]
        else:
            f.close()
            f=open(filePath(gameStr+'SRList.txt'),'r')
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[1]+' '+arr[rnd_2-1]
    if rnd_num<=SSR_rate+SR_rate+R_rate:
        f=open(filePath(gameStr+'RpickupList.txt'),'r')
        x=f.readline()
        R_prate=int(f.readline())
        if rnd_num<=SSR_rate+SR_rate+R_prate:
            x=f.readline()
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[2]+' '+arr[rnd_2-1]
        else:
            f.close()
            f=open(filePath(gameStr+'RList.txt'),'r')
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[2]+' '+arr[rnd_2-1]

def getSRcard_single(sar,gameStr):
    f=open(filePath(gameStr+'SR_Rate.txt'),'r')
    SSR_rate=int(f.readline())
    SR_rate=int(f.readline())
    R_rate=int(f.readline())
    SSR_prate=0
    SR_prate=0
    R_prate=0
    f.close
    rnd_num = random.randint(1, SSR_rate+SR_rate+R_rate)
    print(rnd_num)
    if rnd_num<=SSR_rate:
        f=open(filePath(gameStr+'SSRpickupList.txt'),'r')
        x=f.readline()
        x=f.readline()
        SSR_prate=int(f.readline())
        if rnd_num<=SSR_prate:
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[0]+' '+arr[rnd_2-1]
        else:
            f.close()
            f=open(filePath(gameStr+'SSRList.txt'),'r')
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[0]+' '+arr[rnd_2-1]
    if rnd_num<=SSR_rate+SR_rate:
        f=open(filePath(gameStr+'SRpickupList.txt'),'r')
        x=f.readline()
        x=f.readline()
        SR_prate=int(f.readline())
        if rnd_num<=SSR_rate+SR_prate:
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[1]+' '+arr[rnd_2-1]
        else:
            f.close()
            f=open(filePath(gameStr+'SRList.txt'),'r')
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[1]+' '+arr[rnd_2-1]
    if rnd_num<=SSR_rate+SR_rate+R_rate:
        f=open(filePath(gameStr+'RpickupList.txt'),'r')
        x=f.readline()
        x=f.readline()
        R_prate=int(f.readline())
        if rnd_num<=SSR_rate+SR_rate+R_prate:
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[2]+' '+arr[rnd_2-1]
        else:
            f.close()
            f=open(filePath(gameStr+'RList.txt'),'r')
            arr=f.readlines()
            clear(arr)
            num=len(arr)
            rnd_2=random.randint(1, num)
            f.close()
            return sar[2]+' '+arr[rnd_2-1]    
    
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

