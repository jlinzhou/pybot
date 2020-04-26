from flask import Flask,Blueprint,send_file,request,jsonify
import logging
from logging.handlers import RotatingFileHandler
from common.redis import redisOpt
from common.constant import *
from common.models import *
logging.basicConfig(level=logging.DEBUG)
file_log_handler = RotatingFileHandler('logs/chatplay.log', maxBytes=1024*1024, backupCount=10)
formatter = logging.Formatter('%(asctime)s %(levelname)s  %(lineno)d %(message)s %(filename)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)
app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False
red=redisOpt()
@app.route('/playchat',methods=["POST"])
def playchat():

    data=request.get_json()
    try:
        groupId=data['groupId']
        sessionId = data['sessionId']
        if groupId!='' and sessionId!='':
            recvdata=playChatData()
            recvdata.guid =data['guid']
            recvdata.sessionId = data['sessionId']
            recvdata.userid = data['userid']
            recvdata.message = data['message']
            recvdata.groupId = data['groupId']
            recvdata.whisper = data['whisper']
            # recvdata.isemote = data['isemote']
            recvdata.name = data['name']
            recvdata.roomName = data['roomName']
            recvdata.prefab = data['prefab']
            recvdata.colour = data['colour']
            recvdata.stage = "1"
            red.pushPlay(groupId,str(recvdata))
        else:
            red.pushPlayError(PLAYCHATKEYError, str(data))
    except Exception as e:
        logging.error(e)
    return 'ok'

#先判断这个可以在redis有没有，没有就获取所有chatplayline,并计算最大值，设置key的值为这个最大值

@app.route('/qqchat',methods=["POST"])
def qqchat():
    data=request.get_json()
    if "groupId" in data.keys() and "sessionId" in data.keys():
        groupId=data["groupId"]
        sessionId = data["sessionId"]
        senddata=red.popQQ(groupId,sessionId,data)
        return jsonify(senddata)
    else:
        logging.error("request data error")



@app.before_request
def before_request():
    pass
def main():
    app.run(
        host='0.0.0.0',
        port=9080,
        debug=False
    )
