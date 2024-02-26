class Server(object):
    def __init__(self, svc_ip, hostname=None, interfaces=None):
        self.svc_ip = svc_ip
        self.hostname = hostname
        if interfaces is None:
            self.interfaces = []
        else:
            self.interfaces = interfaces
