__author__ = 'paulie'
import socket
import fcntl
import struct
import sys

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# check for unique ip in eth0
try:
    possible_ip = str(get_ip_address("eth0"))
    if possible_ip == "127.0.0.1":
        pass
    else:
        print possible_ip
        sys.exit()
except IOError:
    pass

# check for unique ip in lo
try:
    possible_ip = str(get_ip_address("lo"))
    if possible_ip == "127.0.0.1":
        pass
    else:
        print possible_ip
        sys.exit()
except IOError:
    pass

# check for unique ip in wlan0
try:
    possible_ip = str(get_ip_address("wlan0"))
    if possible_ip == "127.0.0.1":
        pass
    else:
        print possible_ip
        sys.exit()
except IOError:
    print "couldn't find a unique ip..."