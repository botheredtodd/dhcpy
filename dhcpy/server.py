"""
An object to store server information, like IP address, hostname, and interfaces
"""
import json

from dhcpy.sendToServer import get_config, get_v6_config, save_config, get_v4_config


class Server(object):
    """
    A KEA server, with an IP address, hostname, and interfaces
    """

    def __init__(self, mgmt_ip4=None, mgmt_ip6=None, hostname=None, interfaces=None):
        self.mgmt_ip4 = mgmt_ip4
        """
        The IPv4 address used the manage the server. This is not neccessarily the IP address used by the DHCP service
        """
        self.v4_socket = "/tmp/kea4-ctrl-socket"
        """
        The control socket for the DHCP6 service. Set to the default value. You can change it if you need to.
        """
        self.mgmt_ip6 = mgmt_ip6
        """
        The IPv6 address used the manage the server. This is not neccessarily the IP address used by the DHCP service
        """
        self.v6_socket = "/tmp/kea6-ctrl-socket"
        """
        The control socket for the DHCP6 service. Set to the default value. You can change it if you need to.
        """
        self.hostname = hostname
        """The hostname of the server, if your into that whole DNS thing"""
        self.interfaces = []
        """A list of interfaces on the server. These are the names used by KEA to identify the interfaces"""
        if interfaces is not None:
            self.interfaces = interfaces

    def get_config(self, ssl=True):
        """
        Get the configuration of the server
        """
        conf = get_config(self, ssl=ssl)
        for key in conf[0]["arguments"]:
            if key == "Control-agent":
                for subkey in conf[0]["arguments"]["Control-agent"]:
                    if subkey == "control-sockets":
                        for subsubkey in conf[0]["arguments"]["Control-agent"][subkey]:
                            if subsubkey == "dhcp4":
                                self.v4_socket = conf[0]["arguments"]["Control-agent"][subkey][subsubkey]["socket-name"]
                            elif subsubkey == "dhcp6":
                                self.v6_socket = conf[0]["arguments"]["Control-agent"][subkey][subsubkey]["socket-name"]



    def get_v6_config(self, ssl=True):
        """
        Get the v6 settings of the server
        """
        return get_v6_config(self, ssl=ssl)

    def get_v4_config(self, ssl=True):
        """
        Get the v6 settings of the server
        """
        return get_v4_config(self, ssl=ssl)

    def save_config(self, ssl=True):
        """
        Write the configuration to the server
        :return: the reply from kea
        """
        return save_config(self, ssl=ssl)


