


from nonebot import on_command, CommandSession
from qqbot.botmain import *
from qqbot.config import *
from common.constant import *
from nonebot import permission as perm
from qqbot.awesome.plugins import pushQq
msgSuccess1="接收设置成功,接收处于 {} 状态"
msgSuccess2="发送设置成功,发送处于 {} 状态"
# msgSuccess3="管理员发送设置成功,处于 {} 状态"
msgSuccess4="艾特发送设置成功,处于 {} 状态"
msgCallBack="你没有权限!"
msgError1='指令不正确，请重新输入\n发送格式:接收 开/关'
msgError2='指令不正确，请重新输入\n发送格式:发送 开/关'
msgError3='指令不正确，请重新输入\n发送格式:管理员发送 开/关'
msgError4='指令不正确，请重新输入\n发送格式:艾特发送 开/关'
msgError5='指令不正确，请重新输入\n发送格式:世界状态 房间id'
msgError6='指令不正确，请重新输入\n发送格式:玩家列表 房间id'
#是否开启只能管理员发，
#接收开,接收关 发送开，发送关
@on_command('服务器', aliases=['',])
async def _(session: CommandSession):

    ctx = session.ctx.copy()
    senddata = "在线服务器列表(只有服务器有人才会显示)\n"
    severlist=""
    if "group_id" in ctx.keys():
        keylist = red.red.keys(pattern=PLAYCHATKEYLINE.format(ctx["group_id"],"*"))
        for key in keylist:
            key_roomId = bytes.decode(red.red.hget(key, "id"))
            roomName=bytes.decode(red.red.hget(key, "roomName"))
            severlist=severlist+"房间名:{}   房间Id:{}\n".format(roomName,key_roomId)
    if severlist=="":
        senddata=senddata+"目前暂无服务器在线"
    else:
        senddata = senddata +severlist
    await session.send(senddata)
    return

@on_command('接收', aliases=['',],permission=perm.GROUP_ADMIN)
async def _(session: CommandSession):

    ctx = session.ctx.copy()
    if "group_id" not in ctx.keys():
        return
    # if int(ctx["sender"]["user_id"]) not in SUPERUSERS:
    #     await session.send(msgCallBack)
    #     return
    stripped_arg = session.current_arg_text.strip()
    if not stripped_arg:
        await session.send(msgError1)
        return
    msgdata=stripped_arg
    # try:
    #     msgdata = stripped_arg.split(" ")[1]
    # except Exception as e:
    #     logger.error(e)
    #     await session.send(msgError1)
    #     return

    if msgdata=="开":
        red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]),"recv",str(0))
        msg = msgSuccess1.format("打开")
        await session.send(msg)
        return
    elif msgdata=="关":
        red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]), "recv", str(1))
        msg = msgSuccess1.format("关闭")
        await session.send(msg)
        return
    else:
        await session.send(msgError1)
        return

@on_command('发送', aliases=['',],permission=perm.GROUP_ADMIN)
async def _(session: CommandSession):

    ctx = session.ctx.copy()
    if "group_id" not in ctx.keys():
        return
    stripped_arg = session.current_arg_text.strip()
    if not stripped_arg:
        await session.send(msgError2)
        return
    msgdata = stripped_arg

    if msgdata=="开":
        red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]),"send",str(0))
        msg = msgSuccess2.format("打开")
        await session.send(msg)
        return
    elif msgdata=="关":
        red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]), "send", str(1))
        msg = msgSuccess2.format("关闭")
        await session.send(msg)
        return
    else:
        await session.send(msgError2)
        return

#
# @on_command('管理员发送', aliases=['',],permission=perm.GROUP_ADMIN)
# async def _(session: CommandSession):
#
#     ctx = session.ctx.copy()
#     if "group_id" not in ctx.keys():
#         return
#     # if int(ctx["sender"]["user_id"]) not in SUPERUSERS:
#     #     await session.send(msgCallBack)
#     #     return
#     stripped_arg = session.current_arg_text.strip()
#     if not stripped_arg:
#         await session.send(msgError3)
#         return
#     msgdata = stripped_arg
#
#     if msgdata=="开":
#         red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]),"admin",str(0))
#         msg = msgSuccess3.format("打开")
#         await session.send(msg)
#         return
#     elif msgdata=="关":
#         red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]), "admin", str(1))
#         msg = msgSuccess3.format("关闭")
#         await session.send(msg)
#         return
#     else:
#         await session.send(msgError3)
#         return


