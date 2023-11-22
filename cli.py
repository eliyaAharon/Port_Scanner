from scanner import Scanner
import ipaddress


class CLI:

    def __init__(self):
        """Constractor"""
        self.ip = None
        self.scann_option = int(input("Click one to scan a specific IP or 2 to scan the entire network:\n> "))
        if self.scann_option == 1:
            self.get_ip()
        else:
            self.network_scanner()

    def get_ip(self):
        """scann single ip"""
        self.ip = input("Enter IP address to scan\n>")
        while not self.is_valid_ip():
            self.ip = input("\033[91m [invalid] \033[0m Enter IP address to scan\n>")

        scann_res = Scanner(self.ip, self.scann_option)
        if len(scann_res.open_ports) > 0:
            print(f"The open ports for {self.ip} ip is: \n \033[94m {scann_res.open_ports}\033[0m")
        else:
            print(f" \033[94m No open ports for {self.ip} ip address...  {scann_res.open_ports}\033[0m")

    def network_scanner(self):
        """Scann the entire network"""
        self.ip = input("Enter the first ip address in your network, for exemple: \033[94m 192.168.1.1\033[0m\n>")
        while not self.is_valid_ip():
            self.ip = input(
                "\033[91m InValid ip \033[0m Enter the first ip address in your network, for exemple: \033[94m "
                "192.168.1.1\033[0m\n>")

    def is_valid_ip(self):
        """check if the ip address if valid"""
        try:
            ipaddress.ip_address(self.ip)
            return True
        except ValueError:
            return False
