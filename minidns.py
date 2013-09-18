#!/usr/bin/env python
# -*-encoding:utf8 -*-

import os
import sys
import socket
import fcntl
import struct
import re
from optparse import OptionParser

# DNSQuery class from http://code.activestate.com/recipes/491264-mini-fake-dns-server/
class DNSQuery:
  def __init__(self, data):
    self.data=data
    self.domain=''

    tipo = (ord(data[2]) >> 3) & 15   # Opcode bits
    if tipo == 0:                     # Standard query
      ini=12
      lon=ord(data[ini])
      while lon != 0:
        self.domain+=data[ini+1:ini+lon+1]+'.'
        ini+=lon+1
        lon=ord(data[ini])

  def respuesta(self, ip):
    packet=''
    if self.domain:
      packet+=self.data[:2] + "\x81\x80"
      packet+=self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'   # Questions and Answers Counts
      packet+=self.data[12:]                                         # Original Domain Name Question
      packet+='\xc0\x0c'                                             # Pointer to domain name
      packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'             # Response type, ttl and resource data length -> 4 bytes
      packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) # 4bytes of IP
    return packet



# get_ip_address code from http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/
def get_ip_address(ifname):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  try:
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
  except:
    return None

def gethost(name = '', iface = ''):
  try:
    ip = socket.gethostbyname(name)
  except:
    ip = get_ip_address(iface)
  return ip


if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-i", "--interface", dest="iface", type="string", default="eth0", help=u"指定本地网络接口")
  parser.add_option("-p", "--ip", dest="ip", type="string", default="", help=u"默认返回IP")
  parser.add_option("-f", "--file", dest="dnsfile", type="string", help=u"指定DNS文件", default='')
  (options, args) = parser.parse_args()
  ip = options.ip
  iface = options.iface
  dnsfile = options.dnsfile
  if not ip:
    ip = get_ip_address(iface)

  try:
    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udps.bind(('',53))
  except Exception, e:
    print "Failed to create socket on UDP port 53:", e
    sys.exit(1)

  print 'miniDNS starting\n'

  dns_table = {}
  if options.dnsfile:
    with open(options.dnsfile) as dnsfile:
      dns_lines = dnsfile.readlines()
      dns_lines = [i.split() for i in dns_lines]
      for line in dns_lines:
        dns_table[line[0]] = line[1]

  reg_pattern = re.compile('\W')
  try:
    while 1:
      data, addr = udps.recvfrom(1024)
      p=DNSQuery(data)
      name - p.domain.strip('.')
      resolved_ip = dns_table.get(name) or gethost(name=name, iface=iface) or ip
      udps.sendto(p.respuesta(resolved_ip), addr)
      print 'Request: %s -> %s' % (p.domain.strip('.'), resolved_ip)
  except KeyboardInterrupt:
    print '\nBye!'
    udps.close()
