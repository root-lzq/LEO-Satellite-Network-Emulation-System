#!/usr/bin/python3.6

from datetime import datetime
import os
from multiprocessing import Process

dt=datetime.now()

#设定仿真开始时间 h:m
h = 16
m = 39

#设定仿真时间/min

set_time = 2 

pre_cronjob = "tc -b /bdl_file/"

filename = "/etc/cron.d/cronjob"
with open(filename, 'w+') as file_object:
     for i in range(11, 11+set_time):
            s = str(m)+" "+str(h)+" * * * /usr/sbin/tc qdisc del dev eth0 root && /usr/sbin/tc -b /bdl_file/"+str(i)+".txt || /usr/sbin/tc -b /bdl_file/"+str(i)+".txt"
            m = m+1
            if m == 60:
                m = 0
                h = h+1
                if h == 24: 
                    h = 0
            file_object.write(s+"\n")
     file_object.write(" \n")

os.system('crontab /etc/cron.d/cronjob')
