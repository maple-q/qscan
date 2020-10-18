# coding: utf-8


def is_valid_ip_v4(ip):
    ip_split = ip.split('.')
    if len(ip_split) != 4:
        return False

    for i in range(4):
        try:
            addr = int(ip_split[i])
        except:
            return False

        if addr < 0 or addr > 255:
            return False

    return True


def is_valid_port(port):
    try:
        port = int(port)
    except:
        return False

    if port <= 0 or port > 65535:
        return False

    return True
