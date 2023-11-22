import tkinter as tk
import ipaddress
from scanner import Scanner

SCANN_COUNTER = 0


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()

        self.res_label = self.res_label = tk.Label(self, font=("Arial", 16), fg="red", bg="black")
        self.ip_address = None

        self.title("Port Scanner")
        self.configure(bg="black")

        # Put the window at the center of the screen

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width - 300) / 2)
        y_coordinate = int((screen_height - 200) / 2)
        self.geometry(f"300x200+{x_coordinate}+{y_coordinate}")

        # Window elements

        self.header_label = tk.Label(self, text="Port Scanner", font=("Arial", 16), fg="green", bg="black")
        self.header_label.pack(pady=10)

        self.ip_label = tk.Label(self, text="Enter IP address to scan:", font=("Arial", 12), fg="green", bg="black")
        self.ip_label.pack()

        self.entry = tk.Entry(self, font=("Arial", 12), bg="black", fg="green")
        self.entry.pack(pady=10)

        self.scan_button = tk.Button(self, text="Scan Ports", command=self.get_ip, font=("Arial", 12), fg="green",
                                     bg="black")
        self.scan_button.pack()

    def get_ip(self):
        """Get the client ip address"""

        global SCANN_COUNTER
        self.ip_address = self.entry.get()
        if not self.is_valid_ip():
            self.entry.delete(0, tk.END)
            self.ip_label.configure(text="Error! Enter a valid IP...")
        else:
            self.ip_label.configure(text="Scanning...")
            scann_res = Scanner(self.ip_address, 1).open_ports
            self.res_label.configure(text=f"{scann_res}")
            if SCANN_COUNTER == 0:
                self.res_label.pack()
            SCANN_COUNTER += 1

            # option to scann another IP

            self.scan_button.configure(text="Scan Again!")

    def is_valid_ip(self):
        """check if the ip address if valid"""
        try:
            ipaddress.ip_address(self.ip_address)
            return True
        except ValueError:
            return False
