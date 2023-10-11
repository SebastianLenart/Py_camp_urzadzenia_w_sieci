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

