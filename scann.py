#!/usr/bin/env python3
#coding:utf-8



import time
import re
import requests
import socket
import traceback
import threading
import sys
import selenium
import argparse
from queue import Queue
# from multiprocessing import Process
# from multiprocessing import Queue as Qu
from awvs_api import awvs
from search import Exploit_Search
from main import Libs
from search import selenium_
from lib import get_headers
from lib import info
from lib import error
from lib import warning
from lib import loads
from lib import AttribDict
from lib import print_
from lib import root


foo = AttribDict()
headers = get_headers()
libs = Libs()
selenium_ = selenium_()
event = threading.Event
port_scan_results = []
threadLock = threading.Lock()
browser = selenium.webdriver.Chrome()
commands_ = libs.commands_
commands__ = libs.commands__
get_page_num = selenium_.Get_Page_num


# KeyboardInterrupt


# commands
cmd1 = "xfce4-terminal -e {}"
cmd2 = "nmap -Pn {} -oX {}lib/nmap_xml/{}"
cmd3 = "python3 {}subdns/subdns.py -u {} -d mini_names.txt"



# dns 查询接口
dns_query1 = "https://dns.bufferover.run/dns?q={}"




class Scann(object):

    def __init__(self,queue,domain):

        self.awvs = awvs
        self.option = True
        self.option_ = True
        self.browser = selenium_.browser
        self.browser_ = selenium_.browser_
        self.queue = queue
        self.domain = domain
        self.event = event()
        self.google_search = selenium_.Google_Search
    
    
    def add_task(self,target,rule):
        add = self.awvs(target=target,rule=rule)
        add.add_()

    def delete_(self):
        delete_ = self.awvs(target='',rule='')
        delete_.delete_()

    def delete(self):
        delete = self.awvs(target='',rule='')
        delete.delete()

    def Sqli_Scann(self):
        datas = self.domain
        
        if self.option_:

            print_("""
    1.删除所有任务.
    2.删除单个任务.
    3.跳过.
    0.Exit.
            """)
            ipt1 = input('>')
            if ipt1 is '1':
                self.delete_()
                ipt2 = input('显示细节[y/n]>')
                if ipt2 is 'y':
                    pass
                if ipt2 is 'n':
                    self.option = False
            if ipt1 is '2':
                self.delete()
                ipt2 = input('显示细节[y/n]>')
                if ipt2 is 'y':
                    pass
                if ipt2 is 'n':
                    self.option = False
            if ipt1 is '3':
                self.option_ = False
            
            eXit = False if not ipt1 is '0' else True


        def r():
            if eXit:
                exit(0)
            i = 1
            for target1 in datas:
                if i <= 5:
                    if self.option:
                        info(('Add scann target -> ',target1))
                    self.add_task(target=target1,rule='3')
                else:
                    i = 0
                    time.sleep(600)
                i += 1
        thread1 = threading.Thread(target=r)
        thread1.start()



    def CDN_Scann(self):
        pass


    def Subdomain_Enumeration(self,domain):
        commands__(cmd=cmd3.format(root,domain))



    def Collect_known_domain(self,domain):
        links = []
        number = get_page_num(keyword='site:{}'.format(domain))
        datas = self.google_search(keyword='site:{}'.format(domain),number=number)
        try:
            for data in datas:
                link = data[1]
                links.append(link)
        except Exception as e:
            # error(traceback.format_exc())
            pass

        for link in links:
            thread1 = threading.Thread(target=self.port_scan,args=(link,link))
            thread1.start()


    def DNS_Query_ZZ(self):
        """
        站长之家nslookup查询 http://tool.chinaz.com/nslookup/
        """
        pass

    def DNS_Query_ZZ_(self):
        """
        站长之家whois查询 http://whois.chinaz.com/
        """
        pass



    # def get_url(self,domain):
    #     d1 = domain.split('/')
    #     for d2 in d1:
    #         if \
    #         d2 != 'https' and \
    #         d2 != 'http' and \
    #         d2 != '/' and \
    #         d2 and \
    #         d2 != 'https:' and \
    #         d2 != 'https:/' and \
    #         d2 != 'http:' and \
    #         d2 != 'http:/':
    #             return d2.strip()



    def DNS_Query_Interface(self,domain):
        """
        DNS接口查询
        """
        # threadLock.acquire()
        #方法：add_cookie(cookie={'':'','':''})
        try:
            datas_d1 = []
            datas_d2 = []
            warning(('Query Domain -> '+domain))
            self.browser_.get(dns_query1.format(domain))
            time.sleep(7)
            htmldoc = self.browser_.find_element_by_xpath('/html/body/pre').text
            data = loads(htmldoc)
            # info(data['RDNS'])
            try:
                if 'FDNS_A' in data:
                    data1 = data['FDNS_A']
                    for data_1 in data1:
                        find1 = re.findall('\d',data_1)
                        if find1:
                            d1 = data_1.split(',')
                            ips = d1[0]
                            domains = d1[1]
                            datas_d1.append([ips,domains])

            except:
                pass
            
            try:
                if 'RDNS' in data:
                    data2 = data['RDNS']
                    for data_2 in data2:
                        find2 = re.findall('\d',data_2)
                        if find2:
                            d2 = data_2.split(',')
                            ips = d2[0]
                            domains = d2[1]
                            datas_d2.append([ips,domains])
            except:
                pass
            
            foo.Dns_Qery = [datas_d1,datas_d2]

            for d1 in foo.Dns_Qery[0]:
                ip = d1[0]
                if ip:
                    domain = d1[1]
                    thread1 = threading.Thread(target=self.port_scan,args=(ip,ip))
                    time.sleep(1)
                    thread1.start()
                    info('域名:{} -> 查询IP:{}'.format(domain,ip))

            for d1 in foo.Dns_Qery[1]:
                ip = d1[0]
                if ip:
                    domain = d1[1]
                    thread2 = threading.Thread(target=self.port_scan,args=(ip,ip))
                    time.sleep(1)
                    thread2.start()
                    info('域名:{} -> 查询IP:{}'.format(domain,ip))

            return True
            
        except Exception as e:
            error(traceback.format_exc())
            i = 0
            while True:
                if i == 3:
                    if self.DNS_Query_Interface(domain=domain):
                        break
                    i = 0
                i += 1
        
        # threadLock.release()
        

    def port_scan(self,domain,filename):
        """
        nmap scann
        """
        try:
            libs.commands_(cmd=[cmd2.format(domain,libs.root,filename)])
            time.sleep(10)
            data1 = libs.commands_(cmd=['python2 {}lib/nmap_xml.py {}lib/nmap_xml/{}'.format(libs.root,libs.root,filename)]).strip()
            # data1 = exec('data1 = '+data1)
            data1 = eval(data1)
            foo.nScan_Result = data1
            for i in range(0,2):
                for d1 in foo.nScan_Result[i]:
                    if 'ip' in d1 and \
                       'port' in d1 and \
                       'state' in d1 and \
                       'agreement' in d1:
                        
                        ip = d1.get('ip')
                        port = d1.get('port')
                        state = d1.get('state')
                        agreement = d1.get('agreement')
            
                        if ip:
                            if state != 'closed':
                                info(ip+':'+port+' /'+state+' '+'-'+agreement)
                                if port == '443' or port == '80':
                                    w = open('{}lib/nScan_Result.txt'.format(libs.root),'a+')
                                    w.write('{"ip":"%s","port":"%s","state":"%s","agreement":"%s"}' % (ip,port,state,agreement))
                                    w.write('\n')
                                    warning('写入 nScan_Result ...')
                                    w.close()
                        
                            else:
                                error(ip+':'+port+' /'+state+' '+'-'+agreement)
                    
        except Exception as e:
            # error(traceback.format_exc())
            pass
        
        
    def sub_domain(self):
        pass


    def jietu(self,domain):
        try:
            # self.browser_.set_page_load_timeout(5)
            browser.get(str(domain))
            browser.save_screenshot('lib/img/{}.png'.format(str(domain).replace('https://','').replace('http://','')))
            browser.quit()
            # self.browser_.close()
        except:
            error(traceback.format_exc())
            error('截图此：{}超时...'.format(domain))
            pass


    def main(self,domains=[],number=3):
        self.Sqli_Scann()
        i = 1        
        for domain in domains:
            time.sleep(1)
            if i == number:
                break

            self.DNS_Query_Interface(domain=domain)
            # self.Subdomain_Enumeration(domain=domain)
            self.Collect_known_domain(domain=domain)
            
            i += 1
        



    def run(self):
        self.main(self.domain)
        



