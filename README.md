The git contains two folders *server1* and *server2*. *server1* and *server2* respectively contain 5 files *set_vxlan, vxlan_create_docker, vxlan_link, vxlan_flow_table and flow_table*.  
* *set_vxlan* : build vxlan based on ovs.  
* *vxlan_create_docker* : create a specified number of containers and connect them to ovs.
* *vxlan_link* : realize the flow table configuration of ovs in **multi-process mode**.
* *vxlan_flow_table* :  realize the flow table configuration of ovs with ***flow_table***.
* *flow_table* : a text file that contains zero or more flows in the same syntax, one per line.
