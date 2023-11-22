from logo import programm_logo
from cli import CLI
from gui import GUI

print(programm_logo)

interface_choice = int(input("Select 1 for CLI and 2 for GUI: \n> "))
if interface_choice == 1:
    cli = CLI()
elif interface_choice == 2:
    gui = GUI()
    gui.mainloop()

