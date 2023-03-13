# TS3Audiobot-playlist

 把自己的歌单转换成teamspeak3的歌单



## 说明

- 目前只支持网易云，且不支持vip
- 输入歌单ID自动爬取，不支持私人歌单
- 硬爬歌单转换成TS3Audiobot所使用的格式，存放在 `./bot/botname/playlists` 目录下，也可以放在自己指定的位置

生成好的文件存放在`data`目录下  

## 使用方法

1. 下载本软件

   ​	[下载地址](https://github.com/MyWifeAsuna/TS3Audiobot-playlist/releases)

   可以选择多文件版和单文件版。自动在**程序所在目录**生成文件夹

2. 寻找你想听的歌单，可以多选几个，记下他们的歌单ID

3. 打开软件输入歌单ID，自动生成歌单文件存放在`data`目录下  

4. 打开你的TS3Audiobot后台，**关闭TS3Audiobot程序**

5. 打开TS3Audiobot目录文件，找到你想存放歌单的位置

   一般为`./bot/botname/playlists` 。其中`botname`为你机器人的名字

6. 将第三步获取到的歌单文件放入其中，开启TS3Audiobot程序即可

## 更新日志

[点此查看](https://github.com/MyWifeAsuna/TS3Audiobot-playlist/blob/main/%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97.md)

## 开坑

- [ ] 网易云登陆
- [ ] 网易云翻页（一页最多一千条歌曲数据
- [x] 网易云核心
- [ ] QQ音乐
- [ ] ...

## 

**Splamy：**[TS3AudioBot](https://github.com/Splamy/TS3AudioBot)
