from nonebot import on_command, CommandSession
from qqbot.botmain import *
from nonebot.log import logger
from common.models import *
from qqbot.config import *
from common.constant import *
famineMsgError1='要发送到服务器的id不能为空呢，请重新输入\n发送格式:23 房间id 消息'
famineMsgError2='要发送到服务器的格式不正确，请重新输入\n发送格式:23 房间id 消息'
famineMsgError3='找不到房间号为{}的服务器'
@on_command('23', aliases=('',))
async def pushqq(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    if not stripped_arg:
        await session.send(famineMsgError1)
        return
    try:
        msgdata = stripped_arg.split(" ")[1]
        roomId = stripped_arg.split(" ")[0]
    except Exception as e:
        logger.error(e)
        await session.send(famineMsgError2)
        return

    ctx=session.ctx.copy()
    savedata=qqChatData()
    sessionId=""
    if "group_id" in ctx.keys():
        try:
            keylist = red.red.keys(pattern=PLAYCHATKEYLINE.format(ctx["group_id"],"*"))
            for key in keylist:
                key_roomId = red.red.hget(key, "id")
                if key_roomId!=None and str(bytes.decode(key_roomId))==roomId:
                    sessionId=str(bytes.decode(red.red.hget(key, "sessionId")))
                    break
            if sessionId=="":
                await session.send(famineMsgError3.format(roomId))
                return
        except Exception as e:
            logger.error(e)

        try:
            savedata.card=ctx["sender"]["card"]
            savedata.nickname = ctx["sender"]["nickname"]
            savedata.message=msgdata
            savedata.card = ctx["sender"]["card"]
            savedata.userId=ctx["sender"]["user_id"]
            savedata.groupId=ctx["group_id"]
            send = red.red.hget(QQCHATKEYINFO.format(savedata.groupId), "send")
            adminSend = red.red.hget(QQCHATKEYINFO.format(savedata.groupId), "admin")
            if adminSend!=None and str(bytes.decode(adminSend))== "1" and savedata.userId not in SUPERUSERS:
                await session.send("您不是管理员，没有权限发送")
                return

            if send!=None and str(bytes.decode(send))== "1":
                await session.send("当前发送已关闭")
                return
            else:
                red.pushQQ(savedata.groupId, sessionId, str(savedata))
                return
        except Exception as e:
            logger.error(e)
    else:
        pass
