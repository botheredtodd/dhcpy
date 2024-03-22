from dhcpy import Server, Subnet, Pool, subnet_type, send_subnet_to_server
# from dhcpy.sendToServer import get_config
import json
import ipaddress

# Create a server object
kea_server = Server(
    mgmt_ip4="192.168.100.178",
    # mgmt_ip6="2600:1700:2bb0:950::11f7",
    hostname="kea1",
    interfaces=["prod"])

kea_server.get_config(ssl=False)
# Create a subnet object
subnet = Subnet()
pool = Pool(subnet=ipaddress.IPv4Network("192.168.99.0/24"))
subnet.subnet_type = subnet_type.v4
subnet.pools.append(pool)
subnet.id = 55
# print(json.dumps(subnet.__dict__(), indent=4))

bob = send_subnet_to_server(kea_server, subnet, ssl=False)
print(bob)
print(json.dumps(kea_server.save_config(ssl=False), indent=4))
bobbert = kea_server.get_v4_config(ssl=False)
print(json.dumps(bobbert, indent=4))
#
# config = kea_server.get_config(ssl=False)
# print(json.dumps(config, indent=4))