@on_command('艾特发送', aliases=['',],permission=perm.GROUP_ADMIN)
async def _(session: CommandSession):

    ctx = session.ctx.copy()
    if "group_id" not in ctx.keys():
        return
    # if int(ctx["sender"]["user_id"]) not in SUPERUSERS:
    #     await session.send(msgCallBack)
    #     return
    stripped_arg = session.current_arg_text.strip()
    if not stripped_arg:
        await session.send(msgError4)
        return
    msgdata = stripped_arg

    if msgdata=="开":
        red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]),"@",str(1))
        msg = msgSuccess4.format("打开")
        await session.send(msg)
        return
    elif msgdata=="关":
        red.red.hset(QQCHATKEYINFO.format(ctx["group_id"]), "@", str(0))
        msg = msgSuccess4.format("关闭")
        await session.send(msg)
        return
    else:
        await session.send(msgError4)
        return
#
@on_command('世界状态', aliases=['',])
async def _(session: CommandSession):
    ctx = session.ctx.copy()
    if "group_id" not in ctx.keys():
        return
    stripped_arg = session.current_arg_text.strip()
    if not stripped_arg:
        await session.send(msgError5)
        return
    roomId = stripped_arg
    sessionId = ""
    keylist = red.red.keys(pattern=PLAYCHATKEYLINE.format(ctx["group_id"], "*"))
    try:
        for key in keylist:
            key_roomId = red.red.hget(key, "id")
            if key_roomId != None and str(bytes.decode(key_roomId)) == roomId:
                sessionId = str(bytes.decode(red.red.hget(key, "sessionId")))
                break
        if sessionId == "":
            await session.send(pushQq.famineMsgError3.format(roomId))
            return
    except Exception as e:
        logger.error(e)

    senddata = "世界状态{}\n".format(roomId)
    worldstate=""
    key=PLAYCHATKEYLINE.format(ctx["group_id"],sessionId)
    try:
        worldstatestr=bytes.decode(red.red.hget(key, "worldstate"))
        worldstatedict = eval(worldstatestr)
        worldstate=worldstate+"天数:{}\n".format(worldstatedict["days"])
        worldstate = worldstate + "季节:{}\n".format(worldstatedict["season"])
        worldstate = worldstate + "温度:{}\n".format(worldstatedict["temperature"])
        worldstate = worldstate + "季节剩余天数:{}\n".format(worldstatedict["remainingdaysinseason"])
        #remainingdaysinseason
    except Exception as e:
        logger.error(e)
    if worldstate == "":
        senddata = senddata + "获取世界信息失败"
    else:
        senddata = senddata + worldstate
    await session.send(senddata)
    return

@on_command('玩家列表', aliases=['',])
async def _(session: CommandSession):
    ctx = session.ctx.copy()
    if "group_id" not in ctx.keys():
        return
    stripped_arg = session.current_arg_text.strip()
    if not stripped_arg:
        await session.send(msgError6)
        return
    roomId = stripped_arg
    sessionId = ""
    keylist = red.red.keys(pattern=PLAYCHATKEYLINE.format(ctx["group_id"], "*"))
    try:
        for key in keylist:
            key_roomId = red.red.hget(key, "id")
            if key_roomId != None and str(bytes.decode(key_roomId)) == roomId:
                sessionId = str(bytes.decode(red.red.hget(key, "sessionId")))
                break
        if sessionId == "":
            await session.send(pushQq.famineMsgError3.format(roomId))
            return
    except Exception as e:
        logger.error(e)
    senddata = "玩家列表{} \n".format(roomId)
    playersinfo=""
    key=PLAYCHATKEYLINE.format(ctx["group_id"],sessionId)
    try:
        playersstr=bytes.decode(red.red.hget(key, "allPlayers"))
        playerslist = eval(playersstr)
        for playersdict in  playerslist:
            playersinfo=playersinfo+"{}({})\n".format(playersdict["name"],playersdict["prefab"])
        #remainingdaysinseason
    except Exception as e:
        logger.error(e)
    if playersinfo == "":
        senddata = senddata + "获取玩家信息失败"
    else:
        senddata = senddata + playersinfo
    await session.send(senddata)
    return