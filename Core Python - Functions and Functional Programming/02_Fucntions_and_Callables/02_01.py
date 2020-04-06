import socket


def resolve(host):
    return socket.gethostbyname(host)

print(resolve('sixty-north.com')) # 93.93.131.30