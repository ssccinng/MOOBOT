import requests
from selenium import webdriver
import time
import random


class moobot(object):
    msgnum = 0
    def dataload(self):
        self.headersout = {
            "Referer": "https://d1.web2.qq.com/cfproxy.html?v=20151105001&callback=1",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.headersqun = {
            "Referer": "https://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.headersin = {
            "Referer": "https://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.headersfri = {
            "Referer": "https://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.headersqunyou = {
            "Referer": "https://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1",
            "Content-Type": "utf-8",
        }
        self.headersfwebqq = {
            "Referer": "https://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1",
            "Content-Type": "utf-8",
        }
        self.urlin = "https://d1.web2.qq.com/channel/poll2"
        self.urlout = "https://d1.web2.qq.com/channel/send_qun_msg2"
        self.fwebqqurl = "https://s.web2.qq.com/api/getvfwebqq?clientid=53999199"
        self.urlqunyou = "https://s.web2.qq.com/api/get_group_info_ext2?gcode={}&vfwebqq={}&t=1542542725156"
        self.urlfri = "https://s.web2.qq.com/api/get_user_friends2"
        self.qunurl = "https://s.web2.qq.com/api/get_group_name_list_mask2"
        self.dataout = "r=%7B%22group_uin%22%3A{}%2C%22content%22%3A%22%5B%5C%22{}%5C%22%2C%5B%5C%22font%5C%22%2C%7B%5C%22name%5C%22%3A%5C%22%E5%AE%8B%E4%BD%93%5C%22%2C%5C%22size%5C%22%3A10%2C%5C%22style%5C%22%3A%5B0%2C0%2C0%5D%2C%5C%22color%5C%22%3A%5C%22000000%5C%22%7D%5D%5D%22%2C%22face%22%3A48%2C%22clientid%22%3A53999199%2C%22msg_id%22%3A97820001%2C%22psessionid%22%3A%228368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857%22%7D"
        self.datain = "r=%7B%22ptwebqq%22%3A%22%22%2C%22clientid%22%3A53999199%2C%22psessionid%22%3A%228368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857%22%2C%22key%22%3A%22%22%7D"
        self.datafri = "r=%7B%22vfwebqq%22%3A%2286efdf4e9604dd8119f908e238571dae6359f3eaed39000139eeac53bf24b62ae4f13d83346647e3%22%2C%22hash%22%3A%220005001300670007%22%7D"
        self.qundata = "r=%7B%22vfwebqq%22%3A%22{}%22%2C%22hash%22%3A%220005001300670007%22%7D"
    
    def __init__(self):
        self.dataload();
        self.headersin["Cookie"] = self.headersout["Cookie"] = self.headersqun["Cookie"] = self.headersqunyou["Cookie"] = self.headersfwebqq["Cookie"] = self.getcookies()
        self.vfwebqq = eval(requests.get(self.fwebqqurl, headers = self.headersfwebqq).text)["result"]["vfwebqq"]
        self.qundata = self.qundata.format(self.vfwebqq)
        self.ggdp = []
        self.dpzd = {}

    def getcookies(self):
        f = open("qqcookie")
        a = f.readline().replace("\n", "")
        print(a)
        f.close()
        self.headersin["Cookie"] = a
        qq = eval(requests.post(self.urlin, headers = self.headersin, data = self.datain).text)
        if qq["retmsg"] != "domain login error":
            return a
        UA = 'Mozilla/5.0 (Linux; Android 6.0; PRO 6 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043221 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D QQ/7.0.0.3135 NetType/WIFI WebP/0.3.0 Pixel/1080'
        mobileEmulation = {"userAgent": UA}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(
            'https://web2.qq.com/')
        time.sleep(20)

        cookie = driver.get_cookies()
        driver.quit()
        cookies = {}
        for val in cookie:
            cookies[val['name']] = val['value']
        cookies = ";".join([i + "=" + cookies[i] for i in cookies])
        return cookies

    
    def heartup(self):
        self.checkfollow()
        while True:
            a = requests.post(self.urlin, headers = self.headersin, data = self.datain)
            qqdata = eval(a.text)
            print(qqdata)

            if "errmsg" in qqdata.keys() and qqdata["errmsg"] == "error":
                self.headersin["Cookie"] = self.headersout["Cookie"] = self.headersqun["Cookie"] = self.headersqunyou["Cookie"] = self.headersfwebqq["Cookie"] = self.getcookies()
                continue
            qqdata = qqdata["result"][0]
            if len(qqdata["value"]["content"]) == 1: #图片
                continue
            qqmsg = qqdata["value"]["content"][1] #表情
            if type(qqmsg) == list:
                qqmsg = str(qqmsg)
            if "send_uin" not in qqdata["value"].keys(): #私人消息
                if qqdata["value"]["from_uin"] == qqnum:
                    print("cmd!")
                    tc = self.cmdrun(qqmsg)
                    if tc:
                        break
                continue
            if qqdata["value"]["send_uin"] == qqnum:
                print("cmd!")
                tc = self.cmdrun(qqmsg)
                if tc:
                    break
            self.msgsendid = qqdata["value"]["send_uin"]
            if self.msgsendid == qqnum:
                if qqmsg not in self.ggdp:
                    self.ggdp.append(qqmsg)
                continue
            if self.followflag:
                self.followmsg(qqdata, qqmsg)

    def followmsg(self, qqdata, qqmsg):
        
        qqgroupcode = qqdata["value"]["group_code"]
        if int(qqgroupcode) == int(self.quninid):
            yjgl = False
            self.msgnum += 1
            if not self.getbzdgp(qqmsg): #不值得跟屁
                return

            if self.nameid[self.msgsendid] in self.followlist or self.ALLFollow:
                self.ggdp.append(qqmsg)
                yjgl = True
            if not yjgl:
                if qqmsg in self.dpzd.keys():
                    self.dpzd[qqmsg] += 1
                else:
                    self.dpzd[qqmsg] = 1
                

                print("复读次数：", self.dpzd[qqmsg])
                
                if self.dpzd[qqmsg] >= 3:
                    self.ggdp.append(qqmsg)
                    yjgl = True
                else:
                    print("tiaole")

            qrnd = random.randint(0, 1) 
            rnd = random.randint(0, 200)
            print(rnd, qrnd)
            print("确认将要跟屁", yjgl)

            if ((self.getzdgp(qqmsg) and qrnd == 0) or yjgl) or rnd == 10:
                if not yjgl:
                    self.ggdp.append(qqmsg)
            else:
                return 
            print("准备复读！")
            if self.adduse:
                qqmsg = self.nameid[self.msgsendid] + ": " + qqmsg
            while qqmsg[0] == "!" or qqmsg[0] == "！":
                del qqmsg[0]
            qqmsg = str(qqmsg.encode("utf-8")).replace("\\x", "%")
            qqmsg = qqmsg[2:-1]
            time.sleep(1.5)
            requests.post(self.urlout, data = self.dataout.format(self.qunoutid, qqmsg), headers = self.headersout)

    def cmdrun(self, msg):
        if msg[0] == "!" or msg[0] == "！":
            msg = msg[1:].split(" ")
            if msg[0].upper() == "STOP":
                print("停止！")
                self.followflag = False

            if msg[0].upper() == "START":
                print("启动！")
                self.followflag = True
            if msg[0].upper() == "EXIT":
                return True
            
            print("follow", len(msg) >= 2)
            name = " ".join(msg[1:])
            maxlen = 21
            while True:
                try:
                    name.encode("utf-8")[:maxlen].decode("utf-8")
                    break
                except:
                    maxlen -= 1
            name = name.encode("utf-8")[:maxlen].decode("utf-8")
            if len(msg) >= 2 and self.followflag:
                if msg[0].upper() == "ALL":
                    print("this")
                    if msg[1].upper() == "USEFOLLOW":
                        self.adduse = True
                        self.ALLFollow = True
                    if msg[1].upper() == "FOLLOW":
                        self.ALLFollow = True
                    if msg[1].upper() == "STOP":
                        self.adduse = self.ALLFollow = False
                    
                if msg[0].upper() == "FOLLOW":
                    if name in self.idname.keys():
                        self.followlist.append(name)
                        print("添加成功")

                if msg[0].upper() == "UNFOLLOW":
                    for i in range(len(self.followlist) - 1, 0 - 1,  -1):
                        if self.followlist[i] == name:
                            print("删除成功")
                            del self.followlist[i]
        return False

    def getqunid(self):
        self.qunid = eval(requests.post(self.qunurl, data = self.qundata, headers = self.headersqun).text)
        print("群id获取成功")
        self.qunid = self.qunid["result"]["gnamelist"]
        for i in self.qunid:
            if i["name"] == self.inqun:
                self.quninid = i["gid"]
                self.qunincode = i["code"]
            if i["name"] == self.outqun:
                self.qunoutid = i["gid"]
                self.qunoutcode = i["code"]
            if i["name"] == self.ceshiqun:
                self.ceshiqunid = i["gid"]
                self.ceshiquncode = i["code"]

    def start(self, inqun, outqun):
        self.inqun = inqun
        self.outqun = outqun
        self.followflag = False
        self.followlist = []
        self.ALLFollow = False
        self.adduse = False
        self.msgnum = 0
        self.getqunid()
        self.getqunyouid()
        self.heartup()


    def getqunyouid(self):
        frienduin = eval(requests.get(self.urlqunyou.format(self.qunincode, self.vfwebqq), headers = self.headersqunyou).text)
        qunyouin = frienduin["result"]["minfo"]
        self.nameid = {}
        self.idname = {}
        for qq in qunyouin:
            self.nameid[int(qq["uin"])] = qq["nick"]
            self.idname[qq["nick"]] = int(qq["uin"])
        qunyouin = frienduin["result"]["cards"]
        for qq in qunyouin:
            self.nameid[int(qq["muin"])] = qq["card"]
            self.idname[qq["card"]] = int(qq["muin"])

        

    def checkfollow(self):
        if self.msgnum > 20:
            self.dpzd = {}
            self.msgnum = 0

    def getzdgp(self, text):
        if len(text) > 25:
            print("zdgp ccc")    
            return True and random.randint(0, 2) == 0
        if ("牛逼" in text or 'nb' in text) and random.randint(0, 2) == 0:
            print("zdgp nb")    
            return True
        if "。。。" in text or '...' in text:
            print("zdgp ...")    
            return True
        if "⊙▽⊙" in text:
            print("zdgp ldz")
            return True
        if "嘤嘤嘤" in text:
            print("zdgp yyy")
            return True
        if "唱歌" in text or ".jpg" in text:
            print("zdgp jpg")
            return True
        return False 



    def getbzdgp(self, text):
        self.ggdp
        if len(self.ggdp) > 20:
            self.ggdp = self.ggdp[10:]
        if text in self.ggdp:
            return False
        if "破解" in text or "魔法" in text or "膜法" in text:
            return False 
        return True


fdindex = 0

yf = moobot()

while True:
    qqnum = input("请输入使用者qq号")
    INQ = input("输入群：")
    OUTQ = input("输出群：")
    yf.start(INQ, OUTQ)
