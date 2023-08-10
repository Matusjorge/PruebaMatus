import omronfins.finsudp as finsudp
from omronfins.finsudp import datadef
import time

#cycle_time=2
#while True:
fins = finsudp.FinsUDP(0 , 170)

ret = fins.open('192.168.10.36', 9600)
fins.set_destination(dst_net_addr=0, dst_node_num=36, dst_unit_addr=0)
ret , value1 =fins.read_mem_area(datadef.DM_WORD, 271,0,1, datadef.USHORT)


ret = fins.open('192.168.10.35', 9600)
fins.set_destination(dst_net_addr=0, dst_node_num=35, dst_unit_addr=0)
ret , value2 =fins.read_mem_area(datadef.DM_WORD, 270,0,1, datadef.USHORT)
 

ret = fins.open('192.168.10.34', 9600)
fins.set_destination(dst_net_addr=0, dst_node_num=34, dst_unit_addr=0)
ret , value3 =fins.read_mem_area(datadef.DM_WORD, 270,0,1, datadef.USHORT)


ret = fins.open('192.168.10.33', 9600)
fins.set_destination(dst_net_addr=0, dst_node_num=33, dst_unit_addr=0)
ret , value4 =fins.read_mem_area(datadef.DM_WORD, 270,0,1, datadef.USHORT)
 

ret = fins.open('192.168.10.32', 9600)
fins.set_destination(dst_net_addr=0, dst_node_num=32, dst_unit_addr=0)
ret , value5 =fins.read_mem_area(datadef.DM_WORD, 270,0,1, datadef.USHORT)
 

ret = fins.open('192.168.10.31', 9600)
fins.set_destination(dst_net_addr=0, dst_node_num=31, dst_unit_addr=0)
ret , value6 =fins.read_mem_area(datadef.DM_WORD, 270,0,1, datadef.USHORT)
 
#time.sleep(cycle_time)

