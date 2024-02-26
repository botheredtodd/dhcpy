from enum import Enum
import ipaddress


class subnet_type(Enum):
    none = None
    v4 = "subnet4"  # TODO: This is a guess
    v6 = "subnet6"
    pd = "subnet6-pd"  # TODO: This is a guess


class Pool(object):
    def __init__(self, ip_range=None, subnet=None):
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
        return {"pool": self.ip_range}

    @property
    def ip_range(self):
        if self.subnet is None:
            return None
        else:
            return f"{self.subnet.hosts()[0]}-{self.subnet.hosts()[-1]}"

    @ip_range.setter
    def ip_range(self, ip_range):
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
        print("yeah, let's not do this, okay?")


class Subnet(object):
    def __init__(self):
        self.subnet_type = subnet_type.none
        self.pools = []
        self.name = ""
        self.id = -1

    def __dict__(self):
        if self.id >= 0:
            if len(self.pools) > 0:
                if self.subnet_type == subnet_type.none:
                    self.subnet_type = self.pools[0].subnet_type
                for pool in self.pools:
                    if pool.subnet_type != self.subnet_type:
                        return {"id": int(self.id), "pool": self.pools}
                    else:
                        raise ValueError("Pool type does not match subnet type")
            else:
                raise ValueError("No pools set")

        else:
            raise ValueError("No ID set")

