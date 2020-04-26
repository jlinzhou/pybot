
import nonebot
from nonebot import on_command, CommandSession
import time
import redis
from os import path
from qqbot import config
from nonebot.log import logger
import logging
from logging.handlers import RotatingFileHandler
from common.redis import redisOpt

#
file_log_handler = RotatingFileHandler('logs/chatqq.log', maxBytes=1024*1024, backupCount=10)
# 设置日志的格式       日志等级       日志信息的文件名　　行数　　日志信息
formatter = logging.Formatter('%(asctime)s %(levelname)s  %(lineno)d %(message)s %(filename)s')
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)

red=redisOpt()








def main():
    nonebot.init(config)

    # nonebot.load_builtin_plugins()
    nonebot.load_plugins(path.join(path.dirname(__file__), 'awesome', 'plugins'),'qqbot.awesome.plugins')
    nonebot.run()
