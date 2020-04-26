
import redis
from common.initCommon  import config
from common.constant import *
from common.models import *
class redisOpt:
    def __init__(self):
        pool = redis.ConnectionPool(host=config["redis"]["ip"], port=config["redis"]["port"], db=config["redis"]["db"], password=config["redis"]["password"])
        self.red = redis.Redis(connection_pool=pool)
    def pushQQ(self,groupId,sessionId,data):
        key = QQCHATKEY.format(groupId,sessionId)
        self.red.lpush(key,data)
        self.red.expire(key, QQ_Expire_Time)
    def popQQ(self,groupId,sessionId,data):
        senddata = {"args": {"qqMessage": []}}
        keyline = PLAYCHATKEYLINE.format(groupId,sessionId)

        ########################
        if not self.red.exists(keyline):
            keylineXX = PLAYCHATKEYLINE.format(groupId, "*")
            keylist = self.red.keys(pattern=keylineXX)
            maxId=0
            for key in keylist:
                id=int(self.red.hget(key,"id"))
                # sessionId = int(self.red.get(key, "sessionId"))
                if id>maxId:
                    maxId=id
            maxId+=1
            self.red.hset(keyline,"id",str(maxId))
            self.red.hset(keyline, "sessionId", str(sessionId))
            self.red.hset(keyline, "roomName", data["roomName"])
            self.red.expire(keyline, 30)
        ############################
        if "allPlayers" in data.keys() and "worldstate" in data.keys():
            self.red.hset(keyline, "allPlayers", str(data["allPlayers"]))
            self.red.hset(keyline, "worldstate", str(data["worldstate"]))
            self.red.expire(keyline, 30)

        while 1:
            datastr = self.red.rpop(QQCHATKEY.format(groupId,sessionId))
            if datastr == None:
                break
            strdata=bytes.decode(datastr)
            strdatadict = eval(strdata)
            # datadict=qqChatData()
            datadict={}
            datadict["card"]=strdatadict["card"]
            datadict["nickname"] = strdatadict["nickname"]
            datadict["message"] = strdatadict["message"]
            datadict["userId"] = strdatadict["userId"]
            datadict["groupId"] = strdatadict["groupId"]
            datadict["stage"] = "2"
            self.pushPlay(groupId, str(datadict))
            senddata["args"]["qqMessage"].append(datadict)
        return senddata

    def pushPlay(self,groupId,data):
        key = PLAYCHATKEY.format(groupId)
        self.red.lpush(key,data)
        self.red.expire(key, Play_Expire_Time)

    def pushPlayError(self, groupId, data):
        key = PLAYCHATKEY.format(groupId)
        self.red.lpush(key, data)
        # self.red.expire(key, Play_Expire_Time)
    def popPlay(self,groupId):
        key = PLAYCHATKEY.format(groupId)
        data = self.red.rpop(key)
        return data