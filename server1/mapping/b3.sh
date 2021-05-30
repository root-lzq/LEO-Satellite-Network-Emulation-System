#!/bin/bash
 tc qdisc del dev eth0 root
 tc qdisc add dev eth0 handle 1: root htb
 tc class add dev eth0 parent 1: classid 1:1 htb rate 10mbit ceil 10mbit
 tc qdisc add dev eth0 parent 1:1 handle 10: netem delay 3ms
 tc filter add dev eth0 protocol ip parent 1:0 u32 match ip dst 10.0.0.3 flowid 1:1
 tc class add dev eth0 parent 1: classid 1:2 htb rate 10mbit ceil 10mbit
 tc qdisc add dev eth0 parent 1:2 handle 20: netem delay 3ms
 tc filter add dev eth0 protocol ip parent 1:0 u32 match ip dst 10.0.0.5 flowid 1:2
 tc class add dev eth0 parent 1: classid 1:3 htb rate 10mbit ceil 10mbit
 tc qdisc add dev eth0 parent 1:3 handle 30: netem delay 5ms
 tc filter add dev eth0 protocol ip parent 1:0 u32 match ip dst 10.0.0.54 flowid 1:3
 tc class add dev eth0 parent 1: classid 1:4 htb rate 10mbit ceil 10mbit
 tc qdisc add dev eth0 parent 1:4 handle 40: netem delay 4ms
 tc filter add dev eth0 protocol ip parent 1:0 u32 match ip dst 10.0.6.30 flowid 1:4
