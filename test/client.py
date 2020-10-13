import socket
import time

#ADDR = 'fe80::a029:293c:9940:2162'
ADDR = '2001:db8::1'
#ADDR = 'localhost'
PORT = 2018

msg = b'It was the best of times it was the blurst of times'
def main():
    scope_id = socket.if_nametoindex('lowpan0')
    while True:
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0) as s:
            s.connect((ADDR, PORT, 0, scope_id))
            s.sendall(msg)
            print('data sent')
            num_rx = 0
            rx_msg = []
            while num_rx < len(msg):
                data = s.recv(len(msg)-num_rx)
                if data == b'':
                    print('error')
                    break
                rx_msg.append(data)
                num_rx = num_rx + len(data)
            rx_msg = b''.join(rx_msg)
            if(rx_msg == msg):
                print('echoed', num_rx, 'bytes')
            else:
                print('mismatch', msg, rx_msg)
        time.sleep(10)

if __name__ == '__main__':
    main()