def filter_domain(domain=[]):
    d1 = []
    for data1 in domain:
            if not re.findall('\.xls',data1) and \
                not re.findall('\.sql',data1) and \
                not re.findall('\.txt',data1) and \
                not re.findall('www.google.com',data1) and \
                not re.findall('www.baidu.com',data1) and \
                not re.findall('baidu.com',data1) and \
                not re.findall('google.com',data1) and \
                not re.findall('github.com',data1) and \
                not re.findall('cnblogs.com',data1) and \
                not re.findall('csdn.net',data1) and \
                not re.findall('exploit-db.com',data1):
                d1.append(data1)

    return d1


def get_target_sqli_url():
        d1 = []
        d2 = []
        libs = Libs()
        datas1 = libs.Read_text(filename='sqli1.txt')
        datas2 = libs.Read_text(filename='sqli2.txt')
        d1 = filter_domain(domain=datas1)
        d2 = filter_domain(domain=datas2)        

        return (d1,d2)



def get_url(domain):
    d1 = domain.split('/')
    for d2 in d1:
        if \
        d2 != 'https' and \
        d2 != 'http' and \
        d2 != '/' and \
        d2 and \
        d2 != 'https:' and \
        d2 != 'https:/' and \
        d2 != 'http:' and \
        d2 != 'http:/':
            return d2.strip()





