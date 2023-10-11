import netifaces

from network import extract_ip_adress
import netifaces
from pprint import pprint


class NetworkInterfaces:

    def __init__(self):
        interfaces = netifaces.interfaces()
        self._inter = self._read_all_interfaces(interfaces)

    @staticmethod
    def _read_all_interfaces(interfaces):
        data = {}
        for interface in interfaces:
            families = netifaces.ifaddresses(interface)
            # print(families)
            # print("---")
            for number, family in families.items():
                for item in family:
                    data[item["addr"]] = item
        return data

    def __getitem__(self, key):
        return self._inter[key]


ip = extract_ip_adress()
network_interfaces = NetworkInterfaces()
print(network_interfaces[ip])
