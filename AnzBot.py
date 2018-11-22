# -*- coding: utf-8 -*-
from qqbot import qqbotsched

@qqbotsched(hour='7', minute='0')
def mytask(bot):
    gl = bot.List('group', '雾雨工坊🐍豹群')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, 'みなさん！おはようございまーっす♪\n今日も一日、元気いっぱいがんばろー！')

            
