#!/usr/bin/env python
from socket import *
import time

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)

   for i in range(1, 10000):
      s = socket(AF_INET, SOCK_STREAM)

      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
