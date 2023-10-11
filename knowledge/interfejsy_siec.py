import netifaces

interfaces = netifaces.interfaces()
for interface in interfaces:
    addrs = netifaces.ifaddresses(interface)
    print("addrsx: ", addrs)

    if addrs.get(netifaces.AF_INET): # ipv4
        ip = addrs.get(netifaces.AF_INET)[0]["addr"]
        gateway = netifaces.gateways()["default"][netifaces.AF_INET]
        netmask = addrs.get(netifaces.AF_INET)[0]["netmask"]

        print("ipp: ", ip)
        print("gatewayy: ", gateway)
        print("netmaskk: ", netmask)