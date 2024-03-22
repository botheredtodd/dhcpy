from dhcpy import Server, Subnet, Pool, subnet_type, send_subnet_to_server
# from dhcpy.sendToServer import get_config
import json
import ipaddress

# Create a server object
kea_server = Server(
    mgmt_ip4="192.168.100.161",
    mgmt_ip6="2600:1700:2bb0:950::11f7",
    hostname="kea1",
    interfaces=["eth1"])

# Create a subnet object
subnet = Subnet()
pool = Pool(subnet=ipaddress.IPv6Network("2001:db8:1::/64"))
subnet.subnet_type = subnet_type.v6
subnet.pools.append(pool)
subnet.id = 55
# print(json.dumps(subnet.__dict__(), indent=4))

send_subnet_to_server(kea_server, subnet, ssl=False)
kea_server.save_config(ssl=False)
#
# config = kea_server.get_config(ssl=False)
# print(json.dumps(config, indent=4))