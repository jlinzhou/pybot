from nonebot import on_command, CommandSession
from qqbot.botmain import *
from nonebot.log import logger
from common.constant import *
schedulMsg='{}:{}\n'


@nonebot.scheduler.scheduled_job('cron', second='*')
async def _():
    bot = nonebot.get_bot()
    keylist = red.red.keys(pattern=PLAYCHATKEY.format("*"))
    for key in keylist:
        keystr=bytes.decode(key)
        while 1:
            data=red.red.rpop(keystr)
            if data==None:
                break
            logger.info(data)
            try:
                strdata=bytes.decode(data)
                strdatadict=eval(strdata)
                stage=strdatadict["stage"]
                senddata=""

                if str(stage)=="1":
                    groupId = strdatadict["groupId"]
                    sessionId=strdatadict["sessionId"]
                    roomId=red.red.hget(PLAYCHATKEYLINE.format(groupId,sessionId),"id")
                    aite = red.red.hget(QQCHATKEYINFO.format(groupId), "@")
                    if aite!=None and str(bytes.decode(aite))== "1":
                        if strdatadict["message"][0]=="@":
                            senddata=strdatadict["name"]+"："+strdatadict["message"]+"\n------来自饥荒联机游戏("+strdatadict["roomName"]+")"+"\n房间Id:"+bytes.decode(roomId)
                    else:
                        senddata = strdatadict["name"] + "：" + strdatadict["message"] + "\n------来自饥荒联机游戏(" + \
                                   strdatadict["roomName"] + ")" + "\n房间Id:" + bytes.decode(roomId)
                elif str(stage)=="2":
                    card = strdatadict["card"]
                    nickname=strdatadict["nickname"]
                    message = strdatadict["message"]
                    groupId = strdatadict["groupId"]
                    name=card
                    if name=="":
                        name=nickname
                    senddata="消息反馈\n@{} {}\n发送成功".format(name,message)
            except Exception as e:
                logger.error(e)
            recv=red.red.hget(QQCHATKEYINFO.format(groupId), "recv")
            if recv==None or (recv!=None and str(bytes.decode(recv))=="0"):
                await bot.send_group_msg(group_id=int(groupId), message=senddata)


