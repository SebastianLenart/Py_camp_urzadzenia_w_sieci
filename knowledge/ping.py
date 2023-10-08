import socket
import subprocess


# # 1 sposob
# # ip_address = "109.95.156.170"
# ip_address = "127.0.0.1"
# output = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True)
# print(output.stdout)
# print("unreachable" not in str(output.stdout)) # True


# 2 sposob
ip_address = "127.0.0.1"
answer = False
for port in [80, 443, 8080, 22, 21]:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = socket_obj.connect_ex((ip_address, port))
    if result == 0:
        answer = True
        break
socket_obj.close()
print(answer)




















































