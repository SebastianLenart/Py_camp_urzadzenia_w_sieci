import netifaces

from network import extract_ip_adress, convert_mask2, is_unreachable, is_unreachable2
from network import is_reachable_with_ports
import netifaces
import ipaddress
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
# print(network_interfaces[ip])
mask = network_interfaces[ip]["netmask"]
netmask_as_number = convert_mask2(mask)

all_address = ipaddress.IPv4Network(f"{ip}/{netmask_as_number}", strict=False)
for address in all_address.hosts(): # bez koncowki 255 i 0; to jest obiekt i trzeba na str
    # print(address)
    address = str(address)
    # if is_unreachable2(address):
    #     print(address)
    if is_reachable_with_ports(address):
        print(address)






















