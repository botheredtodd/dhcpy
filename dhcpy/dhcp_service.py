from dhcpy.subnet import Subnet, Pool, subnet_type

class DhcpService(object):
    def __init__(self):
        """Initialize a DHCP service object, with empty strings and lists"""
        self.subnets = []
        """A list of Subnet objects"""
        self.control_socket = ""
        """The control socket for the DHCP service"""
        self.global_params = {}
        """A dictionary of global DHCP Options for the DHCP service"""
        self.default_nameservers = []
    def add_subnet(self, subnet):
        """Add a subnet to the service"""
        self.subnets.append(subnet)
    def __dict__(self):
        """Return a dictionary representation of the service, for making JSON in the format KEA expects"""
        return "Not implemented on the generic object"

    def update_service(self, server, ssl=True):
        """
        Send the service to the server
        """
        return "Not implemented on the generic object"

class Dhcp4Service(DhcpService):
    def __init__(self):
        """Initialize a DHCP4 service object, with empty strings and lists"""
        super().__init__()
        self.control_socket = "/tmp/kea4-ctrl-socket"
        """The control socket for the DHCP4 service"""

class Dhcp6Service(DhcpService):
    def __init__(self):
        """Initialize a DHCP6 service object, with empty strings and lists"""
        super().__init__()
        self.control_socket = "/tmp/kea6-ctrl-socket"
        """The control socket for the DHCP6 service"""
    def add_subnet(self, subnet):
        """Add a subnet to the service"""
        if subnet.subnet_type not in [subnet_type.v6, subnet_type.pd]:
            raise ValueError("This is a DHCP6 service, you can only add DHCP6 subnets")
        self.subnets.append(subnet)
