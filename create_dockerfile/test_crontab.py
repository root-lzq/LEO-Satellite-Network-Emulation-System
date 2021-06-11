#!/usr/bin/python3.6

import os
import time

t1 = time.time()
t_start = (int(round(t1*1000)))


os.system('/usr/sbin/tc qdisc del dev eth0 root')
os.system('/usr/sbin/tc -b /mapping/b1.txt')


t2 = time.time()
t_end = (int(round(t2*1000)))


filename = "/time.txt"
with open(filename, 'a+') as file_object:
            file_object.write(str(t_end-t_start)+" ms"+"\n")

