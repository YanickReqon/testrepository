#!/usr/bin/python

import socket


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.10.10.234", 4444))
    s.send("Test vanuit blind")
    s.close()