def main():
    data = get_target_sqli_url()
    datas = []
    d1 = data[0] + data[1]
    for d2 in d1:
        datas.append(get_url(d2))
    d3 = list(set(datas))
    queue = Queue()
    scan1 = Scann(queue=queue,domain=d3)
    scan1.run()


    




if __name__ == "__main__":
    main()
    selenium_.browser.quit()
    selenium_.browser_.quit()




# queue = Queue()
# s = Scann(queue=queue,domain=['https://www.baidu.com','https://www.so.com'])

# # s.port_scan(domain='www.baidu.com',filename='baidu.xml')
# # info(foo.nScan_Result[0]['ip'])

# # s.DNS_Query_Interface(domain='baidu.com')
# # info(foo.Dns_Qery)

# s.Sqli_Scann()

# selenium_.browser.quit()
# selenium_.browser_.quit()
















# from queue import Queue
# from threading import Thread
# import time

# class Student(Thread):
#     def __init__(self, name, queue):
#         super().__init__()
#         self.name = name
#         self.queue = queue

#     def run(self):
#         while True:
#             # 阻塞程序，时刻监听老师，接收消息
#             msg = self.queue.get()
#             # 一旦发现点到自己名字，就赶紧答到
#             if msg == self.name:
#                 print("{}：到！".format(self.name))
            
#             if self.queue.empty():
#                 exit(0)



# class Teacher:
#     def __init__(self, queue):
#         self.queue=queue

#     def call(self, student_name):
#         print("老师：{}来了没？".format(student_name))
#         # 发送消息，要点谁的名
#         self.queue.put(student_name)


# queue = Queue()
# teacher = Teacher(queue=queue)
# s1 = Student(name="小明", queue=queue)
# s2 = Student(name="小亮", queue=queue)
# s1.start()
# s2.start()


# print('开始点名~')
# teacher.call('小明')
# time.sleep(1)
# teacher.call('小亮')










































# s = Scann()
# data = s.DNS_Query_Interface(domain='www.baidu.com')
# print(data)
# s.browser_.quit()
# s.browser.quit()

# s = Scann()
# result = s.port_scan(host=['www.baidu.com'],port=[80,443,333,222])
# print(result)
# s.browser.quit()
# s.browser_.quit()

# s = Scann()






































# class test(threading.Thread):

#     def __init__(self,queue):
#         super(test,self).__init__()
#         self.queue = queue

#     def t1(self):
#         self.queue.put('hello t1')
#         self.queue.put('hello t1_1')
#         self.queue.put([1,2,3,4,5])
#         self.queue.put({1:'1a',2:'2a'})
#         self.queue.put((11,22,33))
#         self.queue.put({'test1':1})
#         self.queue.put({'test1':2})


#     def t2(self):
#         while True:
#             time.sleep(1)
#             print('hello t2')

#     def t3(self):
#         while True:
#             time.sleep(1)
#             print('hello t3')


#     def run(self):
#         th1 = threading.Thread(target=self.t1)
#         th2 = threading.Thread(target=self.t2)
#         th3 = threading.Thread(target=self.t3)
        
#         # 并发执行
#         th1.start()
#         # 获取队列元素[1]
#         print(self.queue.get())
#         # 获取队列元素[2]
#         print(self.queue.get())
#         # 获取队列元素[3]
#         print(self.queue.get())
        
#         print(self.queue.get())
#         print(self.queue.get())
#         print(self.queue.get()['test1'])
#         print(self.queue.get()['test1'])


#         # th2.start()
#         # th3.start()
        
#         # 正常执行
#         # self.t1()
#         # self.t2()
#         # self.t3()




# queue = Queue()
# t = test(queue)
# t.start()
# selenium_.browser.quit()
# selenium_.browser_.quit()

# """
# result:
#     hello t1
#     hello t1_1
#     [1, 2, 3, 4, 5]
#     {1: '1a', 2: '2a'}
#     (11, 22, 33)

# """






