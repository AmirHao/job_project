#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/11/25
from xml.dom import minidom

import itchat
from itchat.content import *
import os
import time

# 这是保存撤回消息的文件目录(如：图片、语音等)，这里已经写死了，大家可以自行修改
temp = "../ignore_data" + "/" + "撤回的消息"
if not os.path.exists(temp):
    os.mkdir(temp)

itchat.auto_login(True)  # 自动登录

local_dict = {}  # 定义一个字典


# 这是一个装饰器，给下面的函数添加新功能
# 能够捕获好友发送的消息，并传递给函数参数msg
@itchat.msg_register(
    [TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO]
)  # 文本，语音，图片
def resever_info(msg):
    global local_dict  # 声明全局变量

    info = msg["Text"]  # 取出消息内容
    msgId = msg["MsgId"]  # 取出消息标识
    info_type = msg["Type"]  # 取出消息类型
    name = msg["FileName"]  # 取出消息文件名
    # 取出消息发送者标识并从好友列表中检索
    fromUser = itchat.search_friends(userName=msg["FromUserName"])["NickName"]
    ticks = msg["CreateTime"]  # 获取信息发送的时间
    time_local = time.localtime(ticks)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)  # 格式化日期
    # 将消息标识和消息内容添加到字典
    # 每一条消息的唯一标识作为键，消息的具体信息作为值，也是一个字典
    local_dict[msgId] = {
        "info": info,
        "info_type": info_type,
        "name": name,
        "fromUser": fromUser,
        "dt": dt,
    }


@itchat.msg_register(NOTE)  # 监听系统提示
def note_info(msg):
    # 监听撤回了一条消息到好友撤回了一条消息
    if "" in msg["Text"]:
        # 获取系统消息中的Content结点值
        content = msg["Content"]
        # Content值为xml，解析xml
        doc = minidom.parseString(content)
        # 取出msgid标签的值
        result = doc.getElementsByTagName("msgid")
        # 该msgId就是撤回的消息标识，通过它可以在字典中找到撤回的消息信息
        msgId = result[0].childNodes[0].nodeValue
        # 从字典中取出对应消息标识的消息类型
        msg_type = local_dict[msgId]["info_type"]
        if msg_type == "Recording":  # 撤回的消息为语音
            recording_info = local_dict[msgId]["info"]  # 取出消息标识对应的消息内容
            info_name = local_dict[msgId]["name"]  # 取出消息文件名
            fromUser = local_dict[msgId]["fromUser"]  # 取出发送者
            dt = local_dict[msgId]["dt"]  # 取出发送时间
            recording_info(temp + "/" + info_name)  # 保存语音
            # 拼接提示消息
            send_msg = "【发送人:】" + fromUser + "\n" + "发送时间:" + dt + "\n" + "撤回了一条语音"
            itchat.send(send_msg, "filehelper")  # 将提示消息发送给文件助手
            # 发送保存的语音
            itchat.send_file(temp + "/" + info_name, "filehelper")
            del local_dict[msgId]  # 删除字典中对应的消息
            print("保存语音")
        elif msg_type == "Text":
            text_info = local_dict[msgId]["info"]  # 取出消息标识对应的消息内容
            fromUser = local_dict[msgId]["fromUser"]  # 取出发送者
            dt = local_dict[msgId]["dt"]  # 取出发送时间
            # 拼接提示消息
            send_msg = (
                "【发送人:】" + fromUser + "\n" + "发送时间:" + dt + "\n" + "撤回内容:" + text_info
            )
            # 将提示消息发送给文件助手
            itchat.send(send_msg, "filehelper")
            del local_dict[msgId]  # 删除字典中对应的消息
            print("保存文本")
        elif msg_type == "Picture":
            picture_info = local_dict[msgId]["info"]  # 取出消息标识对应的消息内容
            fromUser = local_dict[msgId]["fromUser"]  # 取出发送者
            dt = local_dict[msgId]["dt"]  # 取出发送时间
            info_name = local_dict[msgId]["name"]  # 取出文件名
            picture_info(temp + "/" + info_name)  # 保存图片
            # 拼接提示消息
            send_msg = "【发送人:】" + fromUser + "\n" + "发送时间:" + dt + "\n" + "撤回了一张图片"
            itchat.send(send_msg, "filehelper")  # 将图片发送给文件助手
            # 发送保存的语音
            itchat.send_file(temp + "/" + info_name, "filehelper")
            del local_dict[msgId]  # 删除字典中对应的消息
            print("保存图片")


itchat.run()
