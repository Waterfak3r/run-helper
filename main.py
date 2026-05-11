import gzip
import hashlib
import json
import os
import time
import threading

import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock


SERVER = "http://222.28.94.116:8030/DragonFlyServ"


def get_cjk_font():
    if platform != "android":
        return None

    android_font_candidates = [
        "/system/fonts/NotoSansCJK-Regular.ttc",
        "/system/fonts/NotoSansSC-Regular.otf",
        "/system/fonts/SourceHanSansSC-Regular.otf",
        "/system/fonts/DroidSansFallback.ttf",
    ]
    for font_path in android_font_candidates:
        if os.path.exists(font_path):
            return font_path
    return None


APP_FONT = get_cjk_font()


def loggin(stuno, password, school):
    url = f"{SERVER}/DflyServer"
    data1 = {
        "name": f"['bangding', '{school}', 'student', '{stuno}', '{password}']"
    }
    text = requests.post(url, data=data1).text
    data2 = {
        "name": f"['bangdingschool_local','{school}','{stuno}','{password}','HarmonyOS','{stuno}','android','16']"
    }
    text = requests.post(url, data=data2).text
    index = text.find(",")
    if index != -1:
        return text[index + 1:]
    return None


def getinfo(stuno, uid, school):
    url = f"{SERVER}/Api/webserver/getRunDataSummary"
    data = {
        "studentno": stuno,
        "uid": uid,
        "schoolno": str(school),
    }
    json_str = json.dumps(data, separators=(",", ":"))
    gzip_body = gzip.compress(json_str.encode("utf-8"))
    return requests.post(url, data=gzip_body).text


