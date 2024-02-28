"""KEA subnet pools"""
from enum import Enum
import ipaddress


class subnet_type(Enum):
    """Different types of subnets that KEA can handle. This is used to determine the type of pool to use and the
    commands to run on the server."""
    none = None
    v4 = "subnet4"  # TODO: This is a guess
    v6 = "subnet6"
    pd = "subnet6-pd"  # TODO: This is a guess


class Pool(object):
    def __init__(self, ip_range=None, subnet=None):
        """Initialize a pool object
        :param ip_range: A string in the format "Start-End"
        :param subnet: A string in the format "Network/CIDR" or Network/Netmask" or an ipaddress.IPNetwork object
        """
        if ip_range is not None:
            try:
                low, high = ip_range.split("-")
                self.subnet = ipaddress.ip_network(low, high)
                self.subnet_type = subnet_type.none
            except IndexError:
                raise ValueError("Invalid range, looing for a \"-\" in the range")
            except ValueError:
                raise ValueError("Invalid range, looking for two valid IP addresses")
        if type(subnet) is str:
            try:
                self.subnet = ipaddress.ip_network(subnet)
            except ValueError:
                raise ValueError("Invalid subnet")
        else:
            if type(subnet) is ipaddress.IPv6Network:
                self.subnet_type = subnet_type.v6
                self.subnet = subnet
            elif type(subnet) is ipaddress.IPv4Network:
                self.subnet_type = subnet_type.v4
                self.subnet = subnet
            else:
                raise ValueError("Invalid subnet")
    def __dict__(self):
        """Return a dictionary representation of the pool, for making JSON in the format KEA expects"""
        return {"pool": self.ip_range}

    @property
    def ip_range(self):
        """Return the IP range as a string in the format "Start-End" """
        if self.subnet is None:
            return None
        else:
            return f"{self.subnet.hosts()[0]}-{self.subnet.hosts()[-1]}"
    @property
    def network(self):
        """Return the network of the subnet"""
        return str(self.subnet)
    @ip_range.setter
    def ip_range(self, ip_range):
        """Set the IP range from a string in the format "Start-End" """
        try:
            low, high = ip_range.split("-")
            self.subnet = ipaddress.ip_network(low, high)
            self.subnet_type = subnet_type.none
        except IndexError:
            raise ValueError("Invalid range, looing for a \"-\" in the range")
        except ValueError:
            raise ValueError("Invalid range, looking for two valid IP addresses")

    @ip_range.deleter
    def ip_range(self):
        """Delete the IP range. Don't do this, becuae it doesn't do anything."""
        print("yeah, let's not do this, okay?")


class Subnet(object):
    def __init__(self):
        """Initialize a subnet object, with empty strings and lists"""
        self.subnet_type = subnet_type.none
        """The type of subnet, subnet_type.v4, subnet_type.v6, or subnet_type.pd"""
        self.pools = []
        """A list of Pool objects"""
        self.name = ""
        """The name of the subnet"""
        self.id = -1
        """The ID of the subnet. This must be unique on the server, but the only test so far is that it is not negative"""

    def __dict__(self):
        """Return a dictionary representation of the subnet, for making JSON in the format KEA expects"""
        if self.id >= 0:
            if len(self.pools) > 0:
                if self.subnet_type == subnet_type.none:
                    self.subnet_type = self.pools[0].subnet_type
                if self.name is "":
                    self.name = f"{self.pools[0].network}"
                for pool in self.pools:
                    if pool.subnet_type != self.subnet_type:
                        raise ValueError("Pool type does not match subnet type")
                rets = {}
                rets["id"] = self.id
                rets["subnet"] = self.name
                rets["pools"] = []
                for pool in self.pools:
                    rets["pools"].append(pool.__dict__())
                return rets
            else:
                raise ValueError("No pools set")

        else:
            raise ValueError("No ID set")

