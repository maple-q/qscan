# coding: utf-8
import socket
import sys
import time

from utils import util

"""
python qscan.py 192.168.0.1 0 65535
"""


def command_help():
    print('USAGE: python qscan.py <IP> <Start_Port> <End_Port>')


def cost_time(func):
    def inner(*args, **kwargs):
        start_time = int(time.time())
        func(*args, **kwargs)
        end_time = int(time.time())
        print('Total Cost Time: {}s'.format(end_time - start_time))

    return inner


def connect_port(ip, start_port, end_port):
    opened_ports = list()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(start_port, end_port + 1):
        try:
            client_socket.connect((ip, port))
            opened_ports.append(port)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            continue

    return opened_ports


@cost_time
def main():
    command_params = sys.argv

    # verify params length
    if len(command_params) != 4:
        command_help()
        return

    # verify IP
    if not util.is_valid_ip_v4(command_params[1]):
        print('IP address is not valid!')
        return

    # verify port
    if not util.is_valid_port(command_params[2]):
        print('Start Port is not valid!')
        return

    if not util.is_valid_port(command_params[3]):
        print('End Port is not valid!')
        return

    start_port = int(command_params[2])
    end_port = int(command_params[3])
    if start_port > end_port:
        print('Start port must less than End port')
        return

    opened_ports = connect_port(command_params[1], start_port, end_port)
    print('{} starts at: '.format(command_params[1]))
    for port in opened_ports:
        print(port)


if __name__ == '__main__':
    main()
