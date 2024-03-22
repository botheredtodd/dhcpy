"""
An object to store server information, like IP address, hostname, and interfaces
"""

from dhcpy.sendToServer import get_config, get_v6_config, save_config
class Server(object):
    """
    A KEA server, with an IP address, hostname, and interfaces
    """
    def __init__(self, mgmt_ip4= None, mgmt_ip6= None, hostname=None, interfaces=None):
        self.mgmt_ip4 = mgmt_ip4
        """
        The IPv4 address used the manage the server. This is not neccessarily the IP address used by the DHCP service
        """
        self.mgmt_ip6 = mgmt_ip6
        """
        The IPv6 address used the manage the server. This is not neccessarily the IP address used by the DHCP service
        """
        self.v6_socket = "/tmp/kea6-ctrl-socket"
        """
        The control socket for the IPv6 service. This is the default value for the control socket. You can change it if you need to.
        """
        self.hostname = hostname
        """The hostname of the server, if your into that whole DNS thing"""
        self.interfaces = []
        """A list of interfaces on the server. These are the names used by KEA to identify the interfaces"""
        if interfaces is not None:
            self.interfaces = interfaces

    def get_config(self, ssl=True):
        """
        Get the configuration of a server
        :param server: a server object
        :return: a dictionary of the server configuration
        """
        return get_config(self, ssl=ssl)
    def get_v6_config(self, ssl=True):
        """
        Get the configuration of a server
        :param server: a server object
        :return: a dictionary of the server configuration
        """
        return get_v6_config(self, ssl=ssl)
    def save_config(self, ssl=True):
        """
        Get the configuration of a server
        :param server: a server object
        :return: a dictionary of the server configuration
        """
        return save_config(self, ssl=ssl)

