##
## EPITECH PROJECT, 2021
## get_ip_adress
## File description:
## get_ip_adress.py
##

import socket

hostname = socket.gethostname()
IPAdrr = socket.gethostbyname(hostname)
print("Name is: " + hostname)
print("IP: " + IPAdrr)