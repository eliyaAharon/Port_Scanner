import socket


class Scanner:

    def __init__(self, ip, scann_option):
        self.ip = ip
        self.ports_scann_option = scann_option
        if scann_option == 1:
            self.open_ports = self.ports_scann_4_one_ip(self.ip, 65536)

    def ports_scann_4_one_ip(self, target_ip, port_range):
        open_ports = []
        for port in range(port_range):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports
