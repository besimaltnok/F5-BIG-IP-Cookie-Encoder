#!/usr/bin/env python

import sys

def IPEncode(ipl):
	global a
	a = '0x'
	for i in ipl:
		if int(i) < 16 :
			a = a + '0'
			a = a + hex(int(i)).split('x')[1]
		else:
			a = a + hex(int(i)).split('x')[1]

def PortEncode(port):
	global port_r
	port_r = ''
	port = hex(int(port)).split('x')[1]
	port_r = port[2:]
	port_r = port_r + port[0:2]

if __name__ == "__main__":
	ip   = sys.argv[1]
	port = int(sys.argv[2])
	ipl  = ip.split('.')
	ipl.reverse()
	IPEncode(ipl)
	PortEncode(port)

encode_data = str(int(a,16)) + '.' + str(int(port_r,16)) + '.' + '0000'
print "Encode IP   : ", ip
print "Encode Port : ",port
print "Encode Data : ",encode_data
