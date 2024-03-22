from dhcpy.subnet import subnet_type
class DhcpOption(object):
    def __init__(self, code, value):
        self.code = code
        self.value = value
        self.space = subnet_type.none
        self.sub_options = []

    def __dict__(self):
        """
        {
                        "always-send": false,
                        "code": 23,
                        "csv-format": true,
                        "data": "2001:db8:2::45, 2001:db8:2::100",
                        "name": "dns-servers",
                        "never-send": false,
                        "space": "dhcp6"
                    },
        """
        return {
            "code": self.code,
            "data": self.value
        }

    def __str__(self):
        return f"Code: {self.code}, Value: {self.value}"