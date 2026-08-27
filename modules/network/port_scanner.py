import socket
host=input("Target Host: "); 
[print(f"Port {p}: Open") for p in [21,22,80,443] if socket.socket().connect_ex((host,p))==0]