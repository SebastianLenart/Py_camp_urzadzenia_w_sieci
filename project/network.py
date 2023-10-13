import socket


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
