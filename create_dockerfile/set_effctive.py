#!/usr/bin/python3.6

from multiprocessing import Pool
import os

def set(i):
    path ='docker exec -it b'+str(i)+' /bin/bash -c "chmod a+x /update_cronjob/update_cronjob.py && ./update_cronjob/update_cronjob.py"'
    os.system(path)


if __name__ == '__main__':
    list_order = []
    for i in range(1, 401):
        list_order.append(i)
    with Pool(40) as pool:
        pool.map(set, list_order)
