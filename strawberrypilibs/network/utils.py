import socket
import fcntl
import struct


class Utils:
    """A simple example class"""
    ip = "127.0.0.1"

    def __init__(self):
        self.ip = "127.0.0.1"

    def get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
          s.fileno(),
          0x8915,  # SIOCGIFADDR
          struct.pack('256s', ifname[:15])
        )[20:24])

    def f(self):
        return 'hello world'
