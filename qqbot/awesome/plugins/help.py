
from nonebot import on_command, CommandSession
from qqbot.botmain import *

helpmsg= '我现在支持的功能有：\n\n'+\
         '如何使用，指令：如何使用\n' \
         '使用帮助，指令：帮助\n' \
         '查看在线服务器，指令：服务器\n' \
         '查询世界状态,指令格式:世界状态 房间id\n' \
         '查询玩家列表,指令格式:玩家列表 房间id\n' \
         '发送游戏服务器消息,指令格式:23 房间id 消息\n' \
         '\n下面指令只能管理员使用\n'\
         '1、接收消息(即从游戏里接收消息),指令格式:接收 开/关\n' \
         '2、发送消息(即从qq里发送消息),指令格式:发送 开/关\n' \
         '3、艾特发送设置(即游戏里的消息开头加上@才能发送到群里),指令格式:艾特发送 开/关\n'


# '4、管理员发送(即只能管理员发送qq消息到游戏里),指令格式:管理员发送 开/关\n'
@on_command('usage', aliases=['使用帮助', '帮助', '使用方法'])
async def _(session: CommandSession):
    ctx = session.ctx.copy()
    if "group_id" in ctx.keys():
        await session.send(helpmsg)
    return
@on_command('如何使用', aliases=[''])
async def _(session: CommandSession):
    ctx = session.ctx.copy()
    if "group_id" in ctx.keys():
        await session.send(
            '''chat(游戏与qq消息互通)
即在游戏打字qq群能看见，在qq群打字游戏里能看见。 
需要两步操作实现。
第一步，把qq机器人拉入群中
第二步，mod配置填好自己的qq群号
想拉qq机器人入群的把qq群私聊发给不死(qq772945866)，机器人等会申请进群，通过一下
 ''')
    return