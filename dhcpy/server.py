"""
An object to store server information, like IP address, hostname, and interfaces
"""

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
        self.hostname = hostname
        """The hostname of the server, if your into that whole DNS thing"""
        self.interfaces = []
        """A list of interfaces on the server. These are the names used by KEA to identify the interfaces"""
        if interfaces is not None:
            self.interfaces = interfaces
