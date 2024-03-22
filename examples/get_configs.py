from dhcpy import Server, Subnet, Pool, subnet_type
# from dhcpy.sendToServer import get_config
import json

# Create a server object
kea_server = Server(
    mgmt_ip4="192.168.100.178",
    hostname="kea0",
    interfaces=["prod"])
print("getting config")
kea_server.get_config(ssl=False)

print(f"v4_socket: {kea_server.v4_socket}")
print(f"v6_socket: {kea_server.v6_socket}")

v6_conf = kea_server.get_v6_config(ssl=False)
# print(json.dumps(v6_conf, indent=4))

# Create a subnet object
# subnet = Subnet()
# pool = Pool(subnet="2001:db8:1::/64")
# pool.subnet_type = subnet_type.v6
# subnet.pools.append(pool)
# subnet.id = 1
# print(json.dumps(subnet.__dict__(), indent=4))
