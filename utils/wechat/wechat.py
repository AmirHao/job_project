#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = hzm
# __date__ = 2021/11/25
import datetime
import re

from xml.dom import minidom  # noqa

import itchat
from itchat.content import *
import os
import time

type_dict = {
    "Picture": "撤回了一张图片",
    "Recording": "撤回了一条语音",
    "Video": "撤回了一个视频",
    "Attachment": "撤回了一个文件",
    "Card": "撤回了分享的名片",
}

# 这是保存撤回消息的文件目录(如：图片、语音等)
temp = f"{os.path.abspath('../')}/ignore_data/撤回的消息"
if not os.path.exists(temp):
    os.mkdir(temp)

itchat.auto_login(True)  # 自动登录

local_dict = {}  # 定义一个字典
face_bug = None  # 针对表情包的内容


# 能够捕获好友发送的消息，并传递给函数参数msg
@itchat.msg_register(
    [TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],
    isFriendChat=True,
    isGroupChat=True,
)  # 文本，语音，图片
def resever_info(msg):
    global local_dict  # 声明全局变量
    global face_bug

    if "ActualNickName" in msg:  # ActualNickName : 实际 NickName(昵称) 群消息里(msg)才有这个值
        from_user = msg["ActualUserName"]  # 群消息的发送者,用户的唯一标识
        fromUser = msg["ActualNickName"]  # 发送者群内的昵称
        friends = itchat.get_friends(update=True)  # 获取所有好友
        for f in friends:
            if from_user == f["UserName"]:  # 如果群消息是好友发的
                if f["RemarkName"]:  # 优先使用好友的备注名称，没有则使用昵称
                    fromUser = f["RemarkName"]
                else:
                    fromUser = f["NickName"]
                break
        groups = itchat.get_chatrooms(update=True)  # 获取所有的群
        group_name, group_menbers = "", None
        for g in groups:
            if msg["FromUserName"] == g["UserName"]:  # 根据群消息的FromUserName匹配是哪个群
                group_name = g["NickName"]
                group_menbers = g["MemberCount"]
                break
        group_name = f"{group_name}({group_menbers})"
    else:
        if itchat.search_friends(userName=msg["FromUserName"])[
            "RemarkName"
        ]:  # 优先使用备注名称
            fromUser = itchat.search_friends(userName=msg["FromUserName"])["RemarkName"]
        else:
            # 在好友列表中查询发送信息的好友昵称
            fromUser = itchat.search_friends(userName=msg["FromUserName"])["NickName"]
        group_name = ""

    info = msg["Text"]  # 取出消息内容
    msgId = msg["MsgId"]  # 取出消息标识
    info_type = msg["Type"]  # 取出消息类型
    name = msg["FileName"]  # 取出消息文件名
    ticks = msg["CreateTime"]  # 获取信息发送的时间
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ticks))  # 格式化日期
    msg_share_url = ""  # 记录分享的url

    if info_type in ("Text", "Friends"):  # 如果发送的消息是文本或者好友推荐
        ...
    elif info_type in ("Attachment", "Video", "Picture", "Recording"):  # 如果发送的消息是附件、视频、图片、语音
        ...
    elif info_type == "Map":  # 如果消息为分享的位置信息
        x, y, location = re.search(
            '<location x="(.*?)" y="(.*?)".*label="(.*?)".*', msg["OriContent"]
        ).group(1, 2, 3)
        if location is None:
            info = f"纬度->{x.__str__()}, 经度->{y.__str__()}"  # 内容为详细的地址
        else:
            info = r"" + location
        msg_share_url = msg["Url"]
    elif info_type == "Sharing":  # 如果消息为分享的音乐或者文章，详细的内容为文章的标题或者是分享的名字
        info = msg["Text"]
        msg_share_url = msg["Url"]  # 记录分享的url

    face_bug = info

    # 每一条消息的唯一标识作为键，消息的具体信息作为值，也是一个字典
    local_dict[msgId] = {
        "info": info,
        "info_type": info_type,
        "name": name,
        "fromUser": fromUser,
        "dt": dt,
        "save_dt": time.time(),
        "msg_share_url": msg_share_url,
        "group_name": group_name,
    }

    # 自动删除130秒之前的消息，避免数据量太大后引起内存不足
    del_info = []
    for k in local_dict:
        if int(time.time()) - int(local_dict[k]["save_dt"]) > 130:
            del_info.append(k)
    if del_info:
        for i in del_info:
            local_dict.pop(i)


@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)  # 监听系统提示
def note_info(msg):
    if "撤回了一条消息" in msg["Text"]:  # 监听撤回了一条消息到好友撤回了一条消息
        to = "filehelper"
        content = msg["Content"]  # 获取系统消息中的Content结点值
        doc = minidom.parseString(content)  # Content值为xml，解析xml
        result = doc.getElementsByTagName("msgid")  # 取出msgid标签的值
        # msgId = re.search("\<msgid\>(.*?)\<\/msgid\>", msg["Content"]).group(1)
        msgId = result[0].childNodes[0].nodeValue  # 该msgId就是撤回的消息标识，通过它可以在字典中找到撤回的消息信息
        msg_type = local_dict[msgId]["info_type"]  # 从字典中取出对应消息标识的消息类型
        has_file = msg_type in type_dict  # 有文件的话也要将文件发送回去

        if len(msgId) < 11:
            itchat.send_file(face_bug, toUserName=to)
        else:
            text_info = local_dict[msgId]["info"]  # 取出消息标识对应的消息内容
            fromUser = local_dict[msgId]["fromUser"]  # 取出发送者
            dt = local_dict[msgId]["dt"]  # 取出发送时间
            group_name = local_dict[msgId]["group_name"]  # 群名称
            qun = f"[群组:] {group_name}\n"
            is_share = msg_type in ("Sharing", "Map")
            content = (
                f"撤回了分享: {text_info}"
                if is_share
                else f"{type_dict[msg_type] if has_file else f'撤回内容: {text_info}'}"
            )
            send_msg = (
                f"{qun if group_name else ''}[发送人]: {fromUser}\n发送时间: {dt}\n{content}"
            )
            if is_share:
                send_msg += f"\n链接是:{local_dict[msgId].get('msg_share_url')}"

            itchat.send(send_msg, to)  # 将提示消息发送给文件助手

            if has_file:
                if msg_type == "Card":
                    itchat.send(f"分享的名片信息: {text_info}", to)
                else:
                    recording_info = local_dict[msgId]["info"]
                    info_name = local_dict[msgId]["name"]  # 取出消息文件名
                    recording_info(temp + "/" + info_name)  # 保存
                    itchat.send_file(f"{temp}/{info_name}", toUserName=to)

            del local_dict[msgId]


itchat.run()
