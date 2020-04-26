## 饥荒联机聊天与qq群互通

 	

总体思路：服务器这边有两个进程，一个进程是单纯的http服务器，用来接受饥荒的消息和发送qq群的消息，另一个是用[ nonebot ](https://nonebot.cqp.moe/ )这个qq机器人框架，用来发送饥荒的消息和接受qq群的消息，消息都是存到redis进行操作的 。



### 1.Flask服务器

在文件夹playServer中，定义了两个路由:

* playchat，接收游戏里的消息存储到redis
* qqchat，向游戏发送redis里面保存qq群的消息



```python
#运行
python  runflask.py
```





### 2.Nonebot qq机器人

需要有先运行酷Q ，参考资料: https://nonebot.cqp.moe/ 

```python
#运行
python  runbot.py
```



### 3.steam mod链接

https://steamcommunity.com/sharedfiles/filedetails/?id=1955543584



### 4.注意事项

* 1. 先安装python包，pip install requirements.txt，安装后运行第二步可能还会报错，继续安装 pip install "nonebot[scheduler]" 即可

* 2. 需要安装redis，redis的配置参数可在initCommon中更改

* 3. 需要仔细更改  酷Q Air\data\app\io.github.richardchien.coolqhttpapi\config中配置文件的端口ip，得与qqbot  python文件中的一致。很容易出现反向 WebSocket（Event）客户端连接失败或异常断开，将在 3000 毫秒后尝试重连  错误.

* 4. mod的端口ip请于flask的端口ip一致

* 5. 酷Q、runbot.py、runflask.py、mod同时运行正常，才算正常

     

