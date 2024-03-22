"""Fucntions for sending commands to KEA server"""
import json
import requests
# from dhcpy.server import Server
from dhcpy.subnet import Pool, Subnet, subnet_type

def send_subnet_to_server(server, subnet, ssl=True):
    """
    Send a subnet to a KEA server
    :param server: a server object with a management IP address and a list of interfaces
    :param subnet: a subnet object
    :return: No idea yet. But it should definitely return something
    """
    headers = {
        "Content-Type": "application/json",
    }
    url = f"https://{server.mgmt_ip4}:8000"
    if not ssl:
        url = f"http://{server.mgmt_ip4}:8000"
    data = {}
    data["command"] = "config-set"
    if subnet.subnet_type == subnet_type.v6:
        data["service"] = ["dhcp6"]
        data["arguments"] = {}
        data["arguments"]["Dhcp6"] = {}
        data["arguments"]["Dhcp6"]["interfaces-config"] = {}
        data["arguments"]["Dhcp6"]["interfaces-config"]["interfaces"] = server.interfaces
        data["arguments"]["Dhcp6"]["calculate-tee-times"] = True
        data["arguments"]["Dhcp6"]["control-socket"] = {} # forget this and bad things happen
        data["arguments"]["Dhcp6"]["control-socket"]["socket-name"] = server.v6_socket
        data["arguments"]["Dhcp6"]["control-socket"]["socket-type"] = "unix"

        data["arguments"]["Dhcp6"]["subnet6"] = [subnet.__dict__()]
        r2 = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
        )
        expected_length = r2.headers.get("Content-Length")
        if expected_length is not None:
            actual_length = r2.raw.tell()
            expected_length = int(expected_length)
            if actual_length < expected_length:
                raise IOError(
                    "incomplete read ({} bytes read, {} more expected)".format(
                        actual_length, expected_length - actual_length
                    )
                )
        print(r2.content)

        # print(json.dumps(data, indent=4))
    elif subnet.subnet_type == subnet_type.v4:
        data["service"] = ["dhcp4"]
        data["arguments"] = {}
        data["arguments"]["Dhcp4"] = {}
        data["arguments"]["Dhcp4"]["interfaces-config"] = {}
        data["arguments"]["Dhcp4"]["interfaces-config"]["interfaces"] = server.interfaces
        data["arguments"]["Dhcp4"]["calculate-tee-times"] = True
        data["arguments"]["Dhcp4"]["control-socket"] = {} # forget this and bad things happen
        data["arguments"]["Dhcp4"]["control-socket"]["socket-name"] = server.v4_socket
        data["arguments"]["Dhcp4"]["control-socket"]["socket-type"] = "unix"

        data["arguments"]["Dhcp4"]["subnet4"] = [subnet.__dict__()]
        r2 = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
        )
        expected_length = r2.headers.get("Content-Length")
        if expected_length is not None:
            actual_length = r2.raw.tell()
            expected_length = int(expected_length)
            if actual_length < expected_length:
                raise IOError(
                    "incomplete read ({} bytes read, {} more expected)".format(
                        actual_length, expected_length - actual_length
                    )
                )
        print(r2.content)

        # print(json.dumps(data, indent=4))
    else:
        print(subnet.subnet_type)
    # print(json.dumps(data))

def get_config(server, ssl=True):
    """
    Get the configuration of a server
    :param server: a server object
    :return: a dictionary of the server configuration
    """
    headers = {
        "Content-Type": "application/json",
    }
    url = f"https://{server.mgmt_ip4}:8000"
    if not ssl:
        url = f"http://{server.mgmt_ip4}:8000"
    data = {}
    data["command"] = "config-get"
    print("Sending request to", url)
    r = requests.post(
        url,
        data=json.dumps(data),
        headers=headers,
        # verify=False
    )
    expected_length = r.headers.get("Content-Length")
    if expected_length is not None:
        actual_length = r.raw.tell()
        expected_length = int(expected_length)
        if actual_length < expected_length:
            raise IOError(
                "incomplete read ({} bytes read, {} more expected)".format(
                    actual_length, expected_length - actual_length
                )
            )
    return json.loads(r.content)

def get_v6_config(server, ssl=True):
    """
    Get the configuration of a server
    :param server: a server object
    :return: a dictionary of the server configuration
    """
    headers = {
        "Content-Type": "application/json",
    }
    url = f"https://{server.mgmt_ip4}:8000"
    if not ssl:
        url = f"http://{server.mgmt_ip4}:8000"
    data = {}
    data["command"] = "config-get"
    data["service"] = ["dhcp6"]
    print("Sending request to", url)
    r = requests.post(
        url,
        data=json.dumps(data),
        headers=headers,
        # verify=False
    )
    expected_length = r.headers.get("Content-Length")
    if expected_length is not None:
        actual_length = r.raw.tell()
        expected_length = int(expected_length)
        if actual_length < expected_length:
            raise IOError(
                "incomplete read ({} bytes read, {} more expected)".format(
                    actual_length, expected_length - actual_length
                )
            )
    return json.loads(r.content)

def get_v4_config(server, ssl=True):
    """
    Get the configuration of a server
    :param server: a server object
    :return: a dictionary of the server configuration
    """
    headers = {
        "Content-Type": "application/json",
    }
    url = f"https://{server.mgmt_ip4}:8000"
    if not ssl:
        url = f"http://{server.mgmt_ip4}:8000"
    data = {}
    data["command"] = "config-get"
    data["service"] = ["dhcp4"]
    print("Sending request to", url)
    r = requests.post(
        url,
        data=json.dumps(data),
        headers=headers,
        # verify=False
    )
    expected_length = r.headers.get("Content-Length")
    if expected_length is not None:
        actual_length = r.raw.tell()
        expected_length = int(expected_length)
        if actual_length < expected_length:
            raise IOError(
                "incomplete read ({} bytes read, {} more expected)".format(
                    actual_length, expected_length - actual_length
                )
            )
    return json.loads(r.content)

def save_config(server, ssl=True):
    """
    Get the configuration of a server
    :param server: a server object
    :return: a dictionary of the server configuration
    """
    headers = {
        "Content-Type": "application/json",
    }
    url = f"https://{server.mgmt_ip4}:8000"
    if not ssl:
        url = f"http://{server.mgmt_ip4}:8000"
    data = {}
    data["command"] = "config-write"
    data["service"] = ["dhcp6", "dhcp4"]
    print("Sending request to", url)
    r = requests.post(
        url,
        data=json.dumps(data),
        headers=headers,
        # verify=False
    )
    expected_length = r.headers.get("Content-Length")
    if expected_length is not None:
        actual_length = r.raw.tell()
        expected_length = int(expected_length)
        if actual_length < expected_length:
            raise IOError(
                "incomplete read ({} bytes read, {} more expected)".format(
                    actual_length, expected_length - actual_length
                )
            )

    return json.loads(r.content)