def upload(studentno, school, uid, distance, speed, time2):
    url = f"{SERVER}/Api/webserver/uploadRunData"
    location = (
        "39.994356828667904,116.34414544058843;null;null;null;null;null@"
        "39.994356828667904,116.34414544058843;null;null;null;null;null@"
        "39.994356828667904,116.34414544058843;null;null;null;null;null@"
        "39.99476385634223,116.34501579370607;null;null;null;null;null@"
        "39.99476385634223,116.34501579370607;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99481751485721,116.34514752679799;null;null;null;null;null@"
        "39.99481751485721,116.34514752679799;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99483320648258,116.3452390244922;null;null;null;null;null@"
        "39.99483320648258,116.3452390244922;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99483096006103,116.34527846285137;null;null;null;null;null@"
        "39.99483096006103,116.34527846285137;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99483442062206,116.34532152004854;null;null;null;null;null@"
        "39.99483442062206,116.34532152004854;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994838407888416,116.34536816535535;null;null;null;null;null@"
        "39.994838407888416,116.34536816535535;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99484619092624,116.34541782789778;null;null;null;null;null@"
        "39.99484619092624,116.34541782789778;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99484416368115,116.3454675693533;null;null;null;null;null@"
        "39.99484416368115,116.3454675693533;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994843052881095,116.34551539660268;null;null;null;null;null@"
        "39.994843052881095,116.34551539660268;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99484372866054,116.34556672190712;null;null;null;null;null@"
        "39.99484372866054,116.34556672190712;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99484355922257,116.34561528087055;null;null;null;null;null@"
        "39.99484355922257,116.34561528087055;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99484709655535,116.34566203623227;null;null;null;null;null@"
        "39.99484709655535,116.34566203623227;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994847552768036,116.3457082700126;null;null;null;null;null@"
        "39.994847552768036,116.3457082700126;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99485277503328,116.34575228940749;null;null;null;null;null@"
        "39.99485277503328,116.34575228940749;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994860530263196,116.34579785256456;null;null;null;null;null@"
        "39.994860530263196,116.34579785256456;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994863898950015,116.34584537954859;null;null;null;null;null@"
        "39.994863898950015,116.34584537954859;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994872804413816,116.34589106307764;null;null;null;null;null@"
        "39.994872804413816,116.34589106307764;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994873815910275,116.34594017326606;null;null;null;null;null@"
        "39.994873815910275,116.34594017326606;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99487326091955,116.34598584552943;null;null;null;null;null@"
        "39.99487326091955,116.34598584552943;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99487450434356,116.34603063602343;null;null;null;null;null@"
        "39.99487450434356,116.34603063602343;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99487752629038,116.3460799769116;null;null;null;null;null@"
        "39.99487752629038,116.3460799769116;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99487437232527,116.34612629021514;null;null;null;null;null@"
        "39.99487437232527,116.34612629021514;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99486805082587,116.34616863421067;null;null;null;null;null@"
        "39.99486805082587,116.34616863421067;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994848738999686,116.34620572478765;null;null;null;null;null@"
        "39.994848738999686,116.34620572478765;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99482183908433,116.34623326301521;null;null;null;null;null@"
        "39.99482183908433,116.34623326301521;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.994799487266924,116.3462811974435;null;null;null;null;null@"
        "39.994799487266924,116.3462811974435;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.9947729840202,116.34631770576436;null;null;null;null;null@"
        "39.9947729840202,116.34631770576436;null;null;null;null;null@"
        "39.99436484405375,116.34415345970578;null;null;null;null;null@"
        "39.99474375995455,116.34633769678486;null;null;null;null;null@"
        "39.99474375995455,116.34633769678486;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99472575598313,116.3463736348829;null;null;null;null;null@"
        "39.99472575598313,116.3463736348829;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99472166350545,116.34642622194944;null;null;null;null;null@"
        "39.99472166350545,116.34642622194944;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99471249413889,116.34648061237492;null;null;null;null;null@"
        "39.99471249413889,116.34648061237492;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99469535710828,116.34653645500585;null;null;null;null;null@"
        "39.99469535710828,116.34653645500585;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99467572694869,116.34659068368202;null;null;null;null;null@"
        "39.99467572694869,116.34659068368202;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99464689999741,116.3466414734829;null;null;null;null;null@"
        "39.99464689999741,116.3466414734829;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99460818170494,116.3466702127678;null;null;null;null;null@"
        "39.99460818170494,116.3466702127678;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99458125508644,116.34669420293088;null;null;null;null;null@"
        "39.99458125508644,116.34669420293088;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.9945521617362,116.34672000686278;null;null;null;null;null@"
        "39.9945521617362,116.34672000686278;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.994552935665496,116.34676524794901;null;null;null;null;null@"
        "39.994552935665496,116.34676524794901;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99455580168751,116.34681158171522;null;null;null;null;null@"
        "39.99455580168751,116.34681158171522;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99455261233865,116.34686056059277;null;null;null;null;null@"
        "39.99455261233865,116.34686056059277;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99455261604336,116.34690573135356;null;null;null;null;null@"
        "39.99455261604336,116.34690573135356;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99455068801329,116.34695001987977;null;null;null;null;null@"
        "39.99455068801329,116.34695001987977;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99454854203349,116.34699543085857;null;null;null;null;null@"
        "39.99454854203349,116.34699543085857;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99454489164844,116.34704390845869;null;null;null;null;null@"
        "39.99454489164844,116.34704390845869;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99453977666975,116.34709535245663;null;null;null;null;null@"
        "39.99453977666975,116.34709535245663;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.9945373809213,116.34715173777545;null;null;null;null;null@"
        "39.9945373809213,116.34715173777545;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99453247765705,116.34720413385658;null;null;null;null;null@"
        "39.99453247765705,116.34720413385658;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.9945260317708,116.34724975462616;null;null;null;null;null@"
        "39.9945260317708,116.34724975462616;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.994526422758476,116.34729354215541;null;null;null;null;null@"
        "39.994526422758476,116.34729354215541;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99452776139491,116.34733604692742;null;null;null;null;null@"
        "39.99452776139491,116.34733604692742;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99452293105123,116.34737925245729;null;null;null;null;null@"
        "39.99452293105123,116.34737925245729;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99451403870367,116.34742147526546;null;null;null;null;null@"
        "39.99451403870367,116.34742147526546;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99449754089914,116.34743927276674;null;null;null;null;null@"
        "39.99449754089914,116.34743927276674;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99447246703212,116.3474485702751;null;null;null;null;null@"
        "39.99447246703212,116.3474485702751;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99445905452672,116.3474475162346;null;null;null;null;null@"
        "39.99445905452672,116.3474475162346;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99443870495584,116.34743738111868;null;null;null;null;null@"
        "39.99443870495584,116.34743738111868;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99441456883538,116.34743461190688;null;null;null;null;null@"
        "39.99441456883538,116.34743461190688;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99438651884779,116.34742983774038;null;null;null;null;null@"
        "39.99438651884779,116.34742983774038;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99436512743435,116.34742955440494;null;null;null;null;null@"
        "39.99436512743435,116.34742955440494;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.994363200312286,116.34744739384035;null;null;null;null;null@"
        "39.994363200312286,116.34744739384035;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.9943879042641,116.34746521660279;null;null;null;null;null@"
        "39.9943879042641,116.34746521660279;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.994400259291716,116.34747848767802;null;null;null;null;null@"
        "39.994400259291716,116.34747848767802;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99439965306128,116.34748054217003;null;null;null;null;null@"
        "39.99439965306128,116.34748054217003;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99439945388597,116.3474809931477;null;null;null;null;null@"
        "39.99439945388597,116.3474809931477;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99439986434742,116.34748123373461;null;null;null;null;null@"
        "39.99439986434742,116.34748123373461;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99440661896174,116.34748357980583;null;null;null;null;null@"
        "39.99440661896174,116.34748357980583;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.994467499192474,116.34752565104857;null;null;null;null;null@"
        "39.994467499192474,116.34752565104857;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.994508149645235,116.34754664285599;null;null;null;null;null@"
        "39.994508149645235,116.34754664285599;null;null;null;null;null@"
        "39.994548564575254,116.34754840187736;null;null;null;null;null@"
        "39.994548564575254,116.34754840187736;null;null;null;null;null@"
        "39.99453950244101,116.34755828269515;null;null;null;null;null@"
        "39.99453950244101,116.34755828269515;null;null;null;null;null@"
        "39.99475375355544,116.34623719320241;null;null;null;null;null@"
        "39.99453956283211,116.34755849317064;null;null;null;null;null@"
        "39.99453956283211,116.34755849317064;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.9945379638939,116.3475591043269;null;null;null;null;null@"
        "39.9945379638939,116.3475591043269;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994558206832174,116.34756023941006;null;null;null;null;null@"
        "39.994558206832174,116.34756023941006;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994567503652,116.34756914037035;null;null;null;null;null@"
        "39.994567503652,116.34756914037035;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994583939891065,116.34758298321624;null;null;null;null;null@"
        "39.994583939891065,116.34758298321624;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99460928877411,116.34760889400548;null;null;null;null;null@"
        "39.99460928877411,116.34760889400548;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99461565272435,116.34762714536679;null;null;null;null;null@"
        "39.99461565272435,116.34762714536679;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994614427574575,116.34762980111286;null;null;null;null;null@"
        "39.994614427574575,116.34762980111286;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99461409885554,116.34763050263003;null;null;null;null;null@"
        "39.99461409885554,116.34763050263003;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994614019185136,116.34763068302077;null;null;null;null;null@"
        "39.994614019185136,116.34763068302077;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99461524882315,116.34762504063897;null;null;null;null;null@"
        "39.99461524882315,116.34762504063897;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994615778879364,116.34760880462767;null;null;null;null;null@"
        "39.994615778879364,116.34760880462767;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99451572259767,116.347510162712;null;null;null;null;null@"
        "39.99451572259767,116.347510162712;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99448011884959,116.34748727732307;null;null;null;null;null@"
        "39.99448011884959,116.34748727732307;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99444476183224,116.3474572059778;null;null;null;null;null@"
        "39.99444476183224,116.3474572059778;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99440501011079,116.34746258290888;null;null;null;null;null@"
        "39.99440501011079,116.34746258290888;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99440950725695,116.34747176389519;null;null;null;null;null@"
        "39.99440950725695,116.34747176389519;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994411197457254,116.34747183426542;null;null;null;null;null@"
        "39.994411197457254,116.34747183426542;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99441255465254,116.34745404487437;null;null;null;null;null@"
        "39.99441255465254,116.34745404487437;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.9944157421605,116.34744179803896;null;null;null;null;null@"
        "39.9944157421605,116.34744179803896;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99441784232381,116.3474364263567;null;null;null;null;null@"
        "39.99441784232381,116.3474364263567;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99441212027274,116.34747333772557;null;null;null;null;null@"
        "39.99441212027274,116.34747333772557;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99440210298884,116.34752918062506;null;null;null;null;null@"
        "39.99440210298884,116.34752918062506;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994404360749606,116.3475441642202;null;null;null;null;null@"
        "39.994404360749606,116.3475441642202;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99440468648853,116.34754184911493;null;null;null;null;null@"
        "39.99440468648853,116.34754184911493;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.9944046661916,116.34754168875588;null;null;null;null;null@"
        "39.9944046661916,116.34754168875588;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443428675006,116.34755215576953;null;null;null;null;null@"
        "39.99443428675006,116.34755215576953;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443481712383,116.34755234626006;null;null;null;null;null@"
        "39.99443481712383,116.34755234626006;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.994434667006516,116.34755228610736;null;null;null;null;null@"
        "39.994434667006516,116.34755228610736;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443462698634,116.34755227608002;null;null;null;null;null@"
        "39.99443462698634,116.34755227608002;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99443461698593,116.34755227607874;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99445166769944,116.3475522782399;null;null;null;null;null@"
        "39.99445166769944,116.3475522782399;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99445765795012,116.34755227899916;null;null;null;null;null@"
        "39.99445765795012,116.34755227899916;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99445774795389,116.34755227901057;null;null;null;null;null@"
        "39.99445774795389,116.34755227901057;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99458921826156,116.34757114757795;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99445775795431,116.34755227901184;null;null;null;null;null@"
        "39.99458021233379,116.34756813975353;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.995998312382405,116.34620530206918;null;null;null;null;null@"
        "39.99598442437621,116.34629422483613;null;null;null;null;null@"
        "39.99598442437621,116.34629422483613;null;null;null;null;null@"
        "39.9959608145948,116.3464453933452;null;null;null;null;null@"
        "39.99594831521089,116.3465254236321;null;null;null;null;null@"
        "39.99594831521089,116.3465254236321;null;null;null;null;null@"
        "39.99592331625858,116.34668548399512;null;null;null;null;null@"
        "39.9959108166894,116.3467655140702;null;null;null;null;null@"
        "39.9959108166894,116.3467655140702;null;null;null;null;null@"
        "39.99584462410633,116.34690031151152;null;null;null;null;null@"
        "39.9957906930843,116.34697220766981;null;null;null;null;null@"
        "39.9957906930843,116.34697220766981;null;null;null;null;null@"
        "39.99577451376778,116.34699377650578;null;null;null;null;null@"
        "39.99577451376778,116.34699377650578;null;null;null;null;null@"
        "39.99564507906959,116.34716632700099;null;null;null;null;null@"
        "39.99563429283135,116.34718070619337;null;null;null;null;null@"
        "39.99563429283135,116.34718070619337;null;null;null;null;null@"
        "39.99549946467786,116.34736044589407;null;null;null;null;null@"
        "39.995488678411476,116.3473748250537;null;null;null;null;null@"
        "39.995488678411476,116.3473748250537;null;null;null;null;null@"
        "39.99535924305015,116.34754737477759;null;null;null;null;null@"
        "39.9953430636085,116.34756894346805;null;null;null;null;null@"
        "39.9953430636085,116.34756894346805;null;null;null;null;null@"
        "39.99521362790188,116.34774149278934;null;null;null;null;null@"
        "39.99520284157901,116.34775587188312;null;null;null;null;null@"
        "39.99520284157901,116.34775587188312;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;9;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.99467438021407,116.34960946714587;null;null;null;null;null@"
        "39.994630318803445,116.34946437477994;null;null;null;null;null@"
        "39.994630318803445,116.34946437477994;null;null;null;null;null@"
        "39.994630318803445,116.34946437477994;null;null;null;null;null@"
        "39.99458440901887,116.34929920271345;null;null;null;null;null@"
        "39.99458440901887,116.34929920271345;null;null;null;null;null@"
        "39.99458440901887,116.34929920271345;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.99457216758772,116.3475440852667;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;2;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994161997370206,116.34457576074398;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.994574165820865,116.34754308329204;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;3;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.996020000781144,116.34606115403744;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99459351580522,116.34753722271088;null;null;null;null;null@"
        "39.99459351580522,116.34753722271088;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99458458042768,116.34753992759397;null;null;null;null;null@"
        "39.99458458042768,116.34753992759397;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99456745942167,116.34753435303607;null;null;null;null;null@"
        "39.99456745942167,116.34753435303607;null;null;null;null;null@"
        "39.9945510402447,116.34750809257574;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.9945510402447,116.34750809257574;null;null;null;null;null@"
        "39.99455230865214,116.34752344687374;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99455230865214,116.34752344687374;null;null;null;null;null@"
        "39.99454924759244,116.34752835740375;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99454924759244,116.34752835740375;null;null;null;null;null@"
        "39.99454854319533,116.34752599205605;null;null;null;null;null@"
        "39.99454854319533,116.34752599205605;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99454735979601,116.34752417787307;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99454735979601,116.34752417787307;null;null;null;null;null@"
        "39.99454738399812,116.34752645293406;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.99454738399812,116.34752645293406;null;null;null;null;null@"
        "39.9945464484376,116.34752887820758;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.9945464484376,116.34752887820758;null;null;null;null;null@"
        "39.99454640854698,116.34752893833621;null;null;null;null;null@"
        "39.99454640854698,116.34752893833621;null;null;null;null;null@"
        "39.99482226344568,116.34646595146454;null;null;null;null;null@"
        "39.994544149513565,116.3475240972879;null;null;null;null;null@"
        "39.994544149513565,116.3475240972879;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "39.994549972107706,116.34752537085569;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "39.994549972107706,116.34752537085569;null;null;null;null;null@"
        "39.99453145029968,116.34750314910673;null;null;null;null;null@"
        "39.99453145029968,116.34750314910673;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "39.99452300904416,116.34749724491117;null;null;null;null;null@"
        "39.99452300904416,116.34749724491117;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "39.994518366957124,116.3475016340835;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "39.994518366957124,116.3475016340835;null;null;null;null;null@"
        "39.994521037411204,116.34749099075518;null;null;null;null;null@"
        "39.994521037411204,116.34749099075518;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "39.99452289943693,116.34748663129677;null;null;null;null;null@"
        "39.99452289943693,116.34748663129677;null;null;null;null;null@"
        "39.994576141845926,116.34753005457807;null;null;null;null;null@"
        "888,888;1758339401;null;null;null;null"
    )
    data = {
        "begintime": str(int(time.time()) - time2),
        "endtime": str(int(time.time())),
        "uid": uid,
        "schoolno": str(school),
        "distance": distance,
        "speed": speed,
        "studentno": studentno,
        "atttype": "3",
        "eventno": "802",
        "location": location,
        "pointstatus": "1",
        "usetime": str(time2),
        "path": "39.994130,116.350146;39.994704,116.344357;39.994111,116.348289;39.994813,116.346307;",
        "ruleid": "3",
    }
    json_str = json.dumps(data, separators=(",", ":"))
    gzip_body = gzip.compress(json_str.encode("utf-8"))
    return requests.post(url, data=gzip_body).text


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=14, **kwargs)

        font_kwargs = {"font_name": APP_FONT} if APP_FONT else {}
        self.upload_defaults = {
            "school": "10032",
            "distance": "2000.0",
            "speed": "3.3",
            "time2": 606,
        }

        self.add_widget(Label(
            text="[b]跑步数据上传助手[/b]",
            markup=True,
            size_hint=(1, None),
            height=56,
            font_size="20sp",
            **font_kwargs,
        ))

        self.add_widget(Label(
            text="请输入学号",
            size_hint=(1, None),
            height=32,
            halign="left",
            valign="middle",
            **font_kwargs,
        ))

        reminder = Label(
            text="每次上传按 2km 处理，每日限制 4km。",
            size_hint=(1, None),
            height=52,
            halign="left",
            valign="middle",
            color=(0.35, 0.35, 0.35, 1),
            **font_kwargs,
        )
        reminder.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        self.add_widget(reminder)

        self.stuno_input = TextInput(
            text="",
            hint_text="请输入学号",
            multiline=False,
            size_hint=(1, None),
            height=108,
            font_size="32sp",
            padding=[16, 20, 16, 20],
            **font_kwargs,
        )
        self.add_widget(self.stuno_input)

        self.start_btn = Button(
            text="开始上传",
            size_hint=(1, None),
            height=58,
            font_size="18sp",
            background_color=(0.2, 0.6, 0.8, 1),
            **font_kwargs,
        )
        self.start_btn.bind(on_press=self.do_upload)
        self.add_widget(self.start_btn)
        self.add_widget(Label(size_hint=(1, 1)))

        Clock.schedule_once(lambda dt: self.show_disclaimer(font_kwargs), 0)

    def show_disclaimer(self, font_kwargs):
        content = BoxLayout(orientation="vertical", spacing=12, padding=16)
        header = Label(
            text="[b]免责声明[/b]",
            markup=True,
            size_hint=(1, None),
            height=40,
            halign="center",
            valign="middle",
            **font_kwargs,
        )
        header.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        content.add_widget(header)

        scroll = ScrollView(size_hint=(1, 1))
        message = Label(
            text=(
                "[b]本APP只作为技术学习和验证使用，其余人运用本APP所做的任何行为与本人无关。[/b]\n\n"
                "[b]1. 技术研究定位[/b]\n"
                "本项目所有代码、文档及相关内容，仅用于技术交流与学习，"
                "旨在帮助开发者理解校园跑类应用的技术逻辑，严禁将项目相关技术或"
                "衍生成果用于上传校园跑实际成绩、规避正常运动要求等违规行为。\n\n"
                "[b]2. 健康与合规提示[/b]\n"
                "[b]实际运动优先：[/b]校园跑的核心目的是促进学生身心健康，规律的户外跑步"
                "能有效提升体能、改善精神状态，远优于任何技术手段的“模拟”。"
                "我们强烈建议所有使用者遵循学校规定，通过真实运动完成校园跑任务。\n\n"
                "[b]风险自行承担：[/b]若任何个人或团体违反学校规定，使用本项目相关技术进行"
                "校园跑作弊，导致被学校通报批评、成绩作废、纪律处分等后果，均与本项目"
                "作者及贡献者无关，所有责任由违规使用者自行承担。"
            ),
            markup=True,
            halign="left",
            valign="top",
            size_hint_y=None,
            **font_kwargs,
        )
        message.bind(
            size=lambda instance, value: setattr(instance, "text_size", value),
            texture_size=self._update_disclaimer_height,
        )
        scroll.add_widget(message)
        content.add_widget(scroll)

        button_row = BoxLayout(size_hint=(1, None), height=52, spacing=10)
        agree_btn = Button(text="同意", **font_kwargs)
        exit_btn = Button(text="退出", **font_kwargs)
        button_row.add_widget(agree_btn)
        button_row.add_widget(exit_btn)
        content.add_widget(button_row)

        popup = Popup(
            title="",
            content=content,
            size_hint=(0.92, 0.9),
            auto_dismiss=False,
        )

        agree_btn.bind(on_press=popup.dismiss)
        exit_btn.bind(on_press=lambda instance: self.exit_app())
        popup.open()

    def _update_disclaimer_height(self, instance, value):
        instance.height = max(value[1], 240)

    def show_status_popup(self, title, message):
        font_kwargs = {"font_name": APP_FONT} if APP_FONT else {}
        content = BoxLayout(orientation="vertical", spacing=12, padding=16)
        body = Label(
            text=message,
            halign="left",
            valign="middle",
            **font_kwargs,
        )
        body.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        content.add_widget(body)

        close_btn = Button(
            text="确定",
            size_hint=(1, None),
            height=48,
            **font_kwargs,
        )
        content.add_widget(close_btn)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.84, None),
            height=660,
            auto_dismiss=True,
        )
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

    def do_upload(self, instance):
        stuno = self.stuno_input.text.strip()
        school = self.upload_defaults["school"]
        distance = self.upload_defaults["distance"]
        speed = self.upload_defaults["speed"]
        time2 = self.upload_defaults["time2"]

        if not stuno:
            self.show_status_popup("提示", "请输入学号后再开始上传。")
            return

        self.start_btn.disabled = True
        self.start_btn.text = "运行中..."

        def run():
            try:
                password = hashlib.md5(stuno.encode()).hexdigest()
                uid = loggin(stuno, password, school)
                if not uid:
                    self._show_status("提示", "登录失败，请检查学号后重试。")
                    self._finish()
                    return

                getinfo(stuno, uid, school)

                result = upload(stuno, school, uid, distance, speed, time2)
                info = getinfo(stuno, uid, school)
                self._show_status("上传结果", f"上传成功。\n\n返回结果：{result}\n\n刷新结果：{info}")
            except Exception as e:
                self._show_status("异常", str(e))
            finally:
                self._finish()

        threading.Thread(target=run, daemon=True).start()

    def _show_status(self, title, message):
        Clock.schedule_once(lambda dt: self.show_status_popup(title, message), 0)

    def _finish(self):
        def reset():
            self.start_btn.disabled = False
            self.start_btn.text = "开始上传"
        Clock.schedule_once(lambda dt: reset(), 0)

    def exit_app(self):
        app = App.get_running_app()
        if app:
            app.stop()
        Window.close()


class FuckHQTApp(App):
    def build(self):
        self.title = "跑步数据上传助手"
        return MainLayout()


if __name__ == "__main__":
    FuckHQTApp().run()
