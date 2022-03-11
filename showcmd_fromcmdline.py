#python script will prompt the user to input show commands at 
#the prompt (comma seperated) and will output results to screen 
import getpass
import time
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

rprint("[bold red on yellow]**************THIS SCRIPT WILL DISPLAY THE OUTPUT FROM THE HOSTS FOR SHOW COMMANDS YOU ENTER*************[/bold red on yellow]")
time.sleep(2)
#displaying a banner to confirm what the script does to the user
nr = InitNornir(config_file="config.yaml")
print("Please enter your Login credentials")
username = input("username: ")
password = getpass.getpass()
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

commands = input ("\nEnter Commands you wish to send (comma seperated): ")
cmds = commands.split(",")

def push_show_commands(task):
    for cmd in cmds:
        task.run(task=send_command, command=cmd)

results = nr.run(task=push_show_commands)
print_result(results)

    
