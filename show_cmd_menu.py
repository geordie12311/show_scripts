import sys
import time
from rich import print as rprint

def quit():
    rprint("The menu will now wait...")
    time.sleep(2)
    sys.exit()

def menu():
    rprint("*****Main Menu*****")
    time.sleep(1)

choice = input("""
        A: Show version
        B: show IP interface brief
        C: Show Running Configuration
        D: Enter Show Commands manually
        Q: Quit programme

        Please make a selection from above menu, you will then be prompted to enter your password
""")
if choice == "A" or choice == "a":
    import show_version
elif choice == "B" or choice == "b":
    import show_ip_intbrief
elif choice == "C" or choice == "c":
    import show_run
elif choice == "D" or choice == "d":
    import showcmd_fromcmdline
elif choice == "Q" or choice == "q":
    menu()
else:
    rprint("Error you must enter a valid option from the Menu")

menu