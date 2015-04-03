__author__ = 'paulie'
import socket
import fcntl
import struct
import sys

class NetworkToolbox:
    def __init__(self):
        pass

    def get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

    def get_host(self):
    # check for unique ip in eth0
        try:
            possible_ip = str(self.get_ip_address("eth0"))
            if possible_ip == "127.0.0.1":
                pass
            else:
                return possible_ip
        except IOError:
            pass

        # check for unique ip in lo
        try:
            possible_ip = str(self.get_ip_address("lo"))
            if possible_ip == "127.0.0.1":
                pass
            else:
                return possible_ip
        except IOError:
            pass

        # check for unique ip in wlan0
        try:
            possible_ip = str(self.get_ip_address("wlan0"))
            if possible_ip == "127.0.0.1":
                pass
            else:
                return possible_ip
        except IOError:
            print "couldn't find a unique ip..."