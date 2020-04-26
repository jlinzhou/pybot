class qqChatData:
    def __init__(self):
        #, card, nickname,message,userId,groupId
        self.card = None
        self.nickname = None
        self.message = None
        self.userId = None
        self.groupId = None
        self.stage = None
    def __str__(self):
        data={}
        data["card"]=self.card
        data["nickname"] = self.nickname
        data["message"] = self.message
        data["userId"] = self.userId
        data["groupId"] = self.groupId
        data["stage"] = self.stage
        return str(data)


class playChatData:
    def __init__(self):
        #, card, nickname,message,userId,groupId
        self.guid = None
        self.sessionId = None
        self.userid = None
        self.message = None
        self.groupId = None
        self.whisper = None
        self.isemote = None
        self.name = None
        self.roomName = None
        self.prefab = None
        self.colour = None
        self.stage = None
    def __str__(self):
        data={}
        data["guid"]=self.guid
        data["sessionId"] = self.sessionId
        data["userid"] = self.userid
        data["message"] = self.message
        data["groupId"] = self.groupId
        data["whisper"] = self.whisper
        data["isemote"] = self.isemote
        data["name"] = self.name
        data["roomName"] = self.roomName
        data["prefab"] = self.prefab
        data["colour"] = self.colour
        data["name"] = self.name
        data["stage"] = self.stage #2表示反馈 1表示游戏里的
        return str(data)