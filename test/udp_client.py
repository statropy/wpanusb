 #!/usr/bin/env python
"""UDP client echo"""

import socket
import time
import os

ADDR = '2001:db8::1'
PORT = 4242

def main():
    """send udp packet and compare response"""

    scope_id = socket.if_nametoindex('lowpan0')
    while True:
        with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, 0) as sock:
            msg = bytearray(os.urandom(5))
            sock.settimeout(5)
            sock.sendto(msg, (ADDR, PORT, 0, scope_id))
            print('data sent')
            rx_msg, server = sock.recvfrom(len(msg))
            if bytearray(rx_msg) == msg:
                print('echoed', len(rx_msg), 'bytes from', str(server))
            else:
                print('mismatch', msg, rx_msg)
        time.sleep(5)

if __name__ == '__main__':
    main()

