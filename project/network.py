import socket
import sys
import subprocess


def extract_ip_adress():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(("1.1.1.1", 1))  # ile bajtow ma wyslac
        local_ip, port = st.getsockname()  # krotka
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        st.close()
    return local_ip


def convert_mask(mask):
    parts = mask.split(".")
    mask = 0
    for octet in parts:
        mask += bin(int(octet)).count("1")
    return mask


def convert_mask2(mask):
    return sum((bin(int(octet)).count("1") for octet in mask.split(".")))  # generator


def is_unreachable(ip_address):
    arg = "-c"
    if sys.platform.startswith("win"):
        arg = "-n"
    output = subprocess.run(["ping", arg, "1", ip_address], capture_output=True)
    # print(output)
    return "unreachable" not in str(output.stdout)


def is_unreachable2(ip_address):
    arg = "-c"
    if sys.platform.startswith("win"):
        arg = "-n"
    try:
        output = subprocess.run(["ping", arg, "1", ip_address], capture_output=True,
                                check=True)  # bez capture wyswietla wszystko
        # print(output)
        return True
    except subprocess.CalledProcessError:
        return False


# czasami ping nie odpowiada bo moze byc tak skonfigurowany
def is_reachable_with_ports(ip_addr):
    for port in range(21, 9000):
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # utp a nie tcp
        socket.setdefaulttimeout(1)
        result = socket_obj.connect_ex((ip_addr, port))
        # print(result)
        if result == 0:
            answer = True
    answer = False
    socket_obj.close() # chyba trzeba deklaracje zmiennej wyciagnac przed fora
    return answer